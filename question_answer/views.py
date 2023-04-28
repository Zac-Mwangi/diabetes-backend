from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import QuestionAnswer
from .serializers import QuestionAnswerSerializer

@api_view(['GET', 'POST'])
def question_answer_list(request):
    """
    List all question answers or create a new question answer
    """
    if request.method == 'GET':
        question_answers = QuestionAnswer.objects.all()
        serializer = QuestionAnswerSerializer(question_answers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def question_answer_detail(request, pk):
    """
    Retrieve, update or delete a question answer instance
    """
    try:
        question_answer = QuestionAnswer.objects.get(pk=pk)
    except QuestionAnswer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionAnswerSerializer(question_answer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuestionAnswerSerializer(question_answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question_answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
