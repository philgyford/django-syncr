# django-syncr

**A collection of Django applications for saving your activity on other websites (such as Flickr, Twitter, YouTube, etc) in your local database.** 

This project was begun by Jesse Legg [at Google Code](http://code.google.com/p/django-syncr/), which seemed to stop in 2008. Dan Fairs [did some updates](https://github.com/danfairs/django-syncr) until 2010. Phil Gyford [is currently working on this fork](https://github.com/philgyford/django-syncr).

See [the Issues](https://github.com/philgyford/django-syncr/issues) for known new issues, or the [Google Code issues](http://code.google.com/p/django-syncr/issues/list) for older ones, possibly still extant.

I have only tested these apps using Django 1.3 with Python 2.6.


## Overview

django-syncr consists of one app per third-party service. Each app has a set of models to represent its entities (users, photos, tweets, etc) in your database, and utilities to fetch the remote data and store it locally.

It's possible to install only the apps for the services you want to sync with. Syncing is only one-way (changes to your local database are not pushed to third-party services). If changes are made on third-party services, it's not automatic that those changes will be pulled back to your local database. 

django-syncr provides no views or templates for viewing your locally-stored data, although you can access it all via the Django admin, if you're using that.


## Services

Here are the services covered, with their dependencies, and the rough known state of their functionality.


### [Twitter](http://www.twitter.com/)

**Roughly tested, appears to work.**

Requires: [python-twitter](http://code.google.com/p/python-twitter/)

Can fetch a user's Tweets, lists of Friends and Followers, and Friends' Tweets.  The quantity of each is currently quite limited. Stores the in-reply-to and latitude/longitude of each Tweet, if available, and most of the users' data.


### [Flickr](http://www.flickr.com/)

**Roughly tested, appears to work.**

Requires: [flickrapi](http://stuvel.eu/flickrapi), [django-tagging](http://code.google.com/p/django-tagging/).

Can fetch a user's public photos, recent photos, public favorites, photo sets.  The Photo model stores most/all data, including geo and EXIF data. Comments on photos are also stored. The images themselves are not stored locally.


### [Delicious](http://www.delicious.com/)

**Roughly tested, appears to work.**

Requires: [django-tagging](http://code.google.com/p/django-tagging/).

Fetches a user's bookmarks. All, most recent, a specific tag, or a specific date.


### [YouTube](http://www.youtube.com/)

**Roughly tested, appears to work.**

Requires: [django-tagging](http://code.google.com/p/django-tagging/).

Fetches a user's playlists, favorites and uploads. Stores data about videos such as view counts, length, descriptions, tags, etc. The videos themselves are not stored locally.


### Google Code, Picasa, Readernaut, Tumblr

**Not yet checked.**


### Brightkite

**No longer works.** Brightkite have removed their "check in" functionality which this app used to sync. This app may be removed in future.


### Magnolia

**Service no longer exists.** This app has been removed.



## Installation

Based on the [original docs at Google Code](http://code.google.com/p/django-syncr/).

1. [Create your own fork](http://help.github.com/fork-a-repo/) or check out
   this one:

	```git clone git@github.com:philgyford/django-syncr.git```

2. Add syncr to your PYTHONPATH. This might just involve putting the 'syncr'
   directory in your Django project, or symlinking it there.

3. Add the required apps to the INSTALLED_APPS in your Django settings file.
   eg:

	```INSTALLED_APPS = (
	...
	'syncr.flickr',
	'syncr.twitter',
	)
	```

4. Write code that will access the methods in the appropriate module in
   syncr/app/\*.py eg:

	```from syncr.app.flickr import FlickrSyncr
    f = FlickrSyncr(FLICKR_API_KEY, FLICKR_API_SECRET)
    
    \# sync all my photos from the past week...
    f.syncRecentPhotos('username', days=7)
    
    \# sync my favorite photos list
    f.syncPublicFavorites('username')
	```


More documentation may come at a later date.

