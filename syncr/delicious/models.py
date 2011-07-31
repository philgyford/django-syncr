from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
import hashlib

class Bookmark(models.Model):
    # description, href, tags, extended, dt
    description = models.CharField(max_length=255, blank=True)
    # URLField won't allow unique=True when max_length is more than 255,
    # but we need to allow longer URLs...
    url = models.URLField(max_length=2000, verbose_name='URL')
    # ...so we generate a hash based on the URL and make sure that's unique.
    url_hash = models.CharField(max_length=32, unique=True, verbose_name='URL hash',
            help_text="Hash based on the URL to ensure URLs are unique")
    extended_info = models.TextField(blank=True)
    post_hash = models.CharField(max_length=100, help_text="Delicious's identifier for this bookmark")
    saved_date = models.DateTimeField()

    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ('-saved_date',)
        get_latest_by = 'saved_date'

    def __unicode__(self):
        return self.description

    @models.permalink
    def get_absolute_url(self):
        return ('bookmark_detail', (), { 'year': self.saved_date.strftime('%Y'),
                                         'month': self.saved_date.strftime('%m'),
                                         'day': self.saved_date.strftime('%d'),
                                         'object_id': self.id })

    def save(self, *args, **kwargs):
        '''
        Override default save method, so we can computer the url_hash.
        '''
        self.url_hash = hashlib.md5(self.url.encode('utf-8')).hexdigest()
        super(Bookmark, self).save(*args, **kwargs) # Call the "real" save() method.

    def local_saved_date(self):
	'''
	Convert the delicious saved datetime to the timezone specified in
	DJANGO_SETTINGS_MODULE. Requires pytz.
	'''
	import pytz
	zone = pytz.timezone(settings.TIME_ZONE)
	return self.saved_date.replace(tzinfo=pytz.utc).astimezone(zone)
