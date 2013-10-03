# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BarSpecial.bar'
        db.delete_column(u'gatherer_barspecial', 'bar_id')

        # Adding M2M table for field bars on 'BarSpecial'
        m2m_table_name = db.shorten_name(u'gatherer_barspecial_bars')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('barspecial', models.ForeignKey(orm[u'gatherer.barspecial'], null=False)),
            ('place', models.ForeignKey(orm[u'gatherer.place'], null=False))
        ))
        db.create_unique(m2m_table_name, ['barspecial_id', 'place_id'])


    def backwards(self, orm):
        # Adding field 'BarSpecial.bar'
        db.add_column(u'gatherer_barspecial', 'bar',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['gatherer.Place']),
                      keep_default=False)

        # Removing M2M table for field bars on 'BarSpecial'
        db.delete_table(db.shorten_name(u'gatherer_barspecial_bars'))


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
        u'gatherer.movie': {
            'Meta': {'object_name': 'Movie'},
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gatherer.Genre']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'runtime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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