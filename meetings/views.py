from .serializers import MeetingSerializer, MeetingNotesSerializer
from rest_framework import viewsets 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Meeting, MeetingNotes
from praesidium.models import Praesidium
from reports.models import Report
from datetime import date, datetime, timezone 

class MeetingNotesViewSet(viewsets.ModelViewSet): 
    queryset = MeetingNotes.objects.all()
    serializer_class = MeetingNotesSerializer

    # def 

class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all().order_by('-date')
    serializer_class = MeetingSerializer
    # paginate_by = 5

    def list(self, request):
        print("In list method of FxnAttendanceView\n\n")
        praes_id = request.GET.get('pid') 
        # praesidium = Praesidium.objects.get(id=praes_id) 

        if praes_id:
            meetings = self.queryset.filter(praesidium=praes_id)
            serializer = self.get_serializer(meetings, many=True)
            return Response(serializer.data)
        return super().list(self, request)


class MeetingFilterView(APIView):
    def post(self, request, *args, **kwargs):
        # print(dir(request))
        # print(request.data, request.query_params)
        pid = request.data.get('pid')
        # print("In meeting filter, pid", pid)
        praesidium = Praesidium.objects.get(id=pid) 
        meeting_start = request.data.get('startDate', praesidium.inaug_date.isoformat()) # type:ignore
        print("In meeting filter, startDate", meeting_start)
        # today = datetime.today().date()
        # default_end_date = str(today) 
        meeting_end = request.data.get('endDate')
        loc = "In filter meeting"

        serializer_class = MeetingSerializer

        if meeting_end: 
            # Get meeting range 

            meeting_start = [int(i) for i in meeting_start.split('-')]
            meeting_end = [int(i) for i in meeting_end.split('-')]
            start_date = date(*meeting_start) # .replace(tzinfo=timezone.utc)
            end_date = date(*meeting_end) # .replace(tzinfo=timezone.utc)
            praesidium_meetings = Meeting.objects.filter(praesidium=praesidium).order_by('-date')
            meetings_within_range = praesidium_meetings.filter(date__range=(start_date, end_date))
            # print(loc, "Meetings within range", meetings_within_range)
            serializer = serializer_class(meetings_within_range, many=True)
            return Response(serializer.data)

        elif meeting_start: 
            # Get particular meeting

            # start_date_unstart_date_undasheddashed = 
            start_date_nums = [int(i) for i in meeting_start.split('-')]
            start_date = date(*start_date_nums) # .replace(tzinfo=timezone.utc)
            praesidium_meetings = Meeting.objects.filter(praesidium=praesidium).order_by('-date')
            # print(loc, 'praesidium meetings', praesidium_meetings)
            # print('\n', [meeting.date for meeting in praesidium_meetings], start_date)
            meeting_for_date = praesidium_meetings.filter(date=start_date)
            # print(loc, 'Filtered meeting for this date', meeting_for_date)
            serializer = serializer_class(meeting_for_date, many=True)
            return Response(serializer.data)
        