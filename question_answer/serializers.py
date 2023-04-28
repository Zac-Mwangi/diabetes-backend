from rest_framework import serializers
from .models import QuestionAnswer

from questions_app.models import Question
from authentication.models import User


class QuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAnswer
        fields = ['id', 'question', 'user', 'answer_text',]
        



