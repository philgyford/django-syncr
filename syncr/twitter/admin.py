from django.contrib import admin
from syncr.twitter.models import Tweet, TwitterUser

class TweetAdmin(admin.ModelAdmin):
	date_hierarchy = 'pub_time'
	list_display = ('user', 'protected', 'pub_time', 'text')
	
class TwitterUserAdmin(admin.ModelAdmin):
	list_display = ('screen_name', 'name', 'protected', 'location')
	
	
admin.site.register(Tweet, TweetAdmin)
admin.site.register(TwitterUser, TwitterUserAdmin)
