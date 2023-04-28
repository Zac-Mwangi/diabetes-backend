from rest_framework import serializers
from .models import QuestionAnswer

from questions_app.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'



class QuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAnswer
        fields = ['id', 'question', 'user', 'answer_text',]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # check if it's a GET request
        if self.context['request'].method == 'GET':
            self.fields['question'] = QuestionSerializer()
        



