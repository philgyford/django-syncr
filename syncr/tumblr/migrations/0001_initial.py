# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TumblrPost'
        db.create_table('tumblr_tumblrpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('source', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('post_id', self.gf('django.db.models.fields.IntegerField')()),
            ('format', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('post_link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('feed_item', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('pub_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('tumblelog', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('tumblr', ['TumblrPost'])

        # Adding model 'TumblrPhoto'
        db.create_table('tumblr_tumblrphoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url_to_photo', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('link_500', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('link_400', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('link_250', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('link_100', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('link_75', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('photo_caption', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('photo_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('tumblr', ['TumblrPhoto'])

        # Adding model 'TumblrLink'
        db.create_table('tumblr_tumblrlink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link_text', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('link_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('link_id', self.gf('django.db.models.fields.IntegerField')()),
            ('link_description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('tumblr', ['TumblrLink'])

        # Adding model 'TumblrConversation'
        db.create_table('tumblr_tumblrconversation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('conversation_text', self.gf('django.db.models.fields.TextField')()),
            ('conversation_title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('conversation_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('tumblr', ['TumblrConversation'])

        # Adding model 'TumblrQuote'
        db.create_table('tumblr_tumblrquote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quote_text', self.gf('django.db.models.fields.TextField')()),
            ('quote_source', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('quote_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('tumblr', ['TumblrQuote'])

        # Adding model 'TumblrRegular'
        db.create_table('tumblr_tumblrregular', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('regular_body', self.gf('django.db.models.fields.TextField')()),
            ('regular_title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('regular_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('tumblr', ['TumblrRegular'])

        # Adding model 'TumblrAudio'
        db.create_table('tumblr_tumblraudio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('audio_player', self.gf('django.db.models.fields.TextField')()),
            ('audio_caption', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('audio_plays', self.gf('django.db.models.fields.IntegerField')()),
            ('audio_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('tumblr', ['TumblrAudio'])

        # Adding model 'TumblrVideo'
        db.create_table('tumblr_tumblrvideo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video_caption', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('video_player', self.gf('django.db.models.fields.TextField')()),
            ('video_source', self.gf('django.db.models.fields.TextField')()),
            ('video_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('tumblr', ['TumblrVideo'])


    def backwards(self, orm):
        
        # Deleting model 'TumblrPost'
        db.delete_table('tumblr_tumblrpost')

        # Deleting model 'TumblrPhoto'
        db.delete_table('tumblr_tumblrphoto')

        # Deleting model 'TumblrLink'
        db.delete_table('tumblr_tumblrlink')

        # Deleting model 'TumblrConversation'
        db.delete_table('tumblr_tumblrconversation')

        # Deleting model 'TumblrQuote'
        db.delete_table('tumblr_tumblrquote')

        # Deleting model 'TumblrRegular'
        db.delete_table('tumblr_tumblrregular')

        # Deleting model 'TumblrAudio'
        db.delete_table('tumblr_tumblraudio')

        # Deleting model 'TumblrVideo'
        db.delete_table('tumblr_tumblrvideo')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tumblr.tumblraudio': {
            'Meta': {'object_name': 'TumblrAudio'},
            'audio_caption': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'audio_id': ('django.db.models.fields.IntegerField', [], {}),
            'audio_player': ('django.db.models.fields.TextField', [], {}),
            'audio_plays': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tumblr.tumblrconversation': {
            'Meta': {'object_name': 'TumblrConversation'},
            'conversation_id': ('django.db.models.fields.IntegerField', [], {}),
            'conversation_text': ('django.db.models.fields.TextField', [], {}),
            'conversation_title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tumblr.tumblrlink': {
            'Meta': {'object_name': 'TumblrLink'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_description': ('django.db.models.fields.TextField', [], {}),
            'link_id': ('django.db.models.fields.IntegerField', [], {}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'link_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'tumblr.tumblrphoto': {
            'Meta': {'object_name': 'TumblrPhoto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_100': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'link_250': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'link_400': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'link_500': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'link_75': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'photo_caption': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'photo_id': ('django.db.models.fields.IntegerField', [], {}),
            'url_to_photo': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'tumblr.tumblrpost': {
            'Meta': {'ordering': "('-pub_time',)", 'object_name': 'TumblrPost'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'feed_item': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'format': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'post_id': ('django.db.models.fields.IntegerField', [], {}),
            'post_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'pub_time': ('django.db.models.fields.DateTimeField', [], {}),
            'source': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'tumblelog': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'tumblr.tumblrquote': {
            'Meta': {'object_name': 'TumblrQuote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote_id': ('django.db.models.fields.IntegerField', [], {}),
            'quote_source': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'quote_text': ('django.db.models.fields.TextField', [], {})
        },
        'tumblr.tumblrregular': {
            'Meta': {'object_name': 'TumblrRegular'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'regular_body': ('django.db.models.fields.TextField', [], {}),
            'regular_id': ('django.db.models.fields.IntegerField', [], {}),
            'regular_title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'tumblr.tumblrvideo': {
            'Meta': {'object_name': 'TumblrVideo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video_caption': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'video_id': ('django.db.models.fields.IntegerField', [], {}),
            'video_player': ('django.db.models.fields.TextField', [], {}),
            'video_source': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['tumblr']
