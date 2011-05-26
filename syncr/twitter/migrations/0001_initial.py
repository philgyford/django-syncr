# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Tweet'
        db.create_table('twitter_tweet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pub_time', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('twitter_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['twitter.TwitterUser'])),
        ))
        db.send_create_signal('twitter', ['Tweet'])

        # Adding model 'TwitterUser'
        db.create_table('twitter_twitteruser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('screen_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('thumbnail_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('twitter', ['TwitterUser'])

        # Adding M2M table for field friends on 'TwitterUser'
        db.create_table('twitter_twitteruser_friends', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_twitteruser', models.ForeignKey(orm['twitter.twitteruser'], null=False)),
            ('to_twitteruser', models.ForeignKey(orm['twitter.twitteruser'], null=False))
        ))
        db.create_unique('twitter_twitteruser_friends', ['from_twitteruser_id', 'to_twitteruser_id'])

        # Adding M2M table for field followers on 'TwitterUser'
        db.create_table('twitter_twitteruser_followers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_twitteruser', models.ForeignKey(orm['twitter.twitteruser'], null=False)),
            ('to_twitteruser', models.ForeignKey(orm['twitter.twitteruser'], null=False))
        ))
        db.create_unique('twitter_twitteruser_followers', ['from_twitteruser_id', 'to_twitteruser_id'])


    def backwards(self, orm):
        
        # Deleting model 'Tweet'
        db.delete_table('twitter_tweet')

        # Deleting model 'TwitterUser'
        db.delete_table('twitter_twitteruser')

        # Removing M2M table for field friends on 'TwitterUser'
        db.delete_table('twitter_twitteruser_friends')

        # Removing M2M table for field followers on 'TwitterUser'
        db.delete_table('twitter_twitteruser_followers')


    models = {
        'twitter.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
