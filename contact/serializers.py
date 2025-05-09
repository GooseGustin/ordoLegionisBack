from rest_framework import serializers
# from rest_framework.views import APIView
from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Feedback
        fields = [
            'id', 'user', 'content', 'date'
        ]
        read_only_fields = ['user', 'date']  

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user 
            validated_data['user'] = user
        return super().create(validated_data)

