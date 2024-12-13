from rest_framework import serializers
from .models import Questions

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'question', 'choice_1', 'choice_2', 'choice_3', 'choice_4', 'answer']
