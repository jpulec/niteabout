from django.db import models

from niteabout.apps.places.models import Place

class NiteActivity(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class NiteWho(models.Model):
    who = models.CharField(max_length=16)

    def __unicode__(self):
        return self.who

class NiteWhat(models.Model):
    what = models.CharField(max_length=256)

    def __unicode__(self):
        return self.what

class NiteTemplate(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    activities = models.ManyToManyField('NiteActivity')
    who = models.ManyToManyField('NiteWho')
    what = models.ManyToManyField('NiteWhat')

    def __unicode__(self):
        return self.name + ":" + self.description

class NitePlan(models.Model):
    pass
