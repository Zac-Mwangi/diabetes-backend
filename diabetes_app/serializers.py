from rest_framework import serializers
from .models import ReportModel

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportModel
        fields = '__all__'
