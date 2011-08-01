# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Photo.taken_granularity'
        db.add_column('flickr_photo', 'taken_granularity', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Photo.taken_granularity'
        db.delete_column('flickr_photo', 'taken_granularity')


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
            'exif_aperture': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'exif_color_space': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'exif_exposure': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'exif_flash': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'exif_focal_length': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'exif_iso': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'exif_make': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'exif_metering_mode': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'exif_model': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'exif_orientation': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'exif_software': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
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
            'taken_date': ('django.db.models.fields.DateTimeField', [], {}),
            'taken_granularity': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
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
        },
        'flickr.taggedphoto': {
            'Meta': {'object_name': 'TaggedPhoto'},
            'author_nsid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'content_object': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flickr_taggedphoto_items'", 'to': "orm['flickr.Photo']"}),
            'flickr_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machine_tag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flickr_taggedphoto_items'", 'to': "orm['taggit.Tag']"})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        }
    }

    complete_apps = ['flickr']
