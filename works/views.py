# from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.response import Response
from .serializers import (
    WorkSerializer, 
    WorkListSerializer, 
    WorkTypeOptionSerializer, 
    WorkSummarySerializer
)
from .models import Work, WorkList, WorkTypeOption, WorkSummary

# Create your views here.
class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    def list(self, request): 
        print("In list method of WorkViewSet\n\n")
        meet_id = request.GET.get('mid') 
        if meet_id: # filter by meeting 
            works = self.queryset.filter(meeting=meet_id)
            serializer = self.get_serializer(works, many=True)
            return Response(serializer.data)
        work = Work.objects.all()
        serializer = self.get_serializer(work, many=True)
        return Response(serializer.data)
        
class WorkListViewSet(viewsets.ModelViewSet):
    queryset = WorkList.objects.all()
    serializer_class = WorkListSerializer 

    def list(self, request): 
        print("In list method of WorkListViewSet\n\n")
        praes_id = request.GET.get('pid') 
        if praes_id: # filter by praesidium 
            # Ensure user has access to this praesidium
            work_list = self.queryset.get(praesidium=praes_id)
            serializer = self.get_serializer(work_list, many=False)
            return Response(serializer.data)
        # work_list = WorkList.objects.all()
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data) 

class WorkTypeOptionViewSet(viewsets.ModelViewSet):
    queryset = WorkTypeOption.objects.all()
    serializer_class = WorkTypeOptionSerializer


class WorkSummaryViewSet(viewsets.ModelViewSet):
    queryset = WorkSummary.objects.all()
    serializer_class = WorkSummarySerializer

    def list(self, request): 
        print("In list method of WorkSummaryViewSet\n\n")
        rid = request.GET.get('rid') 
        if rid: # filter by report 
            # Ensure the user has access to this report
            work_summary = self.queryset.get(report=rid)
            serializer = self.get_serializer(work_summary, many=False)
            return Response(serializer.data)
        serializer = self.get_serializer(self.queryset, many=True)
        print(serializer.data)
        return Response(serializer.data) 
