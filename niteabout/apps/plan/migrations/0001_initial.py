# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NiteActivity'
        db.create_table(u'plan_niteactivity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'plan', ['NiteActivity'])

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
        ))
        db.send_create_signal(u'plan', ['NitePlan'])


    def backwards(self, orm):
        # Deleting model 'NiteActivity'
        db.delete_table(u'plan_niteactivity')

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


    models = {
        u'places.featurename': {
            'Meta': {'object_name': 'FeatureName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'plan.niteactivity': {
            'Meta': {'object_name': 'NiteActivity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
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