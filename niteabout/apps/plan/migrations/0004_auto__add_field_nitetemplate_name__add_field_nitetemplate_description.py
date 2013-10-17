# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NiteTemplate.name'
        db.add_column(u'plan_nitetemplate', 'name',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=128),
                      keep_default=False)

        # Adding field 'NiteTemplate.description'
        db.add_column(u'plan_nitetemplate', 'description',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NiteTemplate.name'
        db.delete_column(u'plan_nitetemplate', 'name')

        # Deleting field 'NiteTemplate.description'
        db.delete_column(u'plan_nitetemplate', 'description')


    models = {
        u'plan.niteactivity': {
            'Meta': {'object_name': 'NiteActivity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'plan.niteevent': {
            'Meta': {'object_name': 'NiteEvent'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activity'", 'to': u"orm['plan.NiteActivity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'length'", 'to': u"orm['plan.NiteTimeSpan']"})
        },
        u'plan.niteslot': {
            'Meta': {'object_name': 'NiteSlot'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event'", 'to': u"orm['plan.NiteEvent']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        u'plan.nitetemplate': {
            'Meta': {'object_name': 'NiteTemplate'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slots': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plan.NiteSlot']", 'symmetrical': 'False'})
        },
        u'plan.nitetimespan': {
            'Meta': {'object_name': 'NiteTimeSpan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timespan': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['plan']