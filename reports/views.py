from rest_framework.response import Response
from rest_framework import viewsets, status 
from rest_framework.views import APIView
from django.http import FileResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import * 
from .models import (
    Report, FunctionAttendance, MembershipDetail, Achievement
)
from praesidium.models import Praesidium
from praesidium.serializers import PraesidiumSerializer
from curia.models import Curia 
from curia.serializers import CuriaSerializer
from meetings.models import Meeting
from works.models import Work, WorkList
from works.serializers import WorkListSerializer
from finance.models import FinancialRecord, FinancialSummary
from finance.serializers import FinancialSummarySerializer
from api.function_vault import removeDuplicates
from datetime import date, datetime 
from math import ceil
from pprint import pprint
from .generator import generate_report_docx

# Create your views here.
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all() # filter by manager
    serializer_class = ReportSerializer

    def list(self, request): 
        print("In list method of WorkListViewSet\n\n")
        praes_id = request.GET.get('pid') 
        if praes_id: # filter by praesidium 
            # Ensure user has access to this praesidium
            reports = self.queryset.filter(praesidium=praes_id)
            serializer = self.get_serializer(reports, many=True)
            return Response(serializer.data)
        # work_list = WorkList.objects.all()
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data) 
        
class FunctionAttendanceViewSet(viewsets.ModelViewSet):
    queryset = FunctionAttendance.objects.all()
    serializer_class = FunctionAttendanceSerializer
    
    def list(self, request):
        # if request.method == 'GET': 
        print("In list method of FxnAttendanceView\n\n")
        praes_id = request.GET.get('pid') 
        report_id = request.GET.get('id')
        if praes_id and report_id: # filter by both praesidium and report
            praesidium = Praesidium.objects.get(id=praes_id)
            report = praesidium.reports.get(id=report_id) # type:ignore
            serializer = self.get_serializer(report.function_attendances, many=True)
            return Response(serializer.data)
        return super().list(self, request)

