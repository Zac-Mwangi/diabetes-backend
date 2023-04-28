from django.urls import path
from . import views

urlpatterns = [
    path('image-records-get/<int:pk>', views.image_record_get, name='image-records-get'),
    path('image-records-post', views.image_record_post, name='image-records-post'),
]
