# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'NiteEvent.place'
        db.delete_column(u'plan_niteevent', 'place_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'NiteEvent.place'
        raise RuntimeError("Cannot reverse this migration. 'NiteEvent.place' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'NiteEvent.place'
        db.add_column(u'plan_niteevent', 'place',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='place', to=orm['places.Place']),
                      keep_default=False)


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slots': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plan.NiteSlot']", 'symmetrical': 'False'})
        },
        u'plan.nitetimespan': {
            'Meta': {'object_name': 'NiteTimeSpan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timespan': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['plan']