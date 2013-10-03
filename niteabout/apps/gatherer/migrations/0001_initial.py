# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StringTag'
        db.create_table(u'gatherer_stringtag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length='128')),
            ('value', self.gf('django.db.models.fields.CharField')(max_length='256')),
        ))
        db.send_create_signal(u'gatherer', ['StringTag'])

        # Adding unique constraint on 'StringTag', fields ['key', 'value']
        db.create_unique(u'gatherer_stringtag', ['key', 'value'])

        # Adding model 'IntTag'
        db.create_table(u'gatherer_inttag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'gatherer', ['IntTag'])

        # Adding unique constraint on 'IntTag', fields ['key', 'value']
        db.create_unique(u'gatherer_inttag', ['key', 'value'])

        # Adding model 'Place'
        db.create_table(u'gatherer_place', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='256')),
            ('pos', self.gf('geoposition.fields.GeopositionField')(max_length=42)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('version', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'gatherer', ['Place'])

        # Adding M2M table for field string_tags on 'Place'
        m2m_table_name = db.shorten_name(u'gatherer_place_string_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('place', models.ForeignKey(orm[u'gatherer.place'], null=False)),
            ('stringtag', models.ForeignKey(orm[u'gatherer.stringtag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['place_id', 'stringtag_id'])

        # Adding M2M table for field int_tags on 'Place'
        m2m_table_name = db.shorten_name(u'gatherer_place_int_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('place', models.ForeignKey(orm[u'gatherer.place'], null=False)),
            ('inttag', models.ForeignKey(orm[u'gatherer.inttag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['place_id', 'inttag_id'])

        # Adding model 'Genre'
        db.create_table(u'gatherer_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'gatherer', ['Genre'])

        # Adding model 'Movie'
        db.create_table(u'gatherer_movie', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('synopsis', self.gf('django.db.models.fields.TextField')()),
            ('runtime', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'gatherer', ['Movie'])

        # Adding M2M table for field genres on 'Movie'
        m2m_table_name = db.shorten_name(u'gatherer_movie_genres')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'gatherer.movie'], null=False)),
            ('genre', models.ForeignKey(orm[u'gatherer.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'genre_id'])

        # Adding model 'MovieShowtime'
        db.create_table(u'gatherer_movieshowtime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dt', self.gf('django.db.models.fields.DateTimeField')()),
            ('theater', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gatherer.Place'], null=True, blank=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gatherer.Movie'])),
        ))
        db.send_create_signal(u'gatherer', ['MovieShowtime'])

        # Adding model 'MovieReview'
        db.create_table(u'gatherer_moviereview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
            ('reviewer', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gatherer.Movie'])),
        ))
        db.send_create_signal(u'gatherer', ['MovieReview'])

        # Adding model 'BarSpecial'
        db.create_table(u'gatherer_barspecial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('day', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('deal', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'gatherer', ['BarSpecial'])

        # Adding M2M table for field bars on 'BarSpecial'
        m2m_table_name = db.shorten_name(u'gatherer_barspecial_bars')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('barspecial', models.ForeignKey(orm[u'gatherer.barspecial'], null=False)),
            ('place', models.ForeignKey(orm[u'gatherer.place'], null=False))
        ))
        db.create_unique(m2m_table_name, ['barspecial_id', 'place_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'IntTag', fields ['key', 'value']
        db.delete_unique(u'gatherer_inttag', ['key', 'value'])

        # Removing unique constraint on 'StringTag', fields ['key', 'value']
        db.delete_unique(u'gatherer_stringtag', ['key', 'value'])

        # Deleting model 'StringTag'
        db.delete_table(u'gatherer_stringtag')

        # Deleting model 'IntTag'
        db.delete_table(u'gatherer_inttag')

        # Deleting model 'Place'
        db.delete_table(u'gatherer_place')

        # Removing M2M table for field string_tags on 'Place'
        db.delete_table(db.shorten_name(u'gatherer_place_string_tags'))

        # Removing M2M table for field int_tags on 'Place'
        db.delete_table(db.shorten_name(u'gatherer_place_int_tags'))

        # Deleting model 'Genre'
        db.delete_table(u'gatherer_genre')

        # Deleting model 'Movie'
        db.delete_table(u'gatherer_movie')

        # Removing M2M table for field genres on 'Movie'
        db.delete_table(db.shorten_name(u'gatherer_movie_genres'))

        # Deleting model 'MovieShowtime'
        db.delete_table(u'gatherer_movieshowtime')

        # Deleting model 'MovieReview'
        db.delete_table(u'gatherer_moviereview')

        # Deleting model 'BarSpecial'
        db.delete_table(u'gatherer_barspecial')

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
        u'gatherer.inttag': {
            'Meta': {'unique_together': "(('key', 'value'),)", 'object_name': 'IntTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
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