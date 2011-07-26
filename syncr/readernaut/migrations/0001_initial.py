# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Book'
        db.create_table('readernaut_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book_id', self.gf('django.db.models.fields.IntegerField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('cover_small', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('cover_medium', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('cover_large', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('permalink', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('modified', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('readernaut', ['Book'])


    def backwards(self, orm):
        
        # Deleting model 'Book'
        db.delete_table('readernaut_book')


    models = {
        'readernaut.book': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Book'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'book_id': ('django.db.models.fields.IntegerField', [], {}),
            'cover_large': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'cover_medium': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'cover_small': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'permalink': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['readernaut']
