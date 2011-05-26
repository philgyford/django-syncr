# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Video'
        db.create_table('youtube_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('video_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('published', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['youtube.YoutubeUser'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('tag_list', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('view_count', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('thumbnail_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('length', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('youtube', ['Video'])

        # Adding model 'Playlist'
        db.create_table('youtube_playlist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['youtube.YoutubeUser'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('youtube', ['Playlist'])

        # Adding M2M table for field videos on 'Playlist'
        db.create_table('youtube_playlist_videos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('playlist', models.ForeignKey(orm['youtube.playlist'], null=False)),
            ('playlistvideo', models.ForeignKey(orm['youtube.playlistvideo'], null=False))
        ))
        db.create_unique('youtube_playlist_videos', ['playlist_id', 'playlistvideo_id'])

        # Adding model 'PlaylistVideo'
        db.create_table('youtube_playlistvideo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('original', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['youtube.Video'])),
        ))
        db.send_create_signal('youtube', ['PlaylistVideo'])

        # Adding model 'YoutubeUser'
        db.create_table('youtube_youtubeuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('thumbnail_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('watch_count', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='youtube_acct', unique=True, null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('youtube', ['YoutubeUser'])

        # Adding M2M table for field playlists on 'YoutubeUser'
        db.create_table('youtube_youtubeuser_playlists', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('youtubeuser', models.ForeignKey(orm['youtube.youtubeuser'], null=False)),
            ('playlist', models.ForeignKey(orm['youtube.playlist'], null=False))
        ))
        db.create_unique('youtube_youtubeuser_playlists', ['youtubeuser_id', 'playlist_id'])

        # Adding M2M table for field favorites on 'YoutubeUser'
        db.create_table('youtube_youtubeuser_favorites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('youtubeuser', models.ForeignKey(orm['youtube.youtubeuser'], null=False)),
            ('video', models.ForeignKey(orm['youtube.video'], null=False))
        ))
        db.create_unique('youtube_youtubeuser_favorites', ['youtubeuser_id', 'video_id'])

        # Adding M2M table for field uploads on 'YoutubeUser'
        db.create_table('youtube_youtubeuser_uploads', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('youtubeuser', models.ForeignKey(orm['youtube.youtubeuser'], null=False)),
            ('video', models.ForeignKey(orm['youtube.video'], null=False))
        ))
        db.create_unique('youtube_youtubeuser_uploads', ['youtubeuser_id', 'video_id'])


    def backwards(self, orm):
        
        # Deleting model 'Video'
        db.delete_table('youtube_video')

        # Deleting model 'Playlist'
        db.delete_table('youtube_playlist')

        # Removing M2M table for field videos on 'Playlist'
        db.delete_table('youtube_playlist_videos')

        # Deleting model 'PlaylistVideo'
        db.delete_table('youtube_playlistvideo')

        # Deleting model 'YoutubeUser'
        db.delete_table('youtube_youtubeuser')

        # Removing M2M table for field playlists on 'YoutubeUser'
        db.delete_table('youtube_youtubeuser_playlists')

        # Removing M2M table for field favorites on 'YoutubeUser'
        db.delete_table('youtube_youtubeuser_favorites')

        # Removing M2M table for field uploads on 'YoutubeUser'
        db.delete_table('youtube_youtubeuser_uploads')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'youtube.playlist': {
            'Meta': {'object_name': 'Playlist'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['youtube.YoutubeUser']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'feed': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['youtube.PlaylistVideo']", 'symmetrical': 'False'})
        },
        'youtube.playlistvideo': {
            'Meta': {'object_name': 'PlaylistVideo'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'feed': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['youtube.Video']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'youtube.video': {
            'Meta': {'object_name': 'Video'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['youtube.YoutubeUser']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'feed': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'published': ('django.db.models.fields.DateTimeField', [], {}),
            'tag_list': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'thumbnail_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'youtube.youtubeuser': {
            'Meta': {'object_name': 'YoutubeUser'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'favorites': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'favorited_by'", 'symmetrical': 'False', 'to': "orm['youtube.Video']"}),
            'feed': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'playlists': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['youtube.Playlist']", 'symmetrical': 'False'}),
            'thumbnail_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'uploads': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'uploaded_by'", 'symmetrical': 'False', 'to': "orm['youtube.Video']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'youtube_acct'", 'unique': 'True', 'null': 'True', 'to': "orm['auth.User']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'watch_count': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['youtube']
