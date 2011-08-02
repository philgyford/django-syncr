import time
from datetime import datetime
import twitter
from django.utils.encoding import smart_unicode
from syncr.twitter.models import TwitterUser, Tweet

class TwitterSyncr(object):
    """TwitterSyncr objects sync Twitter information to the Django
    backend. This includes meta data for Twitter users in addition to
    Twitter status updates (Tweets).

    NOTE: Limitations of the Twitter API currently restricts API
    access to only the most recent data in the Twitter system. This
    is for performance reasons (per API docs).

    This app depends on python-twitter:
    http://code.google.com/p/python-twitter/
    """
    def __init__(self, username, consumer_key, consumer_secret, access_token_key, access_token_secret):
        """Construct a new TwitterSyncr object.

        Required arguments
          username: the Twitter username associated with the OAuth credentials
          consumer_key: the Twitter app consumer key for authentication
          consumer_secret: the Twitter app consumer secret for authentication
          access_token_key: the Twitter app access token key for authentication
          access_token_secret: the Twitter app access token secret for authentication
        """
        self.username = username
        self.api = twitter.Api(
                consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token_key,
                access_token_secret=access_token_secret)

        # Caches username: twitter_user_data
        self.user_cache = dict()

        # Caches username: TwitterUser object
        self.user_obj_cache = dict()

    def _getUser(self, user):
        """Retrieve Twitter user information, caching for performance
        purposes.

        Required arguments
          user: a Twitter username as a string.
        """
        if self.user_cache.has_key(user):
            return self.user_cache[user]
        else:
            tw_user = self.api.GetUser(user)
            self.user_cache[user] = tw_user
            return self.user_cache[user]

    def _syncTwitterUser(self, user):
        """Synchronize a twitter.User object with the Django backend

        Required arguments
          user: a twitter.User object.
        """
        if self.user_obj_cache.has_key(user):
            user_obj = self.user_obj_cache[user]
        else:
            try:
                user_obj = TwitterUser.objects.get(twitter_id = user.id)
            except TwitterUser.DoesNotExist:
                user_obj = TwitterUser(twitter_id = user.id)
            user_obj.screen_name     = user.screen_name
            user_obj.description     = user.description
            user_obj.location        = user.location
            user_obj.name            = user.name
            user_obj.thumbnail_url   = user.profile_image_url
            user_obj.url             = user.url
            user_obj.protected       = user.protected
            user_obj.save()
            self.user_obj_cache[user] = user_obj
        return user_obj

    def _syncTwitterStatus(self, status, follow_conversations=False):
        """
        Take a twitter.Status object and synchronize it to Django.

        Args:
          status: a twitter.Status object.

        Optional arguments
          follow_conversations: Boolean, do we fetch tweets this is in-reply-to?

        Returns:
          A syncr.twitter.models.Tweet Django object.
        """
        user_obj = self._syncTwitterUser(status.user)
        pub_time = time.strptime(status.created_at, "%a %b %d %H:%M:%S +0000 %Y")
        pub_time = datetime.fromtimestamp(time.mktime(pub_time))
        default_dict = {'pub_time': pub_time,
                        'twitter_id': status.id,
                        'text': smart_unicode(status.text),
                        'user': user_obj,
                        }

        if status.coordinates:
            default_dict['coordinates_latitude'] = status.coordinates['coordinates'][1]
            default_dict['coordinates_longitude'] = status.coordinates['coordinates'][0]

        if follow_conversations and status.in_reply_to_status_id:
            reply_tweet = self.syncTweet(status.in_reply_to_status_id,
                            follow_conversations=follow_conversations)
            default_dict['in_reply_to_tweet'] = reply_tweet
            default_dict['in_reply_to_user'] = reply_tweet.user

        obj, created = Tweet.objects.get_or_create(twitter_id = status.id,
                                                   defaults = default_dict)
        return obj

    def syncUser(self, user):
        """Synchronize a Twitter user with the Django backend

        Required arguments
          user: a Twitter username as a string
        """
        user_obj = self._syncTwitterUser(self._getUser(user))
        return user_obj

    def syncTweet(self, status_id, follow_conversations=False):
        """Synchronize a Twitter status update by id

        If the tweet is in reply to another, that (and its user) will be fetched,
        and so on, recursively.

        Required arguments
          status_id: a Twitter status update id

        Optional arguments
          follow_conversations: Boolean, do we fetch tweets this is in-reply-to?
        """
        status_obj = self.api.GetStatus(status_id)
        return self._syncTwitterStatus(status_obj,
                follow_conversations=follow_conversations)

    def syncTwitterUserTweets(self, user, follow_conversations=False):
        """Synchronize a Twitter user's tweets with Django (currently
        only the last 20 updates)

        Required arguments
          user: the Twitter user as string

        Optional arguments
          follow_conversations: Boolean, do we fetch tweets these are in-reply-to?
        """
        statuses = self.api.GetUserTimeline(user)
        for status in statuses:
            self._syncTwitterStatus(status,
                    follow_conversations=follow_conversations)

    def syncFriends(self, user):
        """Synchronize a Twitter user's friends with Django.

        Required arguments
          user: the Twitter username as a string
        """
        user_obj = self._syncTwitterUser(self._getUser(user))
        friends = self.api.GetFriends(user)

        # sync our list of twitter.User objs as into ORM
        for friend in friends:
            obj = self._syncTwitterUser(friend)
            user_obj.friends.add(obj)

    def syncFollowers(self, user):
        """Synchronize the Twitter user's followers with Django.
        """
        user_obj = self._syncTwitterUser(self._getUser(user))
        followers = self.api.GetFollowers()

        # sync our list of twitter.User objs into ORM
        for follower in followers:
            obj = self._syncTwitterUser(follower)
            user_obj.followers.add(obj)

    def syncFriendsTweets(self, follow_conversations=False):
        """Synchronize the tweets of the authenticated Twitter user's friends 
        (currently only the last 20 updates). Also automatically add these users
        as friends in the Django database, if they aren't already.

        NOTE: Only works on the currently authenticated user.

        Optional arguments
          follow_conversations: Boolean, do we fetch tweets these are in-reply-to?
        """
        friend_updates = self.api.GetFriendsTimeline()
        user_obj = self._syncTwitterUser(self._getUser(self.username))

        # loop through twitter.Status objects and sync them
        for update in friend_updates:
            self._syncTwitterStatus(update,
                        follow_conversations=follow_conversations)
            friend = self._syncTwitterUser(update.user)
            user_obj.friends.add(friend)

