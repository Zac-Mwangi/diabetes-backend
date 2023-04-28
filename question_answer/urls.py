from django.urls import path
from .views import *

urlpatterns = [
    path('question-answers/<int:pk>', question_answer_list_get, name='question_answer_list_get'),
    path('question-answers', question_answer_list_post, name='question_answer_list_post'),
]
