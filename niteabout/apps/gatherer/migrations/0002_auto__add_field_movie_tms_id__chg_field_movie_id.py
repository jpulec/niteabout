# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Movie.tms_id'
        db.add_column(u'gatherer_movie', 'tms_id',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=14),
                      keep_default=False)


        # Changing field 'Movie.id'
        db.alter_column(u'gatherer_movie', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

    def backwards(self, orm):
        # Deleting field 'Movie.tms_id'
        db.delete_column(u'gatherer_movie', 'tms_id')


        # Changing field 'Movie.id'
        db.alter_column(u'gatherer_movie', 'id', self.gf('django.db.models.fields.IntegerField')(primary_key=True))

    models = {
        u'gatherer.barspecial': {
            'Meta': {'object_name': 'BarSpecial'},
            'bars': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gatherer.Place']", 'symmetrical': 'False'}),
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
        u'gatherer.inttag': {
            'Meta': {'unique_together': "(('key', 'value'),)", 'object_name': 'IntTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'gatherer.movie': {
            'Meta': {'object_name': 'Movie'},
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gatherer.Genre']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'runtime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'synopsis': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'tms_id': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'gatherer.moviereview': {
            'Meta': {'object_name': 'MovieReview'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gatherer.Movie']"}),
            'reviewer': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'score': ('django.db.models.fields.IntegerField', [], {})
        },
        u'gatherer.movieshowtime': {
            'Meta': {'object_name': 'MovieShowtime'},
            'dt': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gatherer.Movie']"}),
            'theater': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gatherer.Place']", 'null': 'True', 'blank': 'True'})
        },
        u'gatherer.place': {
            'Meta': {'object_name': 'Place'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'int_tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'int_tags'", 'symmetrical': 'False', 'to': u"orm['gatherer.IntTag']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'256'"}),
            'pos': ('geoposition.fields.GeopositionField', [], {'max_length': '42'}),
            'string_tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'string_tags'", 'symmetrical': 'False', 'to': u"orm['gatherer.StringTag']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'gatherer.stringtag': {
            'Meta': {'unique_together': "(('key', 'value'),)", 'object_name': 'StringTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': "'128'"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': "'256'"})
        }
    }

    complete_apps = ['gatherer']