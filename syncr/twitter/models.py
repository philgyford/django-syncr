from django.db import models
from django.conf import settings

class Tweet(models.Model):
    pub_time    = models.DateTimeField(db_index=True)
    twitter_id  = models.BigIntegerField(unique=True)
    text        = models.TextField()
    user        = models.ForeignKey('TwitterUser')
    coordinates_latitude    = models.FloatField(null=True)
    coordinates_longitude   = models.FloatField(null=True)
    in_reply_to_tweet       = models.ForeignKey('self', null=True)
    in_reply_to_user        = models.ForeignKey('TwitterUser', related_name='+', null=True)

    def __unicode__(self):
        return u'%s %s' % (self.user.screen_name, self.pub_time)

    def url(self):
        return u'http://twitter.com/%s/statuses/%s' % (self.user.screen_name, self.twitter_id)

    def protected(self):
        """Is this tweet private?"""
        return self.user.protected
    protected.boolean = True
    protected.short_description = 'Private?'

    def local_pub_time(self):
        '''
        Convert the Twitter timestamp stored in pub_time to the timezone
        specified in DJANGO_SETTINGS_MODULE. Requires pytz.
        '''
        import pytz
        zone = pytz.timezone(settings.TIME_ZONE)
        return self.pub_time.replace(tzinfo=pytz.utc).astimezone(zone)

class TwitterUser(models.Model):
    screen_name = models.CharField(max_length=50)
    twitter_id  = models.PositiveIntegerField(unique=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    location    = models.CharField(max_length=50, blank=True, null=True)
    name        = models.CharField(max_length=50, blank=True, null=True)
    thumbnail_url = models.URLField()
    url         = models.URLField(blank=True, null=True)
    protected   = models.BooleanField(blank=False, null=False, default=0,
                    help_text="Is user private?", verbose_name="Private?")
    friends     = models.ManyToManyField('self', symmetrical=False,
                    blank=True, null=True,
                    related_name='friends_user_set')
    followers   = models.ManyToManyField('self', symmetrical=False,
                    blank=True, null=True,
                    related_name='followers_user_set')
    last_tweet_synced = models.BigIntegerField(blank=True, null=True,
            help_text="If this user has their tweets synced, this is the most recent tweet's Twitter ID.")

    def numFriends(self):
        return self.friends.count()

    def numFollowers(self):
        return self.followers.count()

    def __unicode__(self):
        return self.screen_name
