from rest_framework import routers 
from .views import * 
from django.urls import path 

router = routers.DefaultRouter()
router.register('report', ReportViewSet)
router.register('attendance', FunctionAttendanceViewSet)
router.register('membership', MembershipDetailsViewSet)
router.register('achievement', AchievementViewSet)

urlpatterns = router.urls 

urlpatterns += [
    path('get_report_prep_data', ReportPrepGetView.as_view(), name='get-report-prep-data'), 
    path('download', GenerateReportView.as_view(), name='download')
    # path('download', generate_report_view, name='download'),
]