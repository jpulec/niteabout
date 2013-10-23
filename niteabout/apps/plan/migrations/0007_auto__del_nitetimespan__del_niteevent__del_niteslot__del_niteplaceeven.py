# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'NiteTimeSpan'
        db.delete_table(u'plan_nitetimespan')

        # Deleting model 'NiteEvent'
        db.delete_table(u'plan_niteevent')

        # Deleting model 'NiteSlot'
        db.delete_table(u'plan_niteslot')

        # Deleting model 'NitePlaceEvent'
        db.delete_table(u'plan_niteplaceevent')

        # Removing M2M table for field slots on 'NiteTemplate'
        db.delete_table(db.shorten_name(u'plan_nitetemplate_slots'))

        # Adding M2M table for field activities on 'NiteTemplate'
        m2m_table_name = db.shorten_name(u'plan_nitetemplate_activities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nitetemplate', models.ForeignKey(orm[u'plan.nitetemplate'], null=False)),
            ('niteactivity', models.ForeignKey(orm[u'plan.niteactivity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['nitetemplate_id', 'niteactivity_id'])


    def backwards(self, orm):
        # Adding model 'NiteTimeSpan'
        db.create_table(u'plan_nitetimespan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timespan', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'plan', ['NiteTimeSpan'])

        # Adding model 'NiteEvent'
        db.create_table(u'plan_niteevent', (
            ('length', self.gf('django.db.models.fields.related.ForeignKey')(related_name='length', to=orm['plan.NiteTimeSpan'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='activity', to=orm['plan.NiteActivity'])),
        ))
        db.send_create_signal(u'plan', ['NiteEvent'])

        # Adding model 'NiteSlot'
        db.create_table(u'plan_niteslot', (
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='event', to=orm['plan.NiteEvent'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'plan', ['NiteSlot'])

        # Adding model 'NitePlaceEvent'
        db.create_table(u'plan_niteplaceevent', (
            ('length', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plan.NiteTimeSpan'])),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(related_name='place', to=orm['places.Place'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plan.NiteActivity'])),
        ))
        db.send_create_signal(u'plan', ['NitePlaceEvent'])

        # Adding M2M table for field slots on 'NiteTemplate'
        m2m_table_name = db.shorten_name(u'plan_nitetemplate_slots')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nitetemplate', models.ForeignKey(orm[u'plan.nitetemplate'], null=False)),
            ('niteslot', models.ForeignKey(orm[u'plan.niteslot'], null=False))
        ))
        db.create_unique(m2m_table_name, ['nitetemplate_id', 'niteslot_id'])

        # Removing M2M table for field activities on 'NiteTemplate'
        db.delete_table(db.shorten_name(u'plan_nitetemplate_activities'))


    models = {
        u'plan.niteactivity': {
            'Meta': {'object_name': 'NiteActivity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'plan.niteplan': {
            'Meta': {'object_name': 'NitePlan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'plan.nitetemplate': {
            'Meta': {'object_name': 'NiteTemplate'},
            'activities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plan.NiteActivity']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['plan']