# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InstitueInfo'
        db.create_table('InstituteInfo_institueinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=100)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 10, 0, 0), auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 10, 0, 0), auto_now=True, blank=True)),
            ('display_flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('establishment_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50, null=True, blank=True)),
            ('contact_numbers', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=50, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('profile', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('InstituteInfo', ['InstitueInfo'])

        # Adding model 'InstituteImages'
        db.create_table('InstituteInfo_instituteimages', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('institute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['InstituteInfo.InstitueInfo'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['master.ImageInfo'])),
        ))
        db.send_create_signal('InstituteInfo', ['InstituteImages'])

        # Adding model 'WallPost'
        db.create_table('InstituteInfo_wallpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['group_config.UserGroup'])),
            ('wall_post', self.gf('django.db.models.fields.TextField')()),
            ('date_posted', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 7, 10, 0, 0), null=True)),
        ))
        db.send_create_signal('InstituteInfo', ['WallPost'])

        # Adding model 'CsvInfo'
        db.create_table('InstituteInfo_csvinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('institute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['InstituteInfo.InstitueInfo'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['group_config.UserGroup'])),
            ('file_upload', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('InstituteInfo', ['CsvInfo'])


    def backwards(self, orm):
        # Deleting model 'InstitueInfo'
        db.delete_table('InstituteInfo_institueinfo')

        # Deleting model 'InstituteImages'
        db.delete_table('InstituteInfo_instituteimages')

        # Deleting model 'WallPost'
        db.delete_table('InstituteInfo_wallpost')

        # Deleting model 'CsvInfo'
        db.delete_table('InstituteInfo_csvinfo')


    models = {
        'InstituteInfo.csvinfo': {
            'Meta': {'object_name': 'CsvInfo'},
            'file_upload': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['group_config.UserGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['InstituteInfo.InstitueInfo']"})
        },
        'InstituteInfo.institueinfo': {
            'Meta': {'object_name': 'InstitueInfo'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'contact_numbers': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 10, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'display_flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'establishment_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['master.ImageInfo']", 'through': "orm['InstituteInfo.InstituteImages']", 'symmetrical': 'False'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 10, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'profile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'InstituteInfo.instituteimages': {
            'Meta': {'object_name': 'InstituteImages'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['master.ImageInfo']"}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['InstituteInfo.InstitueInfo']"})
        },
        'InstituteInfo.wallpost': {
            'Meta': {'object_name': 'WallPost'},
            'date_posted': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 10, 0, 0)', 'null': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['group_config.UserGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'wall_post': ('django.db.models.fields.TextField', [], {})
        },
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
        'group_config.usergroup': {
            'Meta': {'object_name': 'UserGroup'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['InstituteInfo.InstitueInfo']", 'null': 'True', 'blank': 'True'})
        },
        'master.imageinfo': {
            'Meta': {'object_name': 'ImageInfo'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['InstituteInfo']