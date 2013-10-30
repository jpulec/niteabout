# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'NiteEventOrdered.acivity'
        db.delete_column(u'plan_niteeventordered', 'acivity_id')

        # Adding field 'NiteEventOrdered.activity'
        db.add_column(u'plan_niteeventordered', 'activity',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['plan.NiteActivity']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'NiteEventOrdered.acivity'
        raise RuntimeError("Cannot reverse this migration. 'NiteEventOrdered.acivity' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'NiteEventOrdered.acivity'
        db.add_column(u'plan_niteeventordered', 'acivity',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plan.NiteActivity']),
                      keep_default=False)

        # Deleting field 'NiteEventOrdered.activity'
        db.delete_column(u'plan_niteeventordered', 'activity_id')


    models = {
        u'places.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'places.featurename': {
            'Meta': {'object_name': 'FeatureName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
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
        u'plan.niteactivity': {
            'Meta': {'object_name': 'NiteActivity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'plan.niteevent': {
            'Meta': {'object_name': 'NiteEvent'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plan.NiteActivity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Place']"})
        },
        u'plan.niteeventordered': {
            'Meta': {'object_name': 'NiteEventOrdered'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plan.NiteActivity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Place']"})
        },
        u'plan.nitefeature': {
            'Meta': {'object_name': 'NiteFeature'},
            'feature_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.FeatureName']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '2', 'decimal_places': '1'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plan.NiteTemplate']"})
        },
        u'plan.niteplan': {
            'Meta': {'object_name': 'NitePlan'},
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plan.NiteEventOrdered']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'plan.nitetemplate': {
            'Meta': {'object_name': 'NiteTemplate'},
            'activities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plan.NiteActivity']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'what': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plan.NiteWhat']", 'symmetrical': 'False'}),
            'who': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plan.NiteWho']", 'symmetrical': 'False'})
        },
        u'plan.nitewhat': {
            'Meta': {'object_name': 'NiteWhat'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'what': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'plan.nitewho': {
            'Meta': {'object_name': 'NiteWho'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'who': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['plan']