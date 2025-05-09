from django.urls import path 
from rest_framework import routers 
from .views import AnnouncementViewSet, CuriaViewSet, announcementFormView, delete_announcement

router = routers.DefaultRouter()
router.register('announcements', AnnouncementViewSet)
router.register('curia', CuriaViewSet)

urlpatterns = router.urls 
urlpatterns += [
    path("announcement/form/", announcementFormView, name="announcement-form"),
    path("announcement/delete/", delete_announcement, name="announcement-delete"),
]