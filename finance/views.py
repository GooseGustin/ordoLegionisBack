from rest_framework.response import Response 
from rest_framework import viewsets 
from .serializers import * 
from meetings.models import Meeting

# Create your views here.
class FinancialRecordViewSet(viewsets.ModelViewSet):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer

    def list(self, request): 
        print("In list method of WorkViewSet\n\n")
        meet_id = request.GET.get('mid') 
        if meet_id: # filter by meeting 
            meeting = Meeting.objects.get(id=meet_id)
            records = meeting.records # type:ignore 
            serializer = self.get_serializer(records, many=False)
            return Response(serializer.data)
        record = FinancialRecord.objects.all()
        serializer = self.get_serializer(record, many=True)
        return Response(serializer.data)

class FinancialSummaryViewSet(viewsets.ModelViewSet):
    queryset = FinancialSummary.objects.all()
    serializer_class = FinancialSummarySerializer

class AcctStatementViewSet(viewsets.ModelViewSet):
    queryset = AcctStatement.objects.all()
    serializer_class = AcctStatementSerializer

class AcctAnnouncementViewSet(viewsets.ModelViewSet): 
    queryset = AcctAnnouncement.objects.all() 
    serializer_class = AcctAnnouncementSerializer

class ExpensesViewSet(viewsets.ModelViewSet): 
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer