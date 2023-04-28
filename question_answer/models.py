from django.db import models

from authentication.models import User
from helpers.models import TrackingModel
from questions_app.models import *





class QuestionAnswer(TrackingModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
