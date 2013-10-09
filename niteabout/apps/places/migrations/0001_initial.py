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

        # Adding model 'OSMPlace'
        db.create_table(u'places_osmplace', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lon', self.gf('django.db.models.fields.FloatField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('version', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'places', ['OSMPlace'])

        # Adding unique constraint on 'OSMPlace', fields ['id', 'lat', 'lon']
        db.create_unique(u'places_osmplace', ['id', 'lat', 'lon'])

        # Adding M2M table for field tags on 'OSMPlace'
        m2m_table_name = db.shorten_name(u'places_osmplace_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('osmplace', models.ForeignKey(orm[u'places.osmplace'], null=False)),
            ('tag', models.ForeignKey(orm[u'places.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['osmplace_id', 'tag_id'])

        # Adding model 'Place'
        db.create_table(u'places_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('osm_place', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['places.OSMPlace'], unique=True, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='256')),
            ('pos', self.gf('geoposition.fields.GeopositionField')(max_length=42)),
        ))
        db.send_create_signal(u'places', ['Place'])

        # Adding unique constraint on 'Place', fields ['name', 'pos']
        db.create_unique(u'places_place', ['name', 'pos'])

        # Adding model 'Bar'
        db.create_table(u'places_bar', (
            (u'place_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['places.Place'], unique=True, primary_key=True)),
            ('price', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('volume', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('dancing', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'places', ['Bar'])

        # Adding model 'Cuisine'
        db.create_table(u'places_cuisine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'places', ['Cuisine'])

        # Adding model 'Restaurant'
        db.create_table(u'places_restaurant', (
            (u'place_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['places.Place'], unique=True, primary_key=True)),
            ('price', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('volume', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'places', ['Restaurant'])

        # Adding M2M table for field cuisines on 'Restaurant'
        m2m_table_name = db.shorten_name(u'places_restaurant_cuisines')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('restaurant', models.ForeignKey(orm[u'places.restaurant'], null=False)),
            ('cuisine', models.ForeignKey(orm[u'places.cuisine'], null=False))
        ))
        db.create_unique(m2m_table_name, ['restaurant_id', 'cuisine_id'])

        # Adding model 'BarAndRestaurant'
        db.create_table(u'places_barandrestaurant', (
            (u'restaurant_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['places.Restaurant'], unique=True)),
            (u'bar_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['places.Bar'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'places', ['BarAndRestaurant'])

        # Adding model 'Theater'
        db.create_table(u'places_theater', (
            (u'place_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['places.Place'], unique=True, primary_key=True)),
            ('price', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'places', ['Theater'])

        # Adding model 'BarSpecial'
        db.create_table(u'places_barspecial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bars', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Bar'])),
            ('start_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('day', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('deal', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'places', ['BarSpecial'])


    def backwards(self, orm):
        # Removing unique constraint on 'Place', fields ['name', 'pos']
        db.delete_unique(u'places_place', ['name', 'pos'])

        # Removing unique constraint on 'OSMPlace', fields ['id', 'lat', 'lon']
        db.delete_unique(u'places_osmplace', ['id', 'lat', 'lon'])

        # Removing unique constraint on 'Tag', fields ['key', 'value']
        db.delete_unique(u'places_tag', ['key', 'value'])

        # Deleting model 'Tag'
        db.delete_table(u'places_tag')

        # Deleting model 'OSMPlace'
        db.delete_table(u'places_osmplace')

        # Removing M2M table for field tags on 'OSMPlace'
        db.delete_table(db.shorten_name(u'places_osmplace_tags'))

        # Deleting model 'Place'
        db.delete_table(u'places_place')

        # Deleting model 'Bar'
        db.delete_table(u'places_bar')

        # Deleting model 'Cuisine'
        db.delete_table(u'places_cuisine')

        # Deleting model 'Restaurant'
        db.delete_table(u'places_restaurant')

        # Removing M2M table for field cuisines on 'Restaurant'
        db.delete_table(db.shorten_name(u'places_restaurant_cuisines'))

        # Deleting model 'BarAndRestaurant'
        db.delete_table(u'places_barandrestaurant')

        # Deleting model 'Theater'
        db.delete_table(u'places_theater')

        # Deleting model 'BarSpecial'
        db.delete_table(u'places_barspecial')


    models = {
        u'places.bar': {
            'Meta': {'object_name': 'Bar', '_ormbases': [u'places.Place']},
            'dancing': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'place_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['places.Place']", 'unique': 'True', 'primary_key': 'True'}),
            'price': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'places.barandrestaurant': {
            'Meta': {'object_name': 'BarAndRestaurant', '_ormbases': [u'places.Bar', u'places.Restaurant']},
            u'bar_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['places.Bar']", 'unique': 'True', 'primary_key': 'True'}),
            u'restaurant_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['places.Restaurant']", 'unique': 'True'})
        },
        u'places.barspecial': {
            'Meta': {'object_name': 'BarSpecial'},
            'bars': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Bar']"}),
            'day': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'deal': ('django.db.models.fields.TextField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'places.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'256'"}),
            'osm_place': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['places.OSMPlace']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'pos': ('geoposition.fields.GeopositionField', [], {'max_length': '42'})
        },
        u'places.restaurant': {
            'Meta': {'object_name': 'Restaurant', '_ormbases': [u'places.Place']},
            'cuisines': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.Cuisine']", 'symmetrical': 'False'}),
            u'place_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['places.Place']", 'unique': 'True', 'primary_key': 'True'}),
            'price': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'places.tag': {
            'Meta': {'unique_together': "(('key', 'value'),)", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': "'128'"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': "'256'"})
        },
        u'places.theater': {
            'Meta': {'object_name': 'Theater', '_ormbases': [u'places.Place']},
            u'place_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['places.Place']", 'unique': 'True', 'primary_key': 'True'}),
            'price': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['places']