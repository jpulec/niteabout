# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Vote', fields ['user', 'feature']
        db.delete_unique(u'places_vote', ['user_id', 'feature_id'])

        # Deleting model 'Vote'
        db.delete_table(u'places_vote')

        # Deleting field 'Feature.score'
        db.delete_column(u'places_feature', 'score')

        # Adding field 'Feature.rating_votes'
        db.add_column(u'places_feature', 'rating_votes',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Feature.rating_score'
        db.add_column(u'places_feature', 'rating_score',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Vote'
        db.create_table(u'places_vote', (
            ('score', self.gf('django.db.models.fields.IntegerField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Feature'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'places', ['Vote'])

        # Adding unique constraint on 'Vote', fields ['user', 'feature']
        db.create_unique(u'places_vote', ['user_id', 'feature_id'])

        # Adding field 'Feature.score'
        db.add_column(u'places_feature', 'score',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=2, decimal_places=1),
                      keep_default=False)

        # Deleting field 'Feature.rating_votes'
        db.delete_column(u'places_feature', 'rating_votes')

        # Deleting field 'Feature.rating_score'
        db.delete_column(u'places_feature', 'rating_score')


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
        }
    }

    complete_apps = ['places']