from django.urls import path
from rest_framework import routers 
from .views import (
    AnswerViewSet, 
    CommentViewSet,
    PostViewSet, 
    QuestionViewSet, 
    PrayerRequestViewSet,
)

router = routers.DefaultRouter()
router.register('answers', AnswerViewSet)
router.register('comments', CommentViewSet)
router.register('posts', PostViewSet)
router.register('questions', QuestionViewSet)
router.register('requests', PrayerRequestViewSet)
# router.register('questions', QuestionCreateView)

urlpatterns = router.urls 
# urlpatterns += [
#     path('questions', question_mixin_view, name='question-list'), 
#     path('questins/<int:pk>', question_mixin_view, name='question-retrieve'), 
# ]