# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'places_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length='128')),
            ('value', self.gf('django.db.models.fields.CharField')(max_length='256')),
        ))
        db.send_create_signal(u'places', ['Tag'])

        # Adding unique constraint on 'Tag', fields ['key', 'value']
        db.create_unique(u'places_tag', ['key', 'value'])

        # Adding model 'Cuisine'
        db.create_table(u'places_cuisine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'places', ['Cuisine'])

        # Adding model 'PlaceCategory'
        db.create_table(u'places_placecategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'places', ['PlaceCategory'])

        # Adding model 'Place'
        db.create_table(u'places_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('osm_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lon', self.gf('django.db.models.fields.FloatField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('version', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('price', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('volume', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('dancing', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('attire', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'places', ['Place'])

        # Adding unique constraint on 'Place', fields ['osm_id', 'lat', 'lon']
        db.create_unique(u'places_place', ['osm_id', 'lat', 'lon'])

        # Adding M2M table for field tags on 'Place'
        m2m_table_name = db.shorten_name(u'places_place_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('place', models.ForeignKey(orm[u'places.place'], null=False)),
            ('tag', models.ForeignKey(orm[u'places.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['place_id', 'tag_id'])

        # Adding M2M table for field categories on 'Place'
        m2m_table_name = db.shorten_name(u'places_place_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('place', models.ForeignKey(orm[u'places.place'], null=False)),
            ('placecategory', models.ForeignKey(orm[u'places.placecategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['place_id', 'placecategory_id'])

        # Adding M2M table for field cuisines on 'Place'
        m2m_table_name = db.shorten_name(u'places_place_cuisines')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('place', models.ForeignKey(orm[u'places.place'], null=False)),
            ('cuisine', models.ForeignKey(orm[u'places.cuisine'], null=False))
        ))
        db.create_unique(m2m_table_name, ['place_id', 'cuisine_id'])

        # Adding model 'Hours'
        db.create_table(u'places_hours', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Place'])),
            ('day', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'places', ['Hours'])

        # Adding model 'Deal'
        db.create_table(u'places_deal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Place'])),
            ('start_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('day', self.gf('django.db.models.fields.IntegerField')(max_length=1, null=True, blank=True)),
            ('deal', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'places', ['Deal'])


    def backwards(self, orm):
        # Removing unique constraint on 'Place', fields ['osm_id', 'lat', 'lon']
        db.delete_unique(u'places_place', ['osm_id', 'lat', 'lon'])

        # Removing unique constraint on 'Tag', fields ['key', 'value']
        db.delete_unique(u'places_tag', ['key', 'value'])

        # Deleting model 'Tag'
        db.delete_table(u'places_tag')

        # Deleting model 'Cuisine'
        db.delete_table(u'places_cuisine')

        # Deleting model 'PlaceCategory'
        db.delete_table(u'places_placecategory')

        # Deleting model 'Place'
        db.delete_table(u'places_place')

        # Removing M2M table for field tags on 'Place'
        db.delete_table(db.shorten_name(u'places_place_tags'))

        # Removing M2M table for field categories on 'Place'
        db.delete_table(db.shorten_name(u'places_place_categories'))

        # Removing M2M table for field cuisines on 'Place'
        db.delete_table(db.shorten_name(u'places_place_cuisines'))

        # Deleting model 'Hours'
        db.delete_table(u'places_hours')

        # Deleting model 'Deal'
        db.delete_table(u'places_deal')


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
        u'places.hours': {
            'Meta': {'object_name': 'Hours'},
            'day': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Place']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'places.place': {
            'Meta': {'unique_together': "(('osm_id', 'lat', 'lon'),)", 'object_name': 'Place'},
            'attire': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.PlaceCategory']", 'symmetrical': 'False'}),
            'cuisines': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['places.Cuisine']", 'null': 'True', 'blank': 'True'}),
            'dancing': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lon': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'osm_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'price': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.Tag']", 'symmetrical': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
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