from django.urls import path
from .views import ReportListCreateView, ReportRetrieveUpdateDestroyView

from .views import *


app_name = 'reports'

urlpatterns = [
    path('reports', ReportListCreateView.as_view(), name='report-list-create'),
    path('reports_user/<int:pk>', User_Reports, name='User_Reports'),
    path('reports/<int:pk>', ReportRetrieveUpdateDestroyView.as_view(), name='report-detail'),
]
