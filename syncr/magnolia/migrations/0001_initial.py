# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Link'
        db.create_table('magnolia_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('magnolia_id', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('screen_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('add_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('tags', self.gf('tagging.fields.TagField')()),
        ))
        db.send_create_signal('magnolia', ['Link'])


    def backwards(self, orm):
        
        # Deleting model 'Link'
        db.delete_table('magnolia_link')


    models = {
        'magnolia.link': {
            'Meta': {'ordering': "['-add_date']", 'object_name': 'Link'},
            'add_date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'magnolia_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'screen_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['magnolia']
