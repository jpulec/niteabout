# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Place.attire'
        db.add_column(u'places_place', 'attire',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['places.Attire']),
                      keep_default=False)

        # Removing M2M table for field attire on 'Place'
        db.delete_table(db.shorten_name(u'places_place_attire'))


    def backwards(self, orm):
        # Deleting field 'Place.attire'
        db.delete_column(u'places_place', 'attire_id')

        # Adding M2M table for field attire on 'Place'
        m2m_table_name = db.shorten_name(u'places_place_attire')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('place', models.ForeignKey(orm[u'places.place'], null=False)),
            ('attire', models.ForeignKey(orm[u'places.attire'], null=False))
        ))
        db.create_unique(m2m_table_name, ['place_id', 'attire_id'])


    models = {
        u'places.attire': {
            'Meta': {'object_name': 'Attire'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
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
        u'places.hours': {
            'Meta': {'object_name': 'Hours'},
            'day': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Place']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'places.osmplace': {
            'Meta': {'unique_together': "(('id', 'lat', 'lon'),)", 'object_name': 'OSMPlace'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lon': ('django.db.models.fields.FloatField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.Tag']", 'symmetrical': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'places.place': {
            'Meta': {'unique_together': "(('name', 'pos'),)", 'object_name': 'Place'},
            'attire': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Attire']"}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.PlaceCategory']", 'symmetrical': 'False'}),
            'cuisines': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.Cuisine']", 'symmetrical': 'False'}),
            'dancing': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'256'"}),
            'osm_place': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['places.OSMPlace']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'pos': ('geoposition.fields.GeopositionField', [], {'max_length': '42'}),
            'price': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
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