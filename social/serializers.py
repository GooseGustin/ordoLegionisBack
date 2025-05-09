from rest_framework import serializers
# from rest_framework.views import APIView
from .models import Answer, Post, Question, PrayerRequest, Comment
from accounts.models import Legionary


class AnswerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Answer
        fields = [
            'id', 'content', 'date', 
            'creator_name', 'legionary', 
            'question', 'upvotes', 'downvotes', 
            'flags'
        ]
        read_only_fields = ['legionary', 'date', 'flags']
    
    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user 
            legionary = Legionary.objects.get(user=user)
            validated_data['legionary'] = legionary 
            creator_name = validated_data.pop('creator_name', user.username)
            validated_data['creator_name'] = creator_name
        return super().create(validated_data)

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        fields = [
            'id', 'content', 'date', 
            'creator_name', 'legionary', 
            'post', 'flags'
        ]
        read_only_fields = ['legionary', 'date', 'flags']
    
    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user 
            legionary = Legionary.objects.get(user=user)
            validated_data['legionary'] = legionary 
            creator_name = validated_data.pop('creator_name', user.username)
            validated_data['creator_name'] = creator_name
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post
        fields = [
            'id', 'title', 'content', 
            'image', 'creator_name', 
            'date', 'legionary', 
            'upvotes', 'downvotes', 'flags'
        ]
        read_only_fields = ['legionary', 'date', 'flags']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user 
            legionary = Legionary.objects.get(user=user)
            validated_data['legionary'] = legionary 
            creator_name = validated_data.pop('creator_name', user.username)
            validated_data['creator_name'] = creator_name
        return super().create(validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    # flags = QuestionFlag
    class Meta: 
        model = Question
        fields = [
            'id', 'legionary', 'content', 'creator_name',
            'date', 'flags'
        ]
        read_only_fields = ['legionary', 'date', 'flags']  # Legionary is set automatically

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user 
            legionary = Legionary.objects.get(user=user)
            validated_data['legionary'] = legionary 
            creator_name = validated_data.pop('creator_name', user.username)
            validated_data['creator_name'] = creator_name
        return super().create(validated_data)


class PrayerRequestSerializer(serializers.ModelSerializer):
    # flags = QuestionFlag
    class Meta: 
        model = PrayerRequest
        fields = [
            'id', 'legionary', 'content', 'creator_name', 
            'date', 'flags', 'upvotes', 'downvotes'
        ]
        read_only_fields = ['legionary', 'date', 'flags']  # Legionary is set automatically

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user 
            legionary = Legionary.objects.get(user=user)
            validated_data['legionary'] = legionary 
            creator_name = validated_data.pop('creator_name', user.username)
            validated_data['creator_name'] = creator_name
        return super().create(validated_data)
