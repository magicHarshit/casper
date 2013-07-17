# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StudentInfo'
        db.create_table('studentinfo_studentinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('institute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['InstituteInfo.InstitueInfo'])),
            ('status', self.gf('django.db.models.fields.CharField')(default='Pending', max_length=100)),
            ('profile', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique_number', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('studentinfo', ['StudentInfo'])

        # Adding model 'StudentGroup'
        db.create_table('studentinfo_studentgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentinfo.StudentInfo'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['group_config.UserGroup'])),
        ))
        db.send_create_signal('studentinfo', ['StudentGroup'])


    def backwards(self, orm):
        # Deleting model 'StudentInfo'
        db.delete_table('studentinfo_studentinfo')

        # Deleting model 'StudentGroup'
        db.delete_table('studentinfo_studentgroup')


    models = {
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
        },
        'studentinfo.studentgroup': {
            'Meta': {'object_name': 'StudentGroup'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['group_config.UserGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['studentinfo.StudentInfo']"})
        },
        'studentinfo.studentinfo': {
            'Meta': {'object_name': 'StudentInfo'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['group_config.UserGroup']", 'through': "orm['studentinfo.StudentGroup']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['InstituteInfo.InstitueInfo']"}),
            'profile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Pending'", 'max_length': '100'}),
            'unique_number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['studentinfo']