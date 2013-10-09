from django.db import models

from niteabout.apps.places.models import Theater

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
    theater = models.ForeignKey(Theater, null=True, blank=True)
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
