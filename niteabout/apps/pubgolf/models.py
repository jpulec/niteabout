from django.db import models

from niteabout.apps.main.models import UserProfile
from niteabout.apps.events.models import Event, GooglePlace

class Team(models.Model):
    name = models.CharField(max_length=256)
    player1 = models.ForeignKey(UserProfile, related_name="pubgolf_player1")
    player2 = models.ForeignKey(UserProfile, related_name="pubgolf_player2")

    def __unicode__(self):
        return "Team:" + unicode(self.name) + " with players " + unicode(self.player1) + ", " + unicode(self.player2)

class Score(models.Model):
    player = models.ForeignKey(UserProfile, related_name="pubgolf_score")
    hole = models.ForeignKey('Hole')
    score = models.IntegerField()

    def __unicode__(self):
        return unicode(self.player) + " scored " + unicode(self.score) + " on " + unicode(self.hole)

class OrderedHole(models.Model):
    hole = models.ForeignKey('Hole')
    game = models.ForeignKey('PubGolf')
    order = models.IntegerField()

    def __unicode__(self):
        return unicode(self.hole) + " is stop " + unicode(self.order) + " in game " + unicode(self.game)

class Hole(models.Model):
    location = models.ForeignKey(GooglePlace)
    par = models.IntegerField()
    drink = models.CharField(max_length=256)

    def __unicode__(self):
        return "Drink a " + unicode(self.drink) + " at " + unicode(self.location) + " in " + unicode(self.par) + " drink(s)"

class PubGolf(Event):
    holes = models.ManyToManyField('Hole', related_name="holes", through='OrderedHole')
    teams = models.ManyToManyField('Team', related_name="teams")

    def __unicode__(self):
        return self.name
