# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'GoogleCodeSvnChange'
        db.create_table('googlecode_googlecodesvnchange', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('subtitle', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rev', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('googlecode', ['GoogleCodeSvnChange'])

        # Adding model 'GoogleCodeProjectDownload'
        db.create_table('googlecode_googlecodeprojectdownload', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('subtitle', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('googlecode', ['GoogleCodeProjectDownload'])


    def backwards(self, orm):
        
        # Deleting model 'GoogleCodeSvnChange'
        db.delete_table('googlecode_googlecodesvnchange')

        # Deleting model 'GoogleCodeProjectDownload'
        db.delete_table('googlecode_googlecodeprojectdownload')


    models = {
        'googlecode.googlecodeprojectdownload': {
            'Meta': {'object_name': 'GoogleCodeProjectDownload'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subtitle': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'googlecode.googlecodesvnchange': {
            'Meta': {'object_name': 'GoogleCodeSvnChange'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rev': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'subtitle': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['googlecode']
