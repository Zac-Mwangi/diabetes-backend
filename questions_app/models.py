from django.db import models

from authentication.models import User
from helpers.models import TrackingModel


# Create your models here.

class Question(TrackingModel, models.Model):

    question_text = models.TextField()
    added_by_user = models.BooleanField() 

    def __str__(self):
        return self.question_text
