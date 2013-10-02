from django.db import models
from geoposition.fields import GeopositionField
from planit.apps.gatherer import signals

class Tag(models.Model):
    key = models.CharField(max_length="128")
    value = models.CharField(max_length="256")

    def __unicode__(self):
        return self.key + ":" + self.value

    class Meta:
        unique_together = ('key', 'value',)

class Place(models.Model):
    id = models.IntegerField(primary_key=True)
    tags = models.ManyToManyField('Tag', related_name="tags")
    name = models.CharField(max_length="256")
    pos = GeopositionField()
    timestamp = models.DateTimeField(null=True)
    version = models.IntegerField(null=True)


    def loudness(self):
        return self.tags.get(key="loudness").value

    def opening_hours(self):
        return self.tags.get(key="opening_hours").value

    def amenity(self):
        return self.tags.filter(key="amenity").values_list('value', flat=True)

    def get_tags(self):
        return self.tags.all()

    def __unicode__(self):
        return self.name + ":" + str(self.pos)

class Genre(models.Model):
    name = models.CharField(max_length=64)

class Movie(models.Model):
    MPAA_CHOICES = (
            ("g", "G"),
            ("pg", "PG"),
            ("pg13", "PG-13"),
            ("r", "R"),
            ("nc17", "NC-17"),
        )

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256)
    year = models.IntegerField()
    genres = models.ManyToManyField('Genre')
    mpaa = models.CharField(max_length=8, choices=MPAA_CHOICES)
    synopsis = models.TextField()
    runtime = models.IntegerField()


class MovieReview(models.Model):
    score = models.IntegerField()
    reviewer = models.CharField(max_length=64)
    movie = models.ForeignKey('Movie')

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
    bar = models.ForeignKey('Place')
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.IntegerField(max_length=1, default=0, choices=DAYS_OF_WEEK)
    deal = models.TextField()

    def __unicode__(self):
        return str(self.bar.name) + " has " + self.deal + " on " + str(self.day) + " starting at " + str(self.start_time) + " until " + str(self.end_time)
