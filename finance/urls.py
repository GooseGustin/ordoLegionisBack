from rest_framework import routers 
from .views import (
    FinancialRecordViewSet, 
    FinancialSummaryViewSet, 
    AcctAnnouncementViewSet, AcctStatementViewSet, 
    ExpensesViewSet
)

router = routers.DefaultRouter()
router.register('records', FinancialRecordViewSet)
router.register('summaries', FinancialSummaryViewSet)
router.register('announcements', AcctAnnouncementViewSet)
router.register('statements', AcctStatementViewSet)
router.register('expenses', ExpensesViewSet)

urlpatterns = router.urls 