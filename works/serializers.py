from rest_framework import serializers 
from .models import *

class WorkSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Work
        fields = [
            'id', 
            'type', 
            'active', 
            'done', 
            'meeting',
            'details' 
        ]

class WorkListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = WorkList
        fields = [
            'id', 
            'praesidium',
            'details' 
        ]

class WorkTypeOptionSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = WorkTypeOption
        fields = [
            'id', 
            'name', 
            'metrics'
        ]

class WorkSummarySerializer(serializers.ModelSerializer):
    class Meta: 
        model = WorkSummary
        fields = [
            'id',
            'type', 
            'active', 
            'no_assigned',
            'no_done', 
            'report',
            'details' 
        ]


        # work_summaries_serializer = WorkSummarySerializer(data=work_summaries_data)
        # work_summaries_serializer.is_valid(raise_exception=True)
        # work_summaries = work_summaries_serializer.save()
