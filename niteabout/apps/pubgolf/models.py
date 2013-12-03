from django.db import models

from niteabout.apps.main.models import UserProfile
from niteabout.apps.places.models import Place

class Team(models.Model):
    name = models.CharField(max_length=256)
    player1 = models.ForeignKey(UserProfile, related_name="player1")
    player2 = models.ForeignKey(UserProfile, related_name="player2")

    def __unicode__(self):
        return "Team:" + unicode(self.name) + " with players " + unicode(self.player1) + ", " + unicode(self.player2)

class Score(models.Model):
    team = models.ForeignKey(Team)
    hole = models.ForeignKey(Hole)
    score = models.IntegerField()

class Hole(models.Model):
    location = models.ForeignKey(Place)
    par = models.IntegerField()
    drink = models.CharField(max_length=256)

class Course(models.Model):
    holes = models.ManyToManyField(Hole)

class Tournament(models.Model):
    name = models.CharField(max_length=256)
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return self.name
