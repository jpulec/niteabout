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

        # Adding model 'FeatureName'
        db.create_table(u'places_featurename', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'places', ['FeatureName'])

        # Adding M2M table for field categories on 'FeatureName'
        m2m_table_name = db.shorten_name(u'places_featurename_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('featurename', models.ForeignKey(orm[u'places.featurename'], null=False)),
            ('placecategory', models.ForeignKey(orm[u'places.placecategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['featurename_id', 'placecategory_id'])

        # Adding model 'FeatureLabel'
        db.create_table(u'places_featurelabel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feature_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.FeatureName'])),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'places', ['FeatureLabel'])

        # Adding model 'Feature'
        db.create_table(u'places_feature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feature_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.FeatureName'])),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Place'])),
            ('rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'places', ['Feature'])

        # Adding unique constraint on 'Feature', fields ['feature_name', 'place']
        db.create_unique(u'places_feature', ['feature_name_id', 'place_id'])

        # Adding model 'Place'
        db.create_table(u'places_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('osm_id', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('version', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal(u'places', ['Place'])

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

        # Adding model 'HourSpan'
        db.create_table(u'places_hourspan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('open', self.gf('django.db.models.fields.TimeField')()),
            ('close', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'places', ['HourSpan'])

        # Adding model 'Hours'
        db.create_table(u'places_hours', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Place'])),
            ('sunday', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='sunday_hours', null=True, to=orm['places.HourSpan'])),
            ('monday', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='monday_hours', null=True, to=orm['places.HourSpan'])),
            ('tuesday', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='tuesday_hours', null=True, to=orm['places.HourSpan'])),
            ('wednessday', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='wednesday_hours', null=True, to=orm['places.HourSpan'])),
            ('thursday', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='thursday_hours', null=True, to=orm['places.HourSpan'])),
            ('friday', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='friday_hours', null=True, to=orm['places.HourSpan'])),
            ('saturday', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='saturday_hours', null=True, to=orm['places.HourSpan'])),
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
        # Removing unique constraint on 'Feature', fields ['feature_name', 'place']
        db.delete_unique(u'places_feature', ['feature_name_id', 'place_id'])

        # Removing unique constraint on 'Tag', fields ['key', 'value']
        db.delete_unique(u'places_tag', ['key', 'value'])

        # Deleting model 'Tag'
        db.delete_table(u'places_tag')

        # Deleting model 'Cuisine'
        db.delete_table(u'places_cuisine')

        # Deleting model 'PlaceCategory'
        db.delete_table(u'places_placecategory')

        # Deleting model 'FeatureName'
        db.delete_table(u'places_featurename')

        # Removing M2M table for field categories on 'FeatureName'
        db.delete_table(db.shorten_name(u'places_featurename_categories'))

        # Deleting model 'FeatureLabel'
        db.delete_table(u'places_featurelabel')

        # Deleting model 'Feature'
        db.delete_table(u'places_feature')

        # Deleting model 'Place'
        db.delete_table(u'places_place')

        # Removing M2M table for field tags on 'Place'
        db.delete_table(db.shorten_name(u'places_place_tags'))

        # Removing M2M table for field categories on 'Place'
        db.delete_table(db.shorten_name(u'places_place_categories'))

        # Removing M2M table for field cuisines on 'Place'
        db.delete_table(db.shorten_name(u'places_place_cuisines'))

        # Deleting model 'HourSpan'
        db.delete_table(u'places_hourspan')

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
        u'places.feature': {
            'Meta': {'unique_together': "(('feature_name', 'place'),)", 'object_name': 'Feature'},
            'feature_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.FeatureName']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Place']"}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'})
        },
        u'places.featurelabel': {
            'Meta': {'object_name': 'FeatureLabel'},
            'feature_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.FeatureName']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'places.featurename': {
            'Meta': {'object_name': 'FeatureName'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.PlaceCategory']", 'symmetrical': 'False'}),
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
        }
    }

    complete_apps = ['places']