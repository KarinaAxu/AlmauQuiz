from rest_framework import serializers
from .models import QuizQuestion, QuizAnswer, QuizResult


class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswer
        fields = ['icon', 'text']


class QuizQuestionSerializer(serializers.ModelSerializer):
    answers = QuizAnswerSerializer(many=True)

    class Meta:
        model = QuizQuestion
        fields = ['question_text', 'answers']


class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResult
        fields = ['answers']
