from django.db import models

from authentication.models import User

from helpers.models import TrackingModel


# Create your models here.

class ReportModel(TrackingModel, models.Model):
    report_date = models.DateField()

    time_before_breakfast = models.TimeField()
    blood_before_breakfast = models.DecimalField(max_digits=5, decimal_places=2)

    time_at_breakfast = models.TimeField()
    breakfast_meal = models.CharField(max_length=100)

    time_at_lunch = models.TimeField()
    lunch_meal = models.CharField(max_length=100)

    time_at_dinner = models.TimeField()
    dinner_meal = models.CharField(max_length=100)

    time_after_dinner = models.TimeField()
    blood_after_dinner = models.DecimalField(max_digits=5, decimal_places=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

