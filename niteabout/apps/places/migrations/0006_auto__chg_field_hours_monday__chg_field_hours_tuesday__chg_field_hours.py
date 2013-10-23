# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Hours.monday'
        db.alter_column(u'places_hours', 'monday_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['places.HourSpan']))

        # Changing field 'Hours.tuesday'
        db.alter_column(u'places_hours', 'tuesday_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['places.HourSpan']))

        # Changing field 'Hours.friday'
        db.alter_column(u'places_hours', 'friday_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['places.HourSpan']))

        # Changing field 'Hours.thursday'
        db.alter_column(u'places_hours', 'thursday_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['places.HourSpan']))

        # Changing field 'Hours.sunday'
        db.alter_column(u'places_hours', 'sunday_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['places.HourSpan']))

        # Changing field 'Hours.wednessday'
        db.alter_column(u'places_hours', 'wednessday_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['places.HourSpan']))

        # Changing field 'Hours.saturday'
        db.alter_column(u'places_hours', 'saturday_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['places.HourSpan']))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Hours.monday'
        raise RuntimeError("Cannot reverse this migration. 'Hours.monday' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Hours.monday'
        db.alter_column(u'places_hours', 'monday_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.HourSpan']))

        # User chose to not deal with backwards NULL issues for 'Hours.tuesday'
        raise RuntimeError("Cannot reverse this migration. 'Hours.tuesday' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Hours.tuesday'
        db.alter_column(u'places_hours', 'tuesday_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.HourSpan']))

        # User chose to not deal with backwards NULL issues for 'Hours.friday'
        raise RuntimeError("Cannot reverse this migration. 'Hours.friday' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Hours.friday'
        db.alter_column(u'places_hours', 'friday_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.HourSpan']))

        # User chose to not deal with backwards NULL issues for 'Hours.thursday'
        raise RuntimeError("Cannot reverse this migration. 'Hours.thursday' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Hours.thursday'
        db.alter_column(u'places_hours', 'thursday_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.HourSpan']))

        # User chose to not deal with backwards NULL issues for 'Hours.sunday'
        raise RuntimeError("Cannot reverse this migration. 'Hours.sunday' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Hours.sunday'
        db.alter_column(u'places_hours', 'sunday_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.HourSpan']))

        # User chose to not deal with backwards NULL issues for 'Hours.wednessday'
        raise RuntimeError("Cannot reverse this migration. 'Hours.wednessday' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Hours.wednessday'
        db.alter_column(u'places_hours', 'wednessday_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.HourSpan']))

        # User chose to not deal with backwards NULL issues for 'Hours.saturday'
        raise RuntimeError("Cannot reverse this migration. 'Hours.saturday' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Hours.saturday'
        db.alter_column(u'places_hours', 'saturday_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.HourSpan']))

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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'places.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'places.deal': {
            'Meta': {'object_name': 'Deal'},
            'day': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'deal': ('django.db.models.fields.TextField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Place']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'places.feature': {
            'Meta': {'unique_together': "(('feature_name', 'place'),)", 'object_name': 'Feature'},
            'feature_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.FeatureName']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Place']"}),
            'score': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '2', 'decimal_places': '1'})
        },
        u'places.featurename': {
            'Meta': {'object_name': 'FeatureName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'places.hours': {
            'Meta': {'object_name': 'Hours'},
            'friday': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'friday_hours'", 'null': 'True', 'to': u"orm['places.HourSpan']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monday': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'monday_hours'", 'null': 'True', 'to': u"orm['places.HourSpan']"}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Place']"}),
            'saturday': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'saturday_hours'", 'null': 'True', 'to': u"orm['places.HourSpan']"}),
            'sunday': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sunday_hours'", 'null': 'True', 'to': u"orm['places.HourSpan']"}),
            'thursday': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'thursday_hours'", 'null': 'True', 'to': u"orm['places.HourSpan']"}),
            'tuesday': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tuesday_hours'", 'null': 'True', 'to': u"orm['places.HourSpan']"}),
            'wednessday': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'wednesday_hours'", 'null': 'True', 'to': u"orm['places.HourSpan']"})
        },
        u'places.hourspan': {
            'Meta': {'object_name': 'HourSpan'},
            'close': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'open': ('django.db.models.fields.TimeField', [], {})
        },
        u'places.place': {
            'Meta': {'object_name': 'Place'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.PlaceCategory']", 'symmetrical': 'False'}),
            'cuisines': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['places.Cuisine']", 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'osm_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['places.Tag']", 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'places.placecategory': {
            'Meta': {'object_name': 'PlaceCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'places.tag': {
            'Meta': {'unique_together': "(('key', 'value'),)", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': "'128'"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': "'256'"})
        },
        u'places.vote': {
            'Meta': {'unique_together': "(('user', 'feature'),)", 'object_name': 'Vote'},
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['places']