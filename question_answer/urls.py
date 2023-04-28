from django.urls import path
from .views import *

urlpatterns = [
    path('question-answers/', question_answer_list, name='question_answer_list'),
    path('question-answers/<int:pk>/', question_answer_detail, name='question_answer_detail'),
]
