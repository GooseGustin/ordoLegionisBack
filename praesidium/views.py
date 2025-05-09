from rest_framework import viewsets, status
from rest_framework.response import Response 
from rest_framework.views import APIView
from .models import Praesidium, Reminder
from .serializers import PraesidiumSerializer, ReminderSerializer
from accounts.models import Legionary
from curia.models import Curia
from curia.serializers import CuriaSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class PraesidiumViewSet(viewsets.ModelViewSet):
    queryset = Praesidium.objects.all()
    serializer_class = PraesidiumSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def list(self, request): 
        print("In list method of PraesidiumViewSet\n\n", request.GET)
        cid = request.GET.get('cid') 
        uid = request.GET.get('uid')
        if cid: # filter by praesidium 
            # Ensure user has access to this praesidium
            praesidia = self.queryset.filter(curia=cid)
            serializer = self.get_serializer(praesidia, many=True)
            return Response(serializer.data)
        if uid: # filter by user membership
            # Ensure user has permission
            legionary = Legionary.objects.get(user=request.user)
            praesidia = legionary.associated_praesidia          # type: ignore
            serializer = self.get_serializer(praesidia, many=True) 
            return Response(serializer.data) 

        serializer = self.get_serializer(Praesidium.objects.all(), many=True)
        return Response(serializer.data) 

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    
    def list(self, request): 
        print("In list method of ReminderViewSet\n\n", request.GET)
        pid = request.GET.get('pid') 
        if pid: # filter by praesidium 
            # Ensure user has access to this praesidium
            reminders = self.queryset.filter(praesidium=pid)
            serializer = self.get_serializer(reminders, many=True)
            return Response(serializer.data)
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data) 

class CouncilSearchView(APIView):
    def get(self, request, *args, **kwargs):
        print('In search view', request, request.query_params, dir(request))
        iden = request.query_params.get('iden')
        # iden = 'o49OL1334S'
        print("iden", iden)
        if Praesidium.objects.filter(iden=iden).exists():
            praesidium = Praesidium.objects.get(iden=iden) 
            serializer = PraesidiumSerializer(praesidium)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif Curia.objects.filter(iden=iden).exists():
            curia = Curia.objects.get(iden=iden)
            serializer = CuriaSerializer(curia)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({
            "type": "No result", 
            "name": "There is no curia or praesidium with that ID"
        }) #{}, status=status.HTTP_200_OK)
        
        # return Response(serializer.data, status=status.HTTP_200_OK)