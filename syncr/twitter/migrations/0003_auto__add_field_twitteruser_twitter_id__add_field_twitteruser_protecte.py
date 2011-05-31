# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'TwitterUser.twitter_id'
        db.add_column('twitter_twitteruser', 'twitter_id', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, null=True), keep_default=False)

        # Adding field 'TwitterUser.protected'
        db.add_column('twitter_twitteruser', 'protected', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'TwitterUser.twitter_id'
        db.delete_column('twitter_twitteruser', 'twitter_id')

        # Deleting field 'TwitterUser.protected'
        db.delete_column('twitter_twitteruser', 'protected')


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
            'protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'thumbnail_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'twitter_id': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['twitter']
