from django.db import models

from authentication.models import User
from helpers.models import TrackingModel


# Create your models here.

class QuestionModel(TrackingModel, models.Model):

    question_text = models.TextField()
    added_by_user = models.BooleanField() 

    def __str__(self):
        return self.question_text
    

class QuestionAnswerModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    answer_text = models.TextField()
