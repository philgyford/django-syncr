import time
from datetime import datetime
import twitter
from django.utils.encoding import smart_unicode
from syncr.twitter.models import TwitterUser, Tweet
from syncr.app.service import ServiceSyncr

class TwitterSyncr(ServiceSyncr):
    """
    TwitterSyncr objects sync Twitter information to the Django
    backend. This includes meta data for Twitter users in addition to
    Twitter status updates (Tweets).

    NOTE: Limitations of the Twitter API currently restricts API
    access to only the most recent data in the Twitter system. This
    is for performance reasons (per API docs).

    Set the follow_conversations attribute to True before calling methods if you
    want to follow in-reply-to IDs and fetch conversations that synced tweets are
    involved in (more queries).

    This app depends on python-twitter:
    http://code.google.com/p/python-twitter/
    """
    def __init__(self, username, consumer_key, consumer_secret, access_token_key, access_token_secret, *args, **kwargs):
        """
        Construct a new TwitterSyncr object.

        Required arguments
          username: the Twitter username associated with the OAuth credentials
          consumer_key: the Twitter app consumer key for authentication
          consumer_secret: the Twitter app consumer secret for authentication
          access_token_key: the Twitter app access token key for authentication
          access_token_secret: the Twitter app access token secret for authentication
        """
        super(TwitterSyncr, self).__init__(*args, **kwargs)
        self.username = username
        self.api = twitter.Api(
                consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token_key,
                access_token_secret=access_token_secret)

        # When fetching each tweet, do we want to fetch the tweet that it is
        # in-reply-to? And the same with that one in turn, etc?
        # Can make for a lot more requests, but we end up with complete
        # conversations.
        self.follow_conversations = False

        # Caches username: twitter_user_data
        self.user_cache = dict()

        # Caches twitter_id: TwitterUser object
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
        if self.user_obj_cache.has_key(user.id):
            user_obj = self.user_obj_cache[user.id]
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
            self.user_obj_cache[user.id] = user_obj
        return user_obj


    def _syncTwitterStatus(self, status):
        """
        Take a twitter.Status object and synchronize it to Django.

        Args:
          status: a twitter.Status object.

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

        if self.follow_conversations and status.in_reply_to_status_id:
            reply_tweet = self.syncTweet(status.in_reply_to_status_id)
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


    def syncTweet(self, status_id):
        """Synchronize a Twitter status update by id

        If the tweet is in reply to another, that (and its user) will be fetched,
        and so on, recursively.

        Required arguments
          status_id: a Twitter status update id
        """
        status_obj = self.api.GetStatus(status_id)
        return self._syncTwitterStatus(status_obj,
                )


    def syncTwitterUserTweets(self, user, count=20, since_id=None):
        """
        Synchronize a Twitter user's tweets with Django.

        We save the tweet ID of the most recent tweet to the user's
        last_tweet_synced attribute. This is used when calling
        syncTwitterUserNewTweets().k

        Required arguments
          user: the Twitter user as string, eg 'philgyford'

        Optional arguments
          count: The number of tweets to fetch (3200 is the maximum fetchable).
          since_id: Returns tweets that have IDs greater than this. If set, we will
        """
        max_per_page = 200 # Twitter's maximum number.
        if count < max_per_page:
            fetch_per_page = count
        else:
            fetch_per_page = max_per_page
        num_remaining = count
        page = 1
        max_tweet_id = 0
        while num_remaining > 0:
            statuses = self.api.GetUserTimeline(screen_name=user, include_rts=True,
                                count=fetch_per_page, since_id=since_id, page=page)
            if len(statuses):
                for status in statuses:
                    self._syncTwitterStatus(status)
                    if status.id > max_tweet_id:
                        max_tweet_id = status.id
                num_remaining = count - (page * max_per_page)
                page += 1
                time.sleep(2)
            else:
                break

        # This should be the only place we do this. 
        # Don't want to update last_tweet_synced if we're only getting
        # some tweets by one user when they're in another user's timeline, 
        # for example.
        # Used by syncTwitterUserNewTweets()
        if max_tweet_id != 0:
            tu = TwitterUser.objects.get(screen_name=user)
            tu.last_tweet_synced = max_tweet_id
            tu.save()


    def syncTwitterUserNewTweets(self, user, count=20):
        """
        Use this if you want to do the same as syncTwitterUserTweets() but
        automatically only fetch the tweets by the user since last time we called
        this or that function.

        Required arguments
          user: the Twitter user as string, eg 'philgyford'

        Optional arguments
          count: The number of tweets to fetch (3200 is the maximum fetchable).
        """
        try:
            tu = TwitterUser.objects.get(screen_name=user)
            since_id = tu.last_tweet_synced
        except TwitterUser.DoesNotExist:
            since_id = None

        return self.syncTwitterUserTweets(user, count=count,
                                                        since_id=since_id)


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


    def syncFriendsTweets(self, count=20, since_id=None):
        """
        Synchronize the tweets of the authenticated Twitter user's friends.

        Also automatically add these users
        as friends in the Django database, if they aren't already.

        NOTE: Only works on the currently authenticated user.

        Optional arguments
          count: The number of tweets to fetch
          since_id: Returns tweets that have IDs greater than this.
        """
        user_obj = self._syncTwitterUser(self._getUser(self.username))

        # If python.twitter changes to use home_timeline instead of 
        # friends_timeline, I expect this will change to 200.
        max_per_page = 100 # python.twitter's maximum
        if count < max_per_page:
            fetch_per_page = count
        else:
            fetch_per_page = max_per_page
        num_remaining = count
        page = 1
        while num_remaining > 0:
            statuses = self.api.GetFriendsTimeline(retweets=True,
                                count=fetch_per_page, since_id=since_id, page=page)
            if len(statuses):
                for status in statuses:
                    self._syncTwitterStatus(status)
                    friend = self._syncTwitterUser(status.user)
                    user_obj.friends.add(friend)
                num_remaining = count - (page * max_per_page)
                page += 1
                time.sleep(2)
            else:
                break

