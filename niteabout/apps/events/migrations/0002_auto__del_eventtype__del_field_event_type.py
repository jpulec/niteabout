# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'EventType'
        db.delete_table(u'events_eventtype')

        # Deleting field 'Event.type'
        db.delete_column(u'events_event', 'type_id')

        # Removing M2M table for field attendees on 'Event'
        db.delete_table(db.shorten_name(u'events_event_attendees'))


    def backwards(self, orm):
        # Adding model 'EventType'
        db.create_table(u'events_eventtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'events', ['EventType'])


        # User chose to not deal with backwards NULL issues for 'Event.type'
        raise RuntimeError("Cannot reverse this migration. 'Event.type' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Event.type'
        db.add_column(u'events_event', 'type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.EventType']),
                      keep_default=False)

        # Adding M2M table for field attendees on 'Event'
        m2m_table_name = db.shorten_name(u'events_event_attendees')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'events.event'], null=False)),
            ('userprofile', models.ForeignKey(orm[u'main.userprofile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'userprofile_id'])


    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cost': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dt': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'events.googleplace': {
            'Meta': {'object_name': 'GooglePlace'},
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'events.orderedplace': {
            'Meta': {'object_name': 'OrderedPlace'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.GooglePlace']"})
        }
    }

    complete_apps = ['events']