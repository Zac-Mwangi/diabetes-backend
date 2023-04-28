from rest_framework import generics
from .models import Question
from .serializers import QuestionSerializer


class QuestionList(generics.ListCreateAPIView):

    # bypass authentication
    authentication_classes = []


    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# get all qustions that were not addd by the user
    def get_queryset(self):
        return Question.objects.filter(added_by_user=False)


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):


    # bypass authentication
    authentication_classes = []

    
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

