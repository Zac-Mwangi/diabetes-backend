from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import ImageRecord
from .serializers import ImageRecordSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def image_record_get(request,pk):
    image_record = ImageRecord.objects.filter(user=pk)
    serializer = ImageRecordSerializer(image_record, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def image_record_post(request):
    serializer = ImageRecordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