class MembershipDetailsViewSet(viewsets.ModelViewSet):
    queryset = MembershipDetail.objects.all()
    serializer_class = MembershipDetailsSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class ReportPrepGetView(APIView):
    def post(self, request, *args, **kwargs):
        # print(request.data, dir(request))
        pid = request.data.get('pid')
        praesidium = Praesidium.objects.get(id=pid) 
        # print("In report prep get view", pid, praesidium.id, praesidium.name) # type:ignore
        praesidium_meetings = Meeting.objects.filter(praesidium=pid).order_by('date')
        
        # Get meeting range
        # useLoaderData will provide meetings from last submission or inaug date to today
        # autofill will return meetings within logical date range
        meeting_start = request.data.get('startDate', praesidium.inaug_date.isoformat()) # type:ignore
        if not meeting_start: meeting_start = praesidium.inaug_date.isoformat() # type:ignore
        today = datetime.today().date()
        meeting_end = request.data.get('endDate', str(today))
        if not meeting_end: meeting_end = str(today)

        meeting_start = [int(i) for i in meeting_start.split('-')]
        meeting_end = [int(i) for i in meeting_end.split('-')]
        
        start_date = date(*meeting_start) # .replace(tzinfo=timezone.utc)
        end_date = date(*meeting_end) # .replace(tzinfo=timezone.utc)
        # print("Start and end dates", start_date, end_date)
        meetings_within_range = praesidium_meetings.filter(date__range=(start_date, end_date))

        # Get curia attendance
        simple_curia_meetings_held = (end_date - start_date).days // 28
        no_curia_meetings_held = {
            "President": (end_date - praesidium.pres_app_date).days // 28 if (praesidium.pres_app_date > start_date) else simple_curia_meetings_held, # type:ignore
            "Vice President": (end_date - praesidium.vp_app_date).days // 28 if (praesidium.vp_app_date > start_date) else simple_curia_meetings_held, # type:ignore
            "Secretary": (end_date - praesidium.sec_app_date).days // 28 if (praesidium.sec_app_date > start_date) else simple_curia_meetings_held, # type:ignore
            "Treasurer": (end_date - praesidium.tres_app_date).days // 28 if (praesidium.tres_app_date > start_date) else simple_curia_meetings_held # type:ignore
        }

        # Get praesidium attendance 
        meetings_held_pres = praesidium_meetings.filter(date__range=(praesidium.pres_app_date, end_date)) if (praesidium.pres_app_date > start_date) else meetings_within_range  # type:ignore
        meetings_held_vp = praesidium_meetings.filter(date__range=(praesidium.vp_app_date, end_date)) if (praesidium.vp_app_date > start_date) else meetings_within_range # type:ignore
        meetings_held_sec = praesidium_meetings.filter(date__range=(praesidium.sec_app_date, end_date)) if (praesidium.sec_app_date > start_date) else meetings_within_range # type:ignore
        meetings_held_tres = praesidium_meetings.filter(date__range=(praesidium.tres_app_date, end_date)) if praesidium.tres_app_date > start_date else meetings_within_range # type:ignore

        no_praesidium_meetings_held = {
            "President": len(meetings_held_pres), 
            "Vice President": len(meetings_held_vp), 
            "Secretary": len(meetings_held_sec), 
            "Treasurer": len(meetings_held_tres)
        }

        no_curia_meetings_held_previous = {
            "President": 0, 
            "Vice President": 0, 
            "Secretary": 0,  
            "Treasurer": 0
        }
        no_praesidium_meetings_held_previous = no_curia_meetings_held_previous.copy()

        no_of_meetings_expected = (end_date - start_date).days // 7 
        no_of_meetings_held = len(meetings_within_range)
        average_attendance = 0

        # Get officers meeting and curia attendance 
        officers_curia_attendance = {
            'President': 0, 'Vice President':0, 'Secretary':0, 'Treasurer':0
        }
        officers_meeting_attendance = {
            'President': 0, 'Vice President':0, 'Secretary':0, 'Treasurer':0
        }
        for meeting in meetings_within_range: 
            # Get officers meeting and curia attendance 
            for officer in ['President', 'Vice President', 'Secretary', 'Treasurer']: 
                if officer in meeting.officers_meeting_attendance: 
                    officers_meeting_attendance[officer] += 1
                if officer in meeting.officers_curia_attendance:
                    officers_curia_attendance[officer] += 1
                
            # Get average attendance
            average_attendance += meeting.no_present
        average_attendance = ceil(average_attendance / (no_of_meetings_held or 1))


        # Get submission and last submission date
        last_report = Report.objects.filter(praesidium=praesidium).last()

        # Perhaps the last report is the current report, the submission date
        # will be in the future not the past, so we take the last submision
        # date instead 
        last_submission_date = str(today)
        report_number = 1
        if last_report: 
            if last_report.submission_date and last_report.submission_date < today:
                last_submission_date = last_report.submission_date 
            else: 
                last_submission_date = last_report.last_submission_date
            report_number = last_report.report_number
            no_curia_meetings_held_previous = last_report.no_curia_meetings_held
            no_praesidium_meetings_held_previous = last_report.no_praesidium_meetings_held


        # Get work summaries
        worklist = WorkList.objects.get(praesidium=pid)
        active_work_names = [obj['name'] for obj in worklist.details if (obj['active'] and obj['tracking'])]
        # inactive_work_names = [obj['name'] for obj in worklist.details if (not obj['active'] and obj['tracking'])] 
        work_names = [obj['name'] for obj in worklist.details if obj['tracking']] 
        names_to_metrics = {item['name']:item['metrics'] for item in worklist.details if item['tracking']}
        # Initialise work summaries
        work_summaries = [
            {
                "type": work_name, 
                "active": work_name in active_work_names, 
                "no_done": 0, 
                "no_assigned": 0,
                "details": {}
            } for work_name in work_names
        ]

        for meeting in meetings_within_range: 
            works_for_meeting = Work.objects.filter(meeting=meeting.id) # type:ignore
            # print("\nWorks for meeting", works_for_meeting)

            for workObj in works_for_meeting: 
                # Find location of summary in summaries corresponding to this workObj type 
                # in order to update it when looping through metrics
                work_summary = list(
                    filter(
                        lambda obj: obj['type'] == workObj.type, 
                        work_summaries
                        )
                    )
                if work_summary:
                    work_summary_ind = work_summaries.index(work_summary[0])
                    work_summaries[work_summary_ind]['no_assigned'] += 1
                    if workObj.done:
                        work_summaries[work_summary_ind]['no_done'] += 1
                    
                    # print('\nWork summary index', work_summary_ind, work_summary)
                    specific_work_metrics = names_to_metrics[workObj.type]

                    for metric in specific_work_metrics.keys(): 
                        if specific_work_metrics[metric]: # Check that metric is being tracked
                            # Initiaise metrics values
                            if not work_summaries[work_summary_ind]['details'].get(metric): 
                                work_summaries[work_summary_ind]['details'][metric] = 0
                            # Loop through list of same work, start incrementing count of each metric
                            count = workObj.details.get(metric) # type:ignore
                            # print('Looping through metrics', workObj.details, metric, count)
                            if count: 
                                work_summaries[work_summary_ind]['details'][metric] += int(count)
                # else: 
                #     print("Looks like we have a work that's not in the worklist")


        # Get financial summary
        months = [
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
        ]
        getMonth = lambda ymd: [int(i) for i in str(ymd).split('-')]
        month_year_combo = []
        for meeting in meetings_within_range: 
            [year, month, day] = getMonth(meeting.date)
            # print('Date', months[month-1], year)
            month_year_combo.append(
                {"month": months[month-1], "year": year}
            )

        # Remove duplicates
        month_year_combo = removeDuplicates(month_year_combo)
        fin_summaries = removeDuplicates(month_year_combo)
        # print('initialised fin_summaries', fin_summaries, '\n', month_year_combo)

        # Initialise
        for item in fin_summaries: 
            ind = fin_summaries.index(item)
            fin_summaries[ind]['bf'] = None
            fin_summaries[ind]['sbc'] = 0
            fin_summaries[ind]['balance'] = 0
            fin_summaries[ind]['remittance'] = 0
            fin_summaries[ind]['expenses'] = {
                "bouquet": 0, 
                "stationery": 0, 
                "altar": 0, 
                "extension": 0,
                "others": []
            }

        # Update financial summary
        
        acf_set = set() # Track first occurrence of ACF for each month

        for meeting in meetings_within_range[1:]: 
            [year, month, _] = getMonth(meeting.date)
            # print("year and month", year, month)
            item_array = [i for i in fin_summaries if (i['month']==months[month-1] and i['year']==year)]
            item = item_array[0]
            ind = fin_summaries.index(item)

            fin_record = FinancialRecord.objects.get(meeting=meeting.id) # type:ignore
            acf = fin_record.acct_statement.acf
            # sbc = fin_record.acct_announcement.sbc
            sbc = fin_record.acct_statement.sbc
            bal = fin_record.acct_statement.balance
            exp = fin_record.acct_statement.expenses

            month_key = (month, year) 
            if month_key not in acf_set: 
                # Only keep the first for the month
                fin_summaries[ind]['bf'] = acf 
                acf_set.add(month_key)  # Mark this month as recorded
                # print('Set acf for', month_key, acf)

            fin_summaries[ind]['sbc'] += sbc 


            fin_summaries[ind]['balance'] = bal # so that the last balance for the month (ind) is kept
            fin_summaries[ind]['remittance'] += exp.remittance
            fin_summaries[ind]['expenses']["bouquet"] += exp.bouquet
            fin_summaries[ind]['expenses']["extension"] += exp.extension
            fin_summaries[ind]['expenses']["stationery"] += exp.stationery
            # if exp.stationery > 0:
            #     print(meeting.meeting_no, 'has a non-zero stationery expense')
            fin_summaries[ind]['expenses']["altar"] += exp.altar
            # print('Exp others', exp.others)
            if exp.others.get('purpose'): # type: ignore
                fin_summaries[ind]['expenses']["others"].append(
                        {exp.others.get('purpose'): exp.others.get('value', 0)} # type:ignore
                    )

            # print('month', month, sbc) 
            # if month == 4: 
            #     print(f"\n {months[month-1]} sbc", sbc, fin_summaries[ind]['sbc'], fin_summaries[ind]['expenses'])

        # Get first acf
        # first_meeting = meetings_within_range[0]
        # first_acf = first_meeting.

        processed_data = {
            'last_submission_date': last_submission_date, 
            'report_number': report_number, 
            'no_curia_meetings_held': no_curia_meetings_held, 
            'no_praesidium_meetings_held': no_praesidium_meetings_held, 
            'no_curia_meetings_held_previous': no_curia_meetings_held_previous, 
            'no_praesidium_meetings_held_previous': no_praesidium_meetings_held_previous, 
            'officers_curia_attendance': officers_curia_attendance, 
            'officers_meeting_attendance': officers_meeting_attendance, 
            'no_meetings_expected': no_of_meetings_expected, 
            'no_meetings_held': no_of_meetings_held, 
            'avg_attendance': average_attendance, 
            'work_summaries': work_summaries, 
            'financial_summary': fin_summaries 
        }

        # print("\nProcessed data")
        # print('\n', processed_data['financial_summary'])

        serializer = ReportPrepGetSerializer(processed_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GenerateReportView(APIView):
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):

    # def generate_report_view(request):
        # print(request.POST.get('pid'), request.method, dir(request))
        pid = request.data.get('pid')
        praesidium = Praesidium.objects.get(id=pid) 
        praesidium_dict = PraesidiumSerializer(praesidium).data 
        cid = request.data.get('cid')
        curia = Curia.objects.get(id=cid) 
        curia_dict = CuriaSerializer(curia).data
        rid = request.data.get('rid')
        report = Report.objects.get(id=rid) 
        report_dict = ReportSerializer(report).data

        membership = request.data.get('membership')
        financial_summary = request.data.get('financial_summary') 
        work_summary = request.data.get('work_summary'), 
        fxn_attendances = request.data.get('fxn_attendances')

        # Extend report features
        # Membership details
        report_dict['membership'] = membership
        # Financial summary 
        report_dict['financial_summary'] = financial_summary
        # Function attendance 
        report_dict['fxn_attendances'] = fxn_attendances
        # Work summary
        # print('\n', work_summary, '\n')
        report_dict['work_summary'] = work_summary[0]

        # print('Curia')  http://localhost:5173/praesidium/2/report/19/[object%20Object]
        # pprint(curia_dict) 
        # print('Praesidium')
        # pprint(praesidium_dict)
        # print('Report works')
        # pprint(report_dict['work_summary'])

        # Get the file path 
        document, file_path = generate_report_docx(curia_dict, praesidium_dict, report_dict)
        doc_name = f'Report {report.report_number} of {praesidium.name}.docx'

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename={doc_name}'
        document.save(response)

        return response

        # # Serve the file as a response 
        # return FileResponse(
        #     open(file_path, 'rb'), as_attachment=True, filename='Legion_Report.docx'
        # )

