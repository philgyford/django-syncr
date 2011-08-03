import time, datetime, calendar
import httplib
import urllib, urllib2
import base64
from syncr.delicious.models import Bookmark
from taggit.models import Tag

try:
    import xml.etree.ElementTree as ET
except:
    import elementtree.ElementTree as ET

class DeliciousAPI(object):
    """
    DeliciousAPI is a bare-bones interface to the del.icio.us API. It's
    used by DeliciousSyncr objects and it's not recommended to use it
    directly.
    """
    _deliciousApiHost = 'https://api.del.icio.us/'
    _deliciousApiURL  = 'https://api.del.icio.us/v1/'

    def __init__(self, user, passwd):
        """
        Initialize a DeliciousAPI object.

        Required arguments
          user: The del.icio.us username as a string.
          passwd: The username's password as a string.
        """
        self.user = user
        self.passwd = passwd
        pm = urllib2.HTTPPasswordMgrWithDefaultRealm()
        pm.add_password(None, 'https://' + self._deliciousApiHost, self.user, self.passwd)
        handler = urllib2.HTTPBasicAuthHandler(pm)
        self.opener = urllib2.build_opener(handler)

    def _request(self, path, params=None):
        time.sleep(1.5)
        if params:
            post_data = urllib.urlencode(params)
            url = self._deliciousApiURL + path + post_data
        else:
            url = self._deliciousApiURL + path
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'django/syncr.app.delicious')

        credentials = base64.encodestring("%s:%s" % (self.user, self.passwd))
        request.add_header('Authorization', ('Basic %s' % credentials))

        f = self.opener.open(request)
        return ET.parse(f)

class DeliciousSyncr(object):
    """
    DeliciousSyncr objects sync del.icio.us bookmarks to the Django
    backend. The constructor requires a username and password for
    authenticated access to the API.

    There are three ways to sync:
    - All bookmarks for the user
    - Only recent bookmarks for the user
    - Bookmarks based on a limited search/query functionality. Currently
      based on date, tag, and URL.

    This app requires the excellent ElementTree, which is included in
    Python 2.5.  Otherwise available at:
    http://effbot.org/zone/element-index.htm
    """
    def __init__(self, username, password):
        """
        Construct a new DeliciousSyncr.

        Required arguments
          username: a del.icio.us username
          password: the user's password
        """
        self.delicious = DeliciousAPI(username, password)

    def clean_tags(self, tags):
        """
        Utility method to clean up del.icio.us tags, removing double
        quotes, duplicate tags and return a set of tags.

        Required arguments
          tags: a tag string
        """
        tags = tags.lower().replace('\"', '').split(' ')
        tags = set(tags)
        return tags

    def _syncPost(self, post_elem):
        post_hash = post_elem.attrib['hash']
        time_lst = time.strptime(post_elem.attrib['time'], "%Y-%m-%dT%H:%M:%SZ")
        time_obj = datetime.datetime(*time_lst[0:7])

        try:
            extended = post_elem.attrib['extended']
        except KeyError:
            extended = ''
        default_dict = {
            'description': post_elem.attrib['description'],
            'url': post_elem.attrib['href'],
            # Is post_hash attrib unique to the post/URL or post/username ?!
            'post_hash': post_hash,
            'saved_date': time_obj,
            'extended_info': extended,
        }

        # Save only shared bookmarks
        try:
            is_shared = post_elem.attrib['shared'] # Only set, when it isn't shared
        except KeyError:

            bookmark_obj, created = Bookmark.objects.get_or_create(
                            post_hash=post_hash, defaults=default_dict)

            # Add/remove tags.

            remote_slugs = self.clean_tags(post_elem.attrib['tag'])
            local_slugs = set([])
            local_tags = []
            if not created:
                # Bookmark already in database, so get existing local tags.
                local_tags = bookmark_obj.tags.all()
                local_slugs = set([tag.slug for tag in local_tags])

            # Are there any new slugs to add?
            slugs_to_add = remote_slugs.difference(local_slugs)
            if len(slugs_to_add):
                tags_to_add = []
                for slug in slugs_to_add:
                    tag_obj, tag_created = Tag.objects.get_or_create(
                            slug=slug, defaults={'name':slug}
                    )
                    tags_to_add.append(tag_obj)
                bookmark_obj.tags.add(*tags_to_add)

            # Are there any slugs held locally that have been removed on the remote
            # bookamrk?
            slugs_to_remove = local_slugs.difference(remote_slugs)
            if len(slugs_to_remove):
                tags_to_remove = []
                for tag in local_tags:
                    if tag.slug in slugs_to_remove:
                        tags_to_remove.append(tag)
                bookmark_obj.tags.remove(*tags_to_remove)

            return bookmark_obj
        return None


    def syncRecent(self, count=15, tag=None):
        """
        Synchronize the user's recent bookmarks.

        Optional arguments:
          count: The number of bookmarks to return, default 15, max 100.
          tag: A string. Limit to recent bookmarks that match this tag.
        """
        params = {'count': count}
        if tag: params['tag'] = tag
        result = self.delicious._request('posts/recent?', params)
        root = result.getroot()
        for post in list(root):
            self._syncPost(post)

    def syncAll(self, tag=None):
        """
        Synchronize all of the user's bookmarks. WARNING this may take
        a while! Excessive use may get you throttled.

        Optional arguments
          tag: A string. Limit to all bookmarks that match this tag.
        """
        params = dict()
        if tag: params = {'tag': tag}
        result = self.delicious._request('posts/all?', params)
        root = result.getroot()
        for post in list(root):
            self._syncPost(post)

    def datetime2delicious(self, dt):
        """
        Utility method to convert a Python datetime to a string format
        suitable for the del.icio.us API.

        Required arguments
          dt: a datetime object
        """
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    def syncBookmarks(self, **kwargs):
        """
        Synchronize bookmarks. If no arguments are used, today's
        bookmarks will be sync'd.

        Optional keyword arguments
          date: A datetime object. Sync only bookmarks from this date.
          tag: A string. Limit to bookmarks matching this tag.
          url: A string. Limit to bookmarks matching this URL.
        """
        params = kwargs
        if kwargs.has_key('date'):
            params['date'] = self.datetime2delicious(params['date'])
        result = self.delicious._request('posts/get?', )
        root = result.getroot()
        for post in list(root):
            self._syncPost(post)
