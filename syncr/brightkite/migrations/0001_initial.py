# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Checkin'
        db.create_table('brightkite_checkin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('tiny_avtar', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('checkin_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('brightkite', ['Checkin'])


    def backwards(self, orm):
        
        # Deleting model 'Checkin'
        db.delete_table('brightkite_checkin')


    models = {
        'brightkite.checkin': {
            'Meta': {'ordering': "('-created_at',)", 'object_name': 'Checkin'},
            'checkin_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'place_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tiny_avtar': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['brightkite']
