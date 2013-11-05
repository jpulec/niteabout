# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NiteActivityName'
        db.create_table(u'plan_niteactivityname', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'plan', ['NiteActivityName'])

        # Adding M2M table for field categories on 'NiteActivityName'
        m2m_table_name = db.shorten_name(u'plan_niteactivityname_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('niteactivityname', models.ForeignKey(orm[u'plan.niteactivityname'], null=False)),
            ('placecategory', models.ForeignKey(orm[u'places.placecategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['niteactivityname_id', 'placecategory_id'])

        # Adding model 'NiteActivity'
        db.create_table(u'plan_niteactivity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plan.NiteActivityName'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'plan', ['NiteActivity'])

        # Adding model 'NiteEvent'
        db.create_table(u'plan_niteevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plan.NiteActivity'])),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Place'])),
        ))
        db.send_create_signal(u'plan', ['NiteEvent'])

        # Adding model 'NiteWho'
        db.create_table(u'plan_nitewho', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('who', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'plan', ['NiteWho'])

        # Adding model 'NiteWhat'
        db.create_table(u'plan_nitewhat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('what', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'plan', ['NiteWhat'])

        # Adding model 'NiteTemplate'
        db.create_table(u'plan_nitetemplate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'plan', ['NiteTemplate'])

        # Adding M2M table for field activities on 'NiteTemplate'
        m2m_table_name = db.shorten_name(u'plan_nitetemplate_activities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nitetemplate', models.ForeignKey(orm[u'plan.nitetemplate'], null=False)),
            ('niteactivity', models.ForeignKey(orm[u'plan.niteactivity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['nitetemplate_id', 'niteactivity_id'])

        # Adding M2M table for field who on 'NiteTemplate'
        m2m_table_name = db.shorten_name(u'plan_nitetemplate_who')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nitetemplate', models.ForeignKey(orm[u'plan.nitetemplate'], null=False)),
            ('nitewho', models.ForeignKey(orm[u'plan.nitewho'], null=False))
        ))
        db.create_unique(m2m_table_name, ['nitetemplate_id', 'nitewho_id'])

        # Adding M2M table for field what on 'NiteTemplate'
        m2m_table_name = db.shorten_name(u'plan_nitetemplate_what')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nitetemplate', models.ForeignKey(orm[u'plan.nitetemplate'], null=False)),
            ('nitewhat', models.ForeignKey(orm[u'plan.nitewhat'], null=False))
        ))
        db.create_unique(m2m_table_name, ['nitetemplate_id', 'nitewhat_id'])

        # Adding model 'NiteFeature'
        db.create_table(u'plan_nitefeature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feature_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.FeatureName'])),
            ('score', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=2, decimal_places=1)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plan.NiteTemplate'])),
        ))
        db.send_create_signal(u'plan', ['NiteFeature'])

        # Adding model 'NitePlan'
        db.create_table(u'plan_niteplan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dt', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'plan', ['NitePlan'])

        # Adding M2M table for field events on 'NitePlan'
        m2m_table_name = db.shorten_name(u'plan_niteplan_events')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('niteplan', models.ForeignKey(orm[u'plan.niteplan'], null=False)),
            ('niteevent', models.ForeignKey(orm[u'plan.niteevent'], null=False))
        ))
        db.create_unique(m2m_table_name, ['niteplan_id', 'niteevent_id'])


    def backwards(self, orm):
        # Deleting model 'NiteActivityName'
        db.delete_table(u'plan_niteactivityname')

        # Removing M2M table for field categories on 'NiteActivityName'
        db.delete_table(db.shorten_name(u'plan_niteactivityname_categories'))

        # Deleting model 'NiteActivity'
        db.delete_table(u'plan_niteactivity')

        # Deleting model 'NiteEvent'
        db.delete_table(u'plan_niteevent')

        # Deleting model 'NiteWho'
        db.delete_table(u'plan_nitewho')

        # Deleting model 'NiteWhat'
        db.delete_table(u'plan_nitewhat')

        # Deleting model 'NiteTemplate'
        db.delete_table(u'plan_nitetemplate')

        # Removing M2M table for field activities on 'NiteTemplate'
        db.delete_table(db.shorten_name(u'plan_nitetemplate_activities'))

        # Removing M2M table for field who on 'NiteTemplate'
        db.delete_table(db.shorten_name(u'plan_nitetemplate_who'))

        # Removing M2M table for field what on 'NiteTemplate'
        db.delete_table(db.shorten_name(u'plan_nitetemplate_what'))

        # Deleting model 'NiteFeature'
        db.delete_table(u'plan_nitefeature')

        # Deleting model 'NitePlan'
        db.delete_table(u'plan_niteplan')

        # Removing M2M table for field events on 'NitePlan'
        db.delete_table(db.shorten_name(u'plan_niteplan_events'))


    models = {
        u'places.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'places.featurename': {
            'Meta': {'object_name': 'FeatureName'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.PlaceCategory']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'places.place': {
            'Meta': {'object_name': 'Place'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.PlaceCategory']", 'symmetrical': 'False'}),
            'cuisines': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['places.Cuisine']", 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'osm_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['places.Tag']", 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
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
        },
        u'plan.niteactivity': {
            'Meta': {'ordering': "('order',)", 'object_name': 'NiteActivity'},
            'activity_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plan.NiteActivityName']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'plan.niteactivityname': {
            'Meta': {'object_name': 'NiteActivityName'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['places.PlaceCategory']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'plan.niteevent': {
            'Meta': {'object_name': 'NiteEvent'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plan.NiteActivity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Place']"})
        },
        u'plan.nitefeature': {
            'Meta': {'object_name': 'NiteFeature'},
            'feature_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.FeatureName']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '2', 'decimal_places': '1'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plan.NiteTemplate']"})
        },
        u'plan.niteplan': {
            'Meta': {'object_name': 'NitePlan'},
            'dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plan.NiteEvent']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'plan.nitetemplate': {
            'Meta': {'object_name': 'NiteTemplate'},
            'activities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plan.NiteActivity']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'what': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plan.NiteWhat']", 'symmetrical': 'False'}),
            'who': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plan.NiteWho']", 'symmetrical': 'False'})
        },
        u'plan.nitewhat': {
            'Meta': {'object_name': 'NiteWhat'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'what': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'plan.nitewho': {
            'Meta': {'object_name': 'NiteWho'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'who': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['plan']