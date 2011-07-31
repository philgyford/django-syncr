from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Video(models.Model):
    feed        = models.URLField()
    video_id    = models.CharField(max_length=50, verbose_name="Video ID")
    published   = models.DateTimeField()
    updated     = models.DateTimeField()
    title       = models.CharField(max_length=250)
    author      = models.ForeignKey('YoutubeUser')
    description = models.TextField(blank=True)
    view_count  = models.PositiveIntegerField()
    url         = models.URLField(verbose_name="URL")
    thumbnail_url = models.URLField(blank=True, verbose_name="Thumbnail URL")
    length      = models.PositiveIntegerField()

    tags = TaggableManager(blank=True) 

    def _get_tag_list(self):
        return ', '.join(self.tags.all())
    tag_list = property(_get_tag_list)

    def embed_url(self):
        return u'http://www.youtube.com/v/%s' % self.video_id

    def __unicode__(self):
        return u'%s' % self.title

class Playlist(models.Model):
    feed        = models.URLField()
    updated     = models.DateTimeField()
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    author      = models.ForeignKey('YoutubeUser')
    url         = models.URLField(verbose_name="URL")
    videos      = models.ManyToManyField('PlaylistVideo')

    def __unicode__(self):
        return u'%s' % self.title

    def numVideos(self):
        return self.videos.count()

class PlaylistVideo(models.Model):
    feed        = models.URLField()
    title       = models.CharField(max_length=250, help_text="Playlist creators can give videos new titles")
    description = models.TextField(blank=True, help_text="Playlist creators can give videos new descriptions")
    original    = models.ForeignKey('Video')

    def __unicode__(self):
        return u'%s' % self.title
    
class YoutubeUser(models.Model):
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'))
    feed        = models.URLField()
    username    = models.CharField(max_length=50)
    first_name  = models.CharField(max_length=50)
    age         = models.PositiveIntegerField(null=True, blank=True)
    gender      = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    thumbnail_url = models.URLField(verbose_name="Thumbnail URL")
    watch_count = models.PositiveIntegerField()
    url         = models.URLField(verbose_name="URL")
    playlists   = models.ManyToManyField('Playlist')
    favorites   = models.ManyToManyField('Video', related_name='favorited_by')
    uploads     = models.ManyToManyField('Video', related_name='uploaded_by')
    user        = models.OneToOneField(User, related_name="youtube_acct",
                    null=True, blank=True, help_text="To associate a YouTube user with a user on this website")

    class Meta:
        verbose_name = "YouTube user"

    def __unicode__(self):
        return u'%s' % self.username
    
    def sync(self):
        from syncr.app.youtube import YoutubeSyncr
        yts = YoutubeSyncr()
        yts.syncUser(self.username)
        yts.syncUserUploads(self.username)
        yts.syncUserFavorites(self.username)
        yts.syncUserPlaylists(self.username)
        
