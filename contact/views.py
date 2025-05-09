from rest_framework.viewsets import ModelViewSet 
from rest_framework.response import Response
from .models import Feedback
from .serializers import FeedbackSerializer

# Create your views here.
class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def list(self, request, *args, **kwargs): 
        print("In feedback list view")
        
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
    