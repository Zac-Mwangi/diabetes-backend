from django.db import models

from helpers.models import TrackingModel

# Create your models here.

class Image(TrackingModel, models.Model):

    image = models.TextField()

    def __str__(self):
        return self.image