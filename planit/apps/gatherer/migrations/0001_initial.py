# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PlaceType'
        db.create_table(u'gatherer_placetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='128')),
        ))
        db.send_create_signal(u'gatherer', ['PlaceType'])

        # Adding model 'Place'
        db.create_table(u'gatherer_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('pos', self.gf('geoposition.fields.GeopositionField')(max_length=42)),
        ))
        db.send_create_signal(u'gatherer', ['Place'])

        # Adding M2M table for field types on 'Place'
        m2m_table_name = db.shorten_name(u'gatherer_place_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('place', models.ForeignKey(orm[u'gatherer.place'], null=False)),
            ('placetype', models.ForeignKey(orm[u'gatherer.placetype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['place_id', 'placetype_id'])

        # Adding model 'GooglePlace'
        db.create_table(u'gatherer_googleplace', (
            ('g_id', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('g_rating', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1)),
            ('g_price', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('place', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['gatherer.Place'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'gatherer', ['GooglePlace'])


    def backwards(self, orm):
        # Deleting model 'PlaceType'
        db.delete_table(u'gatherer_placetype')

        # Deleting model 'Place'
        db.delete_table(u'gatherer_place')

        # Removing M2M table for field types on 'Place'
        db.delete_table(db.shorten_name(u'gatherer_place_types'))

        # Deleting model 'GooglePlace'
        db.delete_table(u'gatherer_googleplace')


    models = {
        u'gatherer.googleplace': {
            'Meta': {'object_name': 'GooglePlace'},
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'g_price': ('django.db.models.fields.SmallIntegerField', [], {}),
            'g_rating': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '1'}),
            'place': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['gatherer.Place']", 'unique': 'True', 'primary_key': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'gatherer.place': {
            'Meta': {'object_name': 'Place'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'pos': ('geoposition.fields.GeopositionField', [], {'max_length': '42'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gatherer.PlaceType']", 'symmetrical': 'False'})
        },
        u'gatherer.placetype': {
            'Meta': {'object_name': 'PlaceType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'128'"})
        }
    }

    complete_apps = ['gatherer']