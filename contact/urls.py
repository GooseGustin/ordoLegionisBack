from django.urls import path
from rest_framework import routers 
from .views import FeedbackViewSet

router = routers.DefaultRouter()
router.register('feedback', FeedbackViewSet)

urlpatterns = router.urls 