from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Questions
from .serializers import QuestionSerializer
import random

class QuestionListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        question_ids = Questions.objects.values_list('id', flat=True)
        random_ids = random.sample(list(question_ids), 5)
        quiz_questions = Questions.objects.filter(id__in=random_ids)
        serializer = QuestionSerializer(quiz_questions, many=True)
        return Response(serializer.data)



