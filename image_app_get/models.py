from django.db import models

from helpers.models import TrackingModel
from authentication.models import User
from image_app.models import *


# Create your models here.

class ImageRecord(TrackingModel, models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE , unique= True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

