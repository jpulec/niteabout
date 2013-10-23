# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Feature.feature'
        db.alter_column(u'places_feature', 'feature_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.FeatureName']))

    def backwards(self, orm):

        # Changing field 'Feature.feature'
        db.alter_column(u'places_feature', 'feature_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Feature']))

    models = {
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
            'Meta': {'object_name': 'Feature'},
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.FeatureName']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'})
        },
        u'places.featurename': {
            'Meta': {'object_name': 'FeatureName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'places.hours': {
            'Meta': {'object_name': 'Hours'},
            'day': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Place']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'places.place': {
            'Meta': {'object_name': 'Place'},
            'attire': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.PlaceCategory']", 'symmetrical': 'False'}),
            'cuisines': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['places.Cuisine']", 'null': 'True', 'blank': 'True'}),
            'dancing': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'features'", 'symmetrical': 'False', 'to': u"orm['places.Feature']"}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'osm_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['places.Tag']", 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'volume': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'})
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
        }
    }

    complete_apps = ['places']