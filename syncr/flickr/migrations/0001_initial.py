# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Photo'
        db.create_table('flickr_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flickr_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('owner_nsid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('taken_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('upload_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('photopage_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('farm', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('server', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('original_secret', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('thumbnail_width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('thumbnail_height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('small_width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('small_height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('medium_width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('medium_height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('large_width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('large_height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('original_width', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('original_height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('enable_comments', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('license', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geo_latitude', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('geo_longitude', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('geo_accuracy', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('geo_locality', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('geo_county', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('geo_region', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('geo_country', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('exif_make', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_model', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_orientation', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_exposure', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_software', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_aperture', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_iso', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_metering_mode', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_flash', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_focal_length', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('exif_color_space', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('flickr', ['Photo'])

        # Adding model 'FavoriteList'
        db.create_table('flickr_favoritelist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sync_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('primary', self.gf('django.db.models.fields.related.ForeignKey')(related_name='primary_in', null=True, to=orm['flickr.Photo'])),
        ))
        db.send_create_signal('flickr', ['FavoriteList'])

        # Adding M2M table for field photos on 'FavoriteList'
        db.create_table('flickr_favoritelist_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('favoritelist', models.ForeignKey(orm['flickr.favoritelist'], null=False)),
            ('photo', models.ForeignKey(orm['flickr.photo'], null=False))
        ))
        db.create_unique('flickr_favoritelist_photos', ['favoritelist_id', 'photo_id'])

        # Adding model 'PhotoSet'
        db.create_table('flickr_photoset', (
            ('flickr_id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('primary', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='primary_photo_set', null=True, to=orm['flickr.Photo'])),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('flickr', ['PhotoSet'])

        # Adding M2M table for field photos on 'PhotoSet'
        db.create_table('flickr_photoset_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photoset', models.ForeignKey(orm['flickr.photoset'], null=False)),
            ('photo', models.ForeignKey(orm['flickr.photo'], null=False))
        ))
        db.create_unique('flickr_photoset_photos', ['photoset_id', 'photo_id'])

        # Adding model 'PhotoComment'
        db.create_table('flickr_photocomment', (
            ('flickr_id', self.gf('django.db.models.fields.CharField')(max_length=128, primary_key=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flickr.Photo'])),
            ('author_nsid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('permanent_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('flickr', ['PhotoComment'])


    def backwards(self, orm):
        
        # Deleting model 'Photo'
        db.delete_table('flickr_photo')

        # Deleting model 'FavoriteList'
        db.delete_table('flickr_favoritelist')

        # Removing M2M table for field photos on 'FavoriteList'
        db.delete_table('flickr_favoritelist_photos')

        # Deleting model 'PhotoSet'
        db.delete_table('flickr_photoset')

        # Removing M2M table for field photos on 'PhotoSet'
        db.delete_table('flickr_photoset_photos')

        # Deleting model 'PhotoComment'
        db.delete_table('flickr_photocomment')


    models = {
        'flickr.favoritelist': {
            'Meta': {'object_name': 'FavoriteList'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['flickr.Photo']", 'symmetrical': 'False'}),
            'primary': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary_in'", 'null': 'True', 'to': "orm['flickr.Photo']"}),
            'sync_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'flickr.photo': {
            'Meta': {'ordering': "('-taken_date',)", 'object_name': 'Photo'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'exif_aperture': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_color_space': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_exposure': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_flash': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_focal_length': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_iso': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_make': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_metering_mode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_orientation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'exif_software': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'farm': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'flickr_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
            'geo_accuracy': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'geo_country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'geo_county': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'geo_latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'geo_locality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'geo_longitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'geo_region': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'large_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'medium_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'medium_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'original_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'original_secret': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'original_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner_nsid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photopage_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'server': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'small_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'small_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'taken_date': ('django.db.models.fields.DateTimeField', [], {}),
            'thumbnail_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'thumbnail_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {}),
            'upload_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'flickr.photocomment': {
            'Meta': {'ordering': "('pub_date',)", 'object_name': 'PhotoComment'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'author_nsid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'flickr_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'primary_key': 'True'}),
            'permanent_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flickr.Photo']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'flickr.photoset': {
            'Meta': {'ordering': "('order',)", 'object_name': 'PhotoSet'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'flickr_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['flickr.Photo']", 'symmetrical': 'False'}),
            'primary': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'primary_photo_set'", 'null': 'True', 'to': "orm['flickr.Photo']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['flickr']
