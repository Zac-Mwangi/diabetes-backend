from django.urls import path
from .views import *

urlpatterns = [
    path('image', ImageCreateView.as_view(), name='image_list'),
    path('image/<int:pk>', ImageRetrieveUpdateDestroyView.as_view(), name='image_detail'),
]
