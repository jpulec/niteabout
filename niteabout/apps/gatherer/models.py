from django.db import models
from geoposition.fields import GeopositionField

class StringTag(models.Model):
    key = models.CharField(max_length="128")
    value = models.CharField(max_length="256")

    def __unicode__(self):
        return self.key + ":" + self.value

    class Meta:
        unique_together = ('key', 'value',)

class IntTag(models.Model):
    key = models.CharField(max_length=128)
    value = models.IntegerField()

    def __unicode__(self):
        return self.key + ":" + str(self.value)

    class Meta:
        unique_together = ('key','value',)

class Place(models.Model):
    id = models.IntegerField(primary_key=True)
    string_tags = models.ManyToManyField('StringTag', related_name="string_tags")
    int_tags = models.ManyToManyField('IntTag', related_name="int_tags")
    name = models.CharField(max_length="256")
    pos = GeopositionField()
    timestamp = models.DateTimeField(null=True)
    version = models.IntegerField(null=True)

    def __unicode__(self):
        return self.name + ":" + str(self.pos)

class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class Movie(models.Model):
    MPAA_CHOICES = (
            ("g", "G"),
            ("pg", "PG"),
            ("pg13", "PG-13"),
            ("r", "R"),
            ("nc17", "NC-17"),
        )
    tms_id = models.CharField(max_length=14)
    title = models.CharField(max_length=256)
    year = models.IntegerField()
    genres = models.ManyToManyField('Genre')
    rating = models.CharField(max_length=8, choices=MPAA_CHOICES)
    synopsis = models.TextField()
    runtime = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.title + " (" + str(self.year) + ") "

class MovieShowtime(models.Model):
    dt = models.DateTimeField()
    theater = models.ForeignKey('Place', null=True, blank=True)
    movie = models.ForeignKey('Movie')

    def __unicode__(self):
        return str(self.movie) + " is showing " + " at " + str(self.theater) + " at " + str(self.dt)

class MovieReview(models.Model):
    score = models.IntegerField()
    reviewer = models.CharField(max_length=64)
    movie = models.ForeignKey('Movie')

    def __unicode__(self):
        return self.reviewer + " gave " + str(self.movie) + " a " + str(self.score)

DAYS_OF_WEEK = (
        (0, "Sunday"),
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday")
        )


class BarSpecial(models.Model):
    bars = models.ManyToManyField('Place')
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.IntegerField(max_length=1, default=0, choices=DAYS_OF_WEEK)
    deal = models.TextField()

    def __unicode__(self):
        return str([bar for bar in self.bars.all()]) + " has " + self.deal + " on " + str(self.day) + " starting at " + str(self.start_time) + " until " + str(self.end_time)


from niteabout.apps.gatherer import signals
