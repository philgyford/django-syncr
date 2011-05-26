# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Tweet.coordinates_latitude'
        db.add_column('twitter_tweet', 'coordinates_latitude', self.gf('django.db.models.fields.FloatField')(null=True), keep_default=False)

        # Adding field 'Tweet.coordinates_longitude'
        db.add_column('twitter_tweet', 'coordinates_longitude', self.gf('django.db.models.fields.FloatField')(null=True), keep_default=False)

        # Adding field 'Tweet.in_reply_to_tweet'
        db.add_column('twitter_tweet', 'in_reply_to_tweet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['twitter.Tweet'], null=True), keep_default=False)

        # Adding field 'Tweet.in_reply_to_user'
        db.add_column('twitter_tweet', 'in_reply_to_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['twitter.TwitterUser']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Tweet.coordinates_latitude'
        db.delete_column('twitter_tweet', 'coordinates_latitude')

        # Deleting field 'Tweet.coordinates_longitude'
        db.delete_column('twitter_tweet', 'coordinates_longitude')

        # Deleting field 'Tweet.in_reply_to_tweet'
        db.delete_column('twitter_tweet', 'in_reply_to_tweet_id')

        # Deleting field 'Tweet.in_reply_to_user'
        db.delete_column('twitter_tweet', 'in_reply_to_user_id')


    models = {
        'twitter.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'coordinates_latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'coordinates_longitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_reply_to_tweet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['twitter.Tweet']", 'null': 'True'}),
            'in_reply_to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': "orm['twitter.TwitterUser']"}),
            'pub_time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'twitter_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['twitter.TwitterUser']"})
        },
        'twitter.twitteruser': {
            'Meta': {'object_name': 'TwitterUser'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'followers_user_set'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['twitter.TwitterUser']"}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'friends_user_set'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['twitter.TwitterUser']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'thumbnail_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['twitter']
