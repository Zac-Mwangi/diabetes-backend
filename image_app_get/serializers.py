from rest_framework import serializers
from .models import ImageRecord

class ImageRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageRecord
        fields = ['id','user','image']
