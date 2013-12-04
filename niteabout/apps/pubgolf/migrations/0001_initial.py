# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table(u'pubgolf_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('player1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pubgolf_player1', to=orm['main.UserProfile'])),
            ('player2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pubgolf_player2', to=orm['main.UserProfile'])),
        ))
        db.send_create_signal(u'pubgolf', ['Team'])

        # Adding model 'Score'
        db.create_table(u'pubgolf_score', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pubgolf.Team'])),
            ('hole', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pubgolf.Hole'])),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'pubgolf', ['Score'])

        # Adding model 'Hole'
        db.create_table(u'pubgolf_hole', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.GooglePlace'])),
            ('par', self.gf('django.db.models.fields.IntegerField')()),
            ('drink', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'pubgolf', ['Hole'])

        # Adding model 'Course'
        db.create_table(u'pubgolf_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'pubgolf', ['Course'])

        # Adding M2M table for field holes on 'Course'
        m2m_table_name = db.shorten_name(u'pubgolf_course_holes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm[u'pubgolf.course'], null=False)),
            ('hole', models.ForeignKey(orm[u'pubgolf.hole'], null=False))
        ))
        db.create_unique(m2m_table_name, ['course_id', 'hole_id'])

        # Adding model 'Tournament'
        db.create_table(u'pubgolf_tournament', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pubgolf.Course'])),
        ))
        db.send_create_signal(u'pubgolf', ['Tournament'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table(u'pubgolf_team')

        # Deleting model 'Score'
        db.delete_table(u'pubgolf_score')

        # Deleting model 'Hole'
        db.delete_table(u'pubgolf_hole')

        # Deleting model 'Course'
        db.delete_table(u'pubgolf_course')

        # Removing M2M table for field holes on 'Course'
        db.delete_table(db.shorten_name(u'pubgolf_course_holes'))

        # Deleting model 'Tournament'
        db.delete_table(u'pubgolf_tournament')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.googleplace': {
            'Meta': {'object_name': 'GooglePlace'},
            'g_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'auth': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pubgolf.course': {
            'Meta': {'object_name': 'Course'},
            'holes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pubgolf.Hole']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pubgolf.hole': {
            'Meta': {'object_name': 'Hole'},
            'drink': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.GooglePlace']"}),
            'par': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pubgolf.score': {
            'Meta': {'object_name': 'Score'},
            'hole': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pubgolf.Hole']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pubgolf.Team']"})
        },
        u'pubgolf.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'player1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pubgolf_player1'", 'to': u"orm['main.UserProfile']"}),
            'player2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pubgolf_player2'", 'to': u"orm['main.UserProfile']"})
        },
        u'pubgolf.tournament': {
            'Meta': {'object_name': 'Tournament'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pubgolf.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['pubgolf']