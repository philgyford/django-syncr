# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Photo'
        db.create_table('picasaweb_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gphoto_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, db_index=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('taken_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('photopage_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('small_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('medium_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('thumbnail_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('content_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('enable_comments', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('geo_latitude', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('geo_longitude', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_make', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_model', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_exposure', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_iso', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_flash', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_focal_length', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('picasaweb', ['Photo'])

        # Adding model 'FavoriteList'
        db.create_table('picasaweb_favoritelist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sync_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('picasaweb', ['FavoriteList'])

        # Adding M2M table for field photos on 'FavoriteList'
        db.create_table('picasaweb_favoritelist_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('favoritelist', models.ForeignKey(orm['picasaweb.favoritelist'], null=False)),
            ('photo', models.ForeignKey(orm['picasaweb.photo'], null=False))
        ))
        db.create_unique('picasaweb_favoritelist_photos', ['favoritelist_id', 'photo_id'])

        # Adding model 'Album'
        db.create_table('picasaweb_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gphoto_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, db_index=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('albumname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('access', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('picasaweb', ['Album'])

        # Adding M2M table for field photos on 'Album'
        db.create_table('picasaweb_album_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('album', models.ForeignKey(orm['picasaweb.album'], null=False)),
            ('photo', models.ForeignKey(orm['picasaweb.photo'], null=False))
        ))
        db.create_unique('picasaweb_album_photos', ['album_id', 'photo_id'])


    def backwards(self, orm):
        
        # Deleting model 'Photo'
        db.delete_table('picasaweb_photo')

        # Deleting model 'FavoriteList'
        db.delete_table('picasaweb_favoritelist')

        # Removing M2M table for field photos on 'FavoriteList'
        db.delete_table('picasaweb_favoritelist_photos')

        # Deleting model 'Album'
        db.delete_table('picasaweb_album')

        # Removing M2M table for field photos on 'Album'
        db.delete_table('picasaweb_album_photos')


    models = {
        'picasaweb.album': {
            'Meta': {'object_name': 'Album'},
            'access': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'albumname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'gphoto_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['picasaweb.Photo']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        'picasaweb.favoritelist': {
            'Meta': {'object_name': 'FavoriteList'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['picasaweb.Photo']", 'symmetrical': 'False'}),
            'sync_date': ('django.db.models.fields.DateTimeField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        'picasaweb.photo': {
            'Meta': {'ordering': "('-taken_date',)", 'object_name': 'Photo'},
            'content_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'exif_exposure': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_flash': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_focal_length': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_iso': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_make': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'geo_latitude': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'geo_longitude': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'gphoto_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photopage_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'small_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'taken_date': ('django.db.models.fields.DateTimeField', [], {}),
            'thumbnail_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['picasaweb']
