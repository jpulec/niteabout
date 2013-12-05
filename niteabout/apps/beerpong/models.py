from django.db import models

from niteabout.apps.main.models import UserProfile
from niteabout.apps.events.models import Event

class Tournament(Event):
    teams = models.ManyToManyField('Team', related_name="teams")

class Round(models.Model):
    number = models.IntegerField()
    tournament = models.ForeignKey(Tournament)

    def __unicode__(self):
        return "Round:" + unicode(self.number) + " of Tournament:" + unicode(self.tournament)

class Team(models.Model):
    name = models.CharField(max_length=256)
    player1 = models.ForeignKey(UserProfile, related_name="beerpong_player1")
    player2 = models.ForeignKey(UserProfile, related_name="beerpong_player2")

    def __unicode__(self):
        return "Team:" + unicode(self.name) + " with players " + unicode(self.player1) + ", " + unicode(self.player2)

class Match(models.Model):
    MATCH_TYPES = (
            ('n', 'Normal'),
            ('b', 'Bye')
            )
    round = models.ForeignKey(Round)
    match_type = models.CharField(max_length=1, default='n', choices=MATCH_TYPES)
    home = models.ForeignKey(Team, related_name="home")
    away = models.ForeignKey(Team, related_name="away")
    winner = models.ForeignKey(Team, null=True, blank=True, related_name="winner")

    def __unicode__(self):
        return "Match in " + unicode(self.round) + " with teams:" + unicode(self.home) + ", " + unicode(self.away)
