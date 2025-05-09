from django.test import TestCase
from .models import *
from meetings.models import Meeting
from praesidium.models import Praesidium
from reports.models import Report 
from random import randint, shuffle
from datetime import date 
from curia.models import Curia 

def getIden(name):
    letters = [i[0] for i in name.split(" ")]
    pepper = [str(randint(0,50)) for _ in range(3)]
    letters.extend(pepper) 
    shuffle(letters)
    letters = ''.join(letters)
    return letters

class WorkTest(TestCase):
    def setUp(self):
        self.curia = Curia.objects.create(
            name='Our Lady Queen of Mercy', 
            state='Plateau', 
            parish="St. Gabriel's", 
            spiritual_director="Fr. Gabriel"
        )
        
        praes_name = 'Our Lady Help of the Sick'
        self.praes = Praesidium.objects.create(
            name=praes_name, 
            state='Plateau', 
            parish="St. Michael's", 
            curia=self.curia, 
            iden=getIden(praes_name), 
            address="St. Michael's parish hall", 
            meeting_time="After Sunday morning mass", 
            inaug_date=date(2020, 12, 15), 
            president = "Malachi", 
            pres_app_date = date(2020, 12, 15),
            vice_president = "Justin", 
            vp_app_date = date(2020, 12, 16), 
            secretary = "Joan", 
            sec_app_date = date(2020, 12, 15), 
            treasurer = "Philippa", 
            tres_app_date = date(2020, 12, 15)
        )

        self.meet = Meeting.objects.create(
            date=date(2024, 3, 2), 
            praesidium=self.praes, 
            no_present=13, 
            officers_meeting_attendance=[
                'president', 'treasurer', 'secretary'],
            officers_curia_attendance=[
                'president', 'vice_president', 'treasurer'
            ]
        )
        
        sub_date = date(2025, 4, 13)
        last_sub_date = date(2024, 4, 16)
        self.report = Report.objects.create(
            praesidium=self.praes, 
            submission_date=sub_date, 
            last_submission_date=last_sub_date, 
            report_number=3, 
            report_period=(sub_date-last_sub_date).days,
            last_curia_visit_date=date(2023, 12, 2), 
            last_curia_visitors=[
                'Bro Julius Pwajok',
            ],
            officers_curia_attendance={
                'president': 11, 
                'secretary': 12, 
                'vice president': 10, 
                'treasurer': 6
            },
            officers_meeting_attendance={
                'president': 44, 
                'secretary': 20, 
                'vice president': 50, 
                'treasurer': 33
            },
            extension_plans = '''
            To try to recruit more members by attending 
            closely to lapsed members''', 
            # problems = '',
            # remarks = '', 
            no_meetings_expected=52, 
            no_meetings_held=52, 
            avg_attendance=5, 
            poor_attendance_reason='poverty'

        )

    def test_create_work(self):
        w1 = Work.objects.create(
            type="Home visitation", 
            active=True, 
            done=True, 
            details={
                "No of people visited": 13, 
                "No of active Catholics": 7, 
                "No of inactive Catholics": 2, 
                "No of separated brethren": 4, 
                "No of catechumen": 0, 
                "No of muslims": 0, 
                "No of unknowns": 0
            }, 
            meeting=self.meet
        )

        # print(dir(self.meet.works)) , 
        print('All meet\'s works', self.meet.works.all())
        # self.assertEqual(w1, self.meet.works)
        self.assertEqual(w1.meeting.praesidium, self.praes)
        self.assertEqual(w1.details['No of muslims'], 0)
        self.assertTrue(w1.active) 
        self.assertEqual(self.meet.works.all()[0], w1)

    def test_create_work_list(self):
        wl1 = WorkList.objects.create(
            praesidium=self.praes, 
            details = {
                "Home visitation": [
                    "No of homes visited", 
                    "No of active Catholics", 
                    "No of inactive Catholics", 
                    "No of separated brethren", 
                    "No of catechumen", 
                    "No of muslims", 
                    "No of unknowns"
                ]
            }
        )
        self.assertEqual(wl1.praesidium, self.praes)
        self.assertIn("No of muslims", wl1.details["Home visitation"])
        # print(self.meet.works) /


    def test_create_work_summary(self):
        ws = WorkSummary.objects.create(
            report=self.report, 
            type="Home visitation", 
            active=True,
            no_assigned=20, 
            no_done=15, 
            details={
                "No of people visited": 3, 
                "No of active Catholics": 1, 
                "No of inactive Catholics": 0, 
                "No of separated brethren": 1, 
                "No of catechumen": 1, 
                "No of muslims": 0, 
                "No of unknowns": 0
            }
        )

        self.assertEqual(ws.report, self.report) 
        self.assertEqual(ws.details["No of people visited"], 3)
        self.assertTrue(ws.active) 
