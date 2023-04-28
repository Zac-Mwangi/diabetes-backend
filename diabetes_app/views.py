from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ReportModel
from .serializers import ReportSerializer

from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import status
from rest_framework.decorators import api_view

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




@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def User_Reports(request, pk):
    """
    List all question answers for answered by a particular user
    """
    user_entry = ReportModel.objects.filter(user=pk)

    if user_entry.exists():
        serializer = ReportSerializer(user_entry, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"message": "No reports found for the specified user."}, status=status.HTTP_404_NOT_FOUND)