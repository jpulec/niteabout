# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NitePlaceEvent'
        db.create_table(u'plan_niteplaceevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plan.NiteActivity'])),
            ('length', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plan.NiteTimeSpan'])),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(related_name='place', to=orm['places.Place'])),
        ))
        db.send_create_signal(u'plan', ['NitePlaceEvent'])


    def backwards(self, orm):
        # Deleting model 'NitePlaceEvent'
        db.delete_table(u'plan_niteplaceevent')


    models = {
        u'places.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'places.place': {
            'Meta': {'object_name': 'Place'},
            'attire': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.PlaceCategory']", 'symmetrical': 'False'}),
            'cuisines': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['places.Cuisine']", 'null': 'True', 'blank': 'True'}),
            'dancing': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
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
        },
        u'plan.niteactivity': {
            'Meta': {'object_name': 'NiteActivity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'plan.niteevent': {
            'Meta': {'object_name': 'NiteEvent'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activity'", 'to': u"orm['plan.NiteActivity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'length'", 'to': u"orm['plan.NiteTimeSpan']"})
        },
        u'plan.niteplaceevent': {
            'Meta': {'object_name': 'NitePlaceEvent'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plan.NiteActivity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plan.NiteTimeSpan']"}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'place'", 'to': u"orm['places.Place']"})
        },
        u'plan.niteslot': {
            'Meta': {'object_name': 'NiteSlot'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event'", 'to': u"orm['plan.NiteEvent']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        u'plan.nitetemplate': {
            'Meta': {'object_name': 'NiteTemplate'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slots': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plan.NiteSlot']", 'symmetrical': 'False'})
        },
        u'plan.nitetimespan': {
            'Meta': {'object_name': 'NiteTimeSpan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timespan': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['plan']