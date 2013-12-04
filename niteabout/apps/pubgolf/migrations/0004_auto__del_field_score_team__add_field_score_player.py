# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Score.team'
        db.delete_column(u'pubgolf_score', 'team_id')

        # Adding field 'Score.player'
        db.add_column(u'pubgolf_score', 'player',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='pubgolf_score', to=orm['main.UserProfile']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Score.team'
        raise RuntimeError("Cannot reverse this migration. 'Score.team' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Score.team'
        db.add_column(u'pubgolf_score', 'team',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pubgolf.Team']),
                      keep_default=False)

        # Deleting field 'Score.player'
        db.delete_column(u'pubgolf_score', 'player_id')


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
        u'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'auth': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pubgolf.hole': {
            'Meta': {'object_name': 'Hole'},
            'drink': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.GooglePlace']"}),
            'par': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pubgolf.orderedhole': {
            'Meta': {'object_name': 'OrderedHole'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pubgolf.PubGolf']"}),
            'hole': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pubgolf.Hole']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pubgolf.pubgolf': {
            'Meta': {'object_name': 'PubGolf', '_ormbases': [u'events.Event']},
            u'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['events.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'holes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'holes'", 'symmetrical': 'False', 'through': u"orm['pubgolf.OrderedHole']", 'to': u"orm['pubgolf.Hole']"}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'teams'", 'symmetrical': 'False', 'to': u"orm['pubgolf.Team']"})
        },
        u'pubgolf.score': {
            'Meta': {'object_name': 'Score'},
            'hole': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pubgolf.Hole']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pubgolf_score'", 'to': u"orm['main.UserProfile']"}),
            'score': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pubgolf.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'player1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pubgolf_player1'", 'to': u"orm['main.UserProfile']"}),
            'player2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pubgolf_player2'", 'to': u"orm['main.UserProfile']"})
        }
    }

    complete_apps = ['pubgolf']