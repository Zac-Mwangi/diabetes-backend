from django.urls import path
from .views import ReportListCreateView, ReportRetrieveUpdateDestroyView

app_name = 'reports'

urlpatterns = [
    path('reports', ReportListCreateView.as_view(), name='report-list-create'),
    path('reports/<int:pk>', ReportRetrieveUpdateDestroyView.as_view(), name='report-detail'),
]
