from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import status
from .models import QuestionAnswer
from .serializers import QuestionAnswerSerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def question_answer_list_get(request,pk):
    """
    List all question answers for answerd by a particuar user
    """
    question_answers = QuestionAnswer.objects.filter(user=pk)
    serializer = QuestionAnswerSerializer(question_answers, many=True)
    return Response(serializer.data)


# post the questions and answers for the user 
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def question_answer_list_post(request):
    """
    Create a new question answer
    """
    serializer = QuestionAnswerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
