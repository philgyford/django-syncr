# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Bookmark'
        db.create_table('delicious_bookmark', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=2000)),
            ('url_hash', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('extended_info', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('post_hash', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('saved_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('delicious', ['Bookmark'])


    def backwards(self, orm):
        
        # Deleting model 'Bookmark'
        db.delete_table('delicious_bookmark')


    models = {
        'delicious.bookmark': {
            'Meta': {'ordering': "('-saved_date',)", 'object_name': 'Bookmark'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'extended_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_hash': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'saved_date': ('django.db.models.fields.DateTimeField', [], {}),
            'tags': ('tagging.fields.TagField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '2000'}),
            'url_hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        }
    }

    complete_apps = ['delicious']
