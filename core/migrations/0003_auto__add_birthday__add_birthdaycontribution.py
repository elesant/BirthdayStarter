# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Birthday'
        db.create_table('table_birthday', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facebook_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('amount_raised', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('amount_target', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('shipping_address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('shipping_province_state', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('shipping_country', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('shipping_postal_code', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('shipping_phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Birthday'])

        # Adding model 'BirthdayContribution'
        db.create_table('table_birthday_contribution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('birthday', self.gf('django.db.models.fields.related.ForeignKey')(related_name='birthdaycontribution_birthday', to=orm['core.Birthday'])),
            ('contributor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='birthdaycontribution_contributor', to=orm['core.User'])),
            ('amount', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['BirthdayContribution'])


    def backwards(self, orm):
        # Deleting model 'Birthday'
        db.delete_table('table_birthday')

        # Deleting model 'BirthdayContribution'
        db.delete_table('table_birthday_contribution')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.birthday': {
            'Meta': {'object_name': 'Birthday', 'db_table': "'table_birthday'"},
            'amount_raised': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'amount_target': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shipping_address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'shipping_country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'shipping_phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'shipping_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'shipping_province_state': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.birthdaycontribution': {
            'Meta': {'object_name': 'BirthdayContribution', 'db_table': "'table_birthday_contribution'"},
            'amount': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'birthday': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'birthdaycontribution_birthday'", 'to': u"orm['core.Birthday']"}),
            'contributor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'birthdaycontribution_contributor'", 'to': u"orm['core.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'core.present': {
            'Meta': {'object_name': 'Present', 'db_table': "'table_present'"},
            'cost': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_link': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'item_link': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'core.user': {
            'Meta': {'object_name': 'User', 'db_table': "'table_user'"},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tz_offset': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['core']