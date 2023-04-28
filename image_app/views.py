from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Image
from .serializers import ImageSerializer

class ImageCreateView(ListCreateAPIView):

# bypass authentication
    authentication_classes = []

    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    
# bypass authentication
    authentication_classes = []
    
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

