from django.db import models

from niteabout.apps.places.models import Place, PlaceCategory, FeatureName

class NiteActivityName(models.Model):
    name = models.CharField(max_length=128)
    categories = models.ManyToManyField(PlaceCategory)

    def __unicode__(self):
        return unicode(self.name) + ":" + unicode(",".join([cat.name for cat in self.categories.all()]))

class NiteActivity(models.Model):
    activity_name = models.ForeignKey('NiteActivityName')
    order = models.IntegerField()

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return unicode(self.order) + ":" + unicode(self.activity_name)

class NiteEvent(models.Model):
    activity = models.ForeignKey('NiteActivity')
    place = models.ForeignKey(Place)

    def __unicode__(self):
        return unicode(self.activity) + ":" + unicode(self.place)

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


class NitePlan(models.Model):
    events = models.ManyToManyField('NiteEvent')

    def __unicode__(self):
        return unicode(self.events)
