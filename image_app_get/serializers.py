from rest_framework import serializers
from .models import ImageRecord
from image_app.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id','image']


class ImageRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageRecord
        fields = ['id','user','image']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # check if it's a GET request
        if self.context['request'].method == 'GET':
            self.fields['image'] = ImageSerializer()
