# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Genre'
        db.create_table(u'movies_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'movies', ['Genre'])

        # Adding model 'Movie'
        db.create_table(u'movies_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tms_id', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('synopsis', self.gf('django.db.models.fields.TextField')()),
            ('runtime', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'movies', ['Movie'])

        # Adding M2M table for field genres on 'Movie'
        m2m_table_name = db.shorten_name(u'movies_movie_genres')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm[u'movies.movie'], null=False)),
            ('genre', models.ForeignKey(orm[u'movies.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['movie_id', 'genre_id'])

        # Adding model 'MovieShowtime'
        db.create_table(u'movies_movieshowtime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dt', self.gf('django.db.models.fields.DateTimeField')()),
            ('theater', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Place'], null=True, blank=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movies.Movie'])),
        ))
        db.send_create_signal(u'movies', ['MovieShowtime'])

        # Adding model 'MovieReview'
        db.create_table(u'movies_moviereview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
            ('reviewer', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movies.Movie'])),
        ))
        db.send_create_signal(u'movies', ['MovieReview'])


    def backwards(self, orm):
        # Deleting model 'Genre'
        db.delete_table(u'movies_genre')

        # Deleting model 'Movie'
        db.delete_table(u'movies_movie')

        # Removing M2M table for field genres on 'Movie'
        db.delete_table(db.shorten_name(u'movies_movie_genres'))

        # Deleting model 'MovieShowtime'
        db.delete_table(u'movies_movieshowtime')

        # Deleting model 'MovieReview'
        db.delete_table(u'movies_moviereview')


    models = {
        u'movies.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'movies.movie': {
            'Meta': {'object_name': 'Movie'},
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['movies.Genre']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'runtime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'synopsis': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'tms_id': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'movies.moviereview': {
            'Meta': {'object_name': 'MovieReview'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movies.Movie']"}),
            'reviewer': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'score': ('django.db.models.fields.IntegerField', [], {})
        },
        u'movies.movieshowtime': {
            'Meta': {'object_name': 'MovieShowtime'},
            'dt': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movies.Movie']"}),
            'theater': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Place']", 'null': 'True', 'blank': 'True'})
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
            'attire': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.PlaceCategory']", 'symmetrical': 'False'}),
            'cuisines': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['places.Cuisine']", 'null': 'True', 'blank': 'True'}),
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

    complete_apps = ['movies']