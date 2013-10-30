from django.db import models

from niteabout.apps.places.models import Place, FeatureName

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

class NiteFeature(models.Model):
    feature_name = models.ForeignKey(FeatureName)
    score = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    template = models.ForeignKey('NiteTemplate')

    def __unicode__(self):
        return unicode(self.template) + ":" + unicode(self.feature_name) + ":" + unicode(self.score)

class NiteEvent(models.Model):
    place = models.ForeignKey(Place)
    activity = models.ForeignKey('NiteActivity')

class NiteEventOrdered(models.Model):
    place = models.ForeignKey(Place)
    activity = models.ForeignKey('NiteActivity')
    order = models.IntegerField()

    def __unicode__(self):
        return unicode(self.order) + ":" + unicode(self.activity) + ":" + unicode(self.place)

class NitePlan(models.Model):
    events = models.ManyToManyField('NiteEventOrdered')

    def __unicode__(self):
        return unicode(self.events)
