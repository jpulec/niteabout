# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'gatherer_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length='128')),
            ('value', self.gf('django.db.models.fields.CharField')(max_length='256')),
        ))
        db.send_create_signal(u'gatherer', ['Tag'])

        # Adding model 'Place'
        db.create_table(u'gatherer_place', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='256')),
            ('pos', self.gf('geoposition.fields.GeopositionField')(max_length=42)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('version', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'gatherer', ['Place'])

        # Adding M2M table for field tags on 'Place'
        m2m_table_name = db.shorten_name(u'gatherer_place_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('place', models.ForeignKey(orm[u'gatherer.place'], null=False)),
            ('tag', models.ForeignKey(orm[u'gatherer.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['place_id', 'tag_id'])

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
            ('mpaa', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('synopsis', self.gf('django.db.models.fields.TextField')()),
            ('runtime', self.gf('django.db.models.fields.IntegerField')()),
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

        # Adding model 'MovieReview'
        db.create_table(u'gatherer_moviereview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
            ('reviewer', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gatherer.Movie'])),
        ))
        db.send_create_signal(u'gatherer', ['MovieReview'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'gatherer_tag')

        # Deleting model 'Place'
        db.delete_table(u'gatherer_place')

        # Removing M2M table for field tags on 'Place'
        db.delete_table(db.shorten_name(u'gatherer_place_tags'))

        # Deleting model 'Genre'
        db.delete_table(u'gatherer_genre')

        # Deleting model 'Movie'
        db.delete_table(u'gatherer_movie')

        # Removing M2M table for field genres on 'Movie'
        db.delete_table(db.shorten_name(u'gatherer_movie_genres'))

        # Deleting model 'MovieReview'
        db.delete_table(u'gatherer_moviereview')


    models = {
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
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': "'128'"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': "'256'"})
        }
    }

    complete_apps = ['gatherer']