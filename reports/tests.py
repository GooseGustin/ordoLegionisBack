from django.test import TestCase
from .models import *
from curia.models import Curia 
from random import randint, shuffle 
from datetime import date 

# Create your tests here
def getIden(name):
    letters = [i[0] for i in name.split(' ')]
    pepper = [str(randint(0,50)) for _ in range(3)]
    letters.extend(pepper) 
    shuffle(letters)
    letters = ''.join(letters)
    return letters


class ReportTest(TestCase):
    def setUp(self):
        self.curia = Curia.objects.create(
            name='Our Lady Queen of Mercy', 
            state='Plateau', 
            parish="St. Gabriel's", 
            spiritual_director="Fr. Gabriel"
        )
        praes_name = 'Our Lady Help of the Sick'
        self.p1 = Praesidium.objects.create(
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


    def test_create_report(self):
        sub_date = date(2025, 4, 13)
        last_sub_date = date(2024, 4, 16)
        rep = Report.objects.create(
            praesidium=self.p1, 
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

        # test model 
        self.assertEqual(rep.praesidium, self.p1) 
        self.assertEqual(rep.no_meetings_expected, 52)
        
        self.assertGreaterEqual(rep.submission_date, rep.last_submission_date)

        # test relationship
        self.assertEqual(self.curia, rep.praesidium.curia) 

    def test_create_function_attendance(self):
        sub_date = date(2025, 4, 13)
        last_sub_date = date(2024, 4, 16)
        rep = Report.objects.create(
            praesidium=self.p1, 
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

        fa = FunctionAttendance.objects.create(
            report=rep, 
            name='Acies', 
            date=date(2024, 10, 15), 
            current_year_attendance=3, 
            previous_year_attendance=5
        )

        self.assertEqual(fa.name, 'Acies')
        self.assertTrue(fa.report==rep)

    def test_create_membership_details_and_achievement(self):
        sub_date = date(2025, 4, 13)
        last_sub_date = date(2024, 4, 16)
        rep = Report.objects.create(
            praesidium=self.p1, 
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

        ma = MembershipDetails.objects.create(
            report=rep, 
            senior_praesidia=0, 
            junior_praesidia=0, 
            active_members=10, 
            probationary_members=3, 
            auxiliary_members=3, 
            adjutorian_members=0, 
            praetorian_members=0
        )

        self.assertEqual(ma.report, rep) 
        self.assertGreater(ma.active_members, ma.praetorian_members)

        ach = Achievement.objects.create(
            report=rep, 
            no_recruited=3, 
            no_baptized=0, 
            no_confirmed=3, 
            no_first_communicants=0, 
        )

        self.assertEqual(ach.report,rep)
        self.assertEqual(ach.no_baptized, 0) 
