from django.urls import path 
from rest_framework import routers 
from .views import PraesidiumViewSet, ReminderViewSet, CouncilSearchView

router = routers.DefaultRouter()
router.register('praesidium', PraesidiumViewSet)
router.register('reminders', ReminderViewSet)

urlpatterns = router.urls 

urlpatterns += [
    path('council_search', CouncilSearchView.as_view(), name='council-search'), 
]