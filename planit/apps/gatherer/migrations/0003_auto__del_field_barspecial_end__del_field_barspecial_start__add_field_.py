# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BarSpecial.end'
        db.delete_column(u'gatherer_barspecial', 'end')

        # Deleting field 'BarSpecial.start'
        db.delete_column(u'gatherer_barspecial', 'start')

        # Adding field 'BarSpecial.start_time'
        db.add_column(u'gatherer_barspecial', 'start_time',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(0, 0)),
                      keep_default=False)

        # Adding field 'BarSpecial.end_time'
        db.add_column(u'gatherer_barspecial', 'end_time',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(0, 0)),
                      keep_default=False)

        # Adding field 'BarSpecial.day'
        db.add_column(u'gatherer_barspecial', 'day',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'BarSpecial.end'
        db.add_column(u'gatherer_barspecial', 'end',
                      self.gf('django.db.models.fields.DateTimeField')(default=None),
                      keep_default=False)

        # Adding field 'BarSpecial.start'
        db.add_column(u'gatherer_barspecial', 'start',
                      self.gf('django.db.models.fields.DateTimeField')(default=None),
                      keep_default=False)

        # Deleting field 'BarSpecial.start_time'
        db.delete_column(u'gatherer_barspecial', 'start_time')

        # Deleting field 'BarSpecial.end_time'
        db.delete_column(u'gatherer_barspecial', 'end_time')

        # Deleting field 'BarSpecial.day'
        db.delete_column(u'gatherer_barspecial', 'day')


    models = {
        u'gatherer.barspecial': {
            'Meta': {'object_name': 'BarSpecial'},
            'bar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gatherer.Place']"}),
            'day': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'deal': ('django.db.models.fields.TextField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'gatherer.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'gatherer.movie': {
            'Meta': {'object_name': 'Movie'},
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gatherer.Genre']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'mpaa': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'runtime': ('django.db.models.fields.IntegerField', [], {}),
            'synopsis': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'gatherer.moviereview': {
            'Meta': {'object_name': 'MovieReview'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gatherer.Movie']"}),
            'reviewer': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'score': ('django.db.models.fields.IntegerField', [], {})
        },
        u'gatherer.place': {
            'Meta': {'object_name': 'Place'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'256'"}),
            'pos': ('geoposition.fields.GeopositionField', [], {'max_length': '42'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tags'", 'symmetrical': 'False', 'to': u"orm['gatherer.Tag']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'gatherer.tag': {
            'Meta': {'unique_together': "(('key', 'value'),)", 'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': "'128'"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': "'256'"})
        }
    }

    complete_apps = ['gatherer']