from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet # , GenericViewSet
from rest_framework.response import Response
# from rest_framework import status, generics, mixins
from rest_framework.decorators import action 
from .models import (
    Answer, 
    Comment,
    Post, 
    Question, 
    PrayerRequest
)
from .serializers import (
    AnswerSerializer, 
    CommentSerializer,
    PostSerializer, 
    QuestionSerializer, 
    PrayerRequestSerializer
)
from accounts.models import Legionary

class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all().order_by('-date')
    serializer_class = AnswerSerializer
    # permission_classes = [permissions.AllowAny]

    def list(self, request): 
        qid = request.GET.get('qid')
        # print(request.data, request.GET)
        print("in answers list view", qid)
        if qid: 
            question = Question.objects.get(id=qid)
            answers = question.answers.order_by('-date')
            serializer = self.serializer_class(answers, many=True)
            print('answers returned', answers)
            return Response(serializer.data)
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by('-date')
    serializer_class = CommentSerializer
    # permission_classes = [permissions.AllowAny]

    def list(self, request): 
        pid = request.GET.get('pid')
        # print(request.data, request.GET)
        print("in comments list view", pid)
        if pid: 
            post= Post.objects.get(id=pid)
            comments = post.comments.order_by('-date') 
            serializer = self.serializer_class(comments, many=True)
            print('answers returned', comments)
            return Response(serializer.data)
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)


class PostViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs): 
        print("In post list view")
        # legionary = Legionary.objects.get(user=request.user) 
        # posts = self.queryset.filter(legionary=legionary)
        # print("In post list view", posts)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs): 
        print("In question list view")
        # legionary = Legionary.objects.get(user=request.user) 
        # questions = self.queryset.filter(legionary=legionary)
        # print("In postlist view", questions)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

class PrayerRequestViewSet(ModelViewSet):
    queryset = PrayerRequest.objects.all()
    serializer_class = PrayerRequestSerializer

    def list(self, request, *args, **kwargs): 
        print("In prayer request list view")
        # legionary = Legionary.objects.get(user=request.user) 
        # requests = self.queryset.filter(legionary=legionary)
        # print("In prayer request list view", requests)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
