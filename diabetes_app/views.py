from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ReportModel
from .serializers import ReportSerializer

class ReportListCreateView(ListCreateAPIView):

# bypass authentication
    authentication_classes = []

    queryset = ReportModel.objects.all()
    serializer_class = ReportSerializer

class ReportRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    
# bypass authentication
    authentication_classes = []

    queryset = ReportModel.objects.all()
    serializer_class = ReportSerializer
