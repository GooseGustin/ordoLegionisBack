from django.test import TestCase
from .models import *
from praesidium.models import Praesidium
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


class MeetingTest(TestCase):
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

        self.meet = Meeting.objects.create(
            date=date(2024, 3, 2), 
            praesidium=self.p1, 
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

    def test_create_account_statement_and_announcement(self):
        exp1 = Expenses.objects.create(
            extension=200.0, 
            remittance=2000, 
            stationery=0, 
            altar=50, 
            bouquet=0, 
        )

        acct_stat = AcctStatement.objects.create(
            acf=2500, sbc=150, expenses=exp1, balance=400
        )
        def totalExpenses(exp):
            total = exp.extension + exp.remittance + exp.stationery + exp.altar + exp.bouquet + sum(exp.others.values())
            return total
        exp_total = totalExpenses(exp1)

        acct_ann = AcctAnnouncement.objects.create(
            sbc=200, 
            collection_1 = 150, 
            collection_2 = 200
        )

        # test model 
        self.assertGreaterEqual(acct_stat.acf+acct_stat.sbc, acct_stat.balance)
        self.assertEqual(acct_stat.acf+acct_stat.sbc-exp_total, acct_stat.balance)
        self.assertEqual(acct_ann.sbc, 200)

        # test relationship
        self.assertEqual(acct_stat.expenses, exp1) 

    def test_create_financial_record_and_summary(self):
        exp2 = Expenses.objects.create(
            extension=1000.0, 
            remittance=200, 
            stationery=50, 
            altar=0, 
        )
        acct_stat = AcctStatement.objects.create(
            acf=2500, sbc=150, expenses=exp2, balance=1400
        )
        def totalExpenses(exp):
            total = exp.extension + exp.remittance + exp.stationery + exp.altar + exp.bouquet + sum(exp.others.values())
            return total

        exp_total = totalExpenses(exp2)

        acct_ann = AcctAnnouncement.objects.create(
            sbc=200, collection_1 = 150, collection_2 = 200
        )

        fin_rec = FinancialRecord.objects.create(
            meeting=self.meet, 
            acct_statement=acct_stat, 
            acct_announcement=acct_ann
        )

        # test model 
        self.assertGreaterEqual(fin_rec.acct_statement.acf+fin_rec.acct_statement.sbc, fin_rec.acct_statement.balance)
        self.assertEqual(fin_rec.acct_statement.acf+fin_rec.acct_statement.sbc-exp_total, fin_rec.acct_statement.balance)
        self.assertEqual(fin_rec.acct_announcement.sbc, 200)

        # test relationship
        self.assertEqual(fin_rec.acct_statement.expenses, exp2) 
        print('Meeting date:', fin_rec.meeting.date)
        print('Officers present:', *fin_rec.meeting.officers_meeting_attendance)
        self.assertEqual(fin_rec.meeting.praesidium.name, 'Our Lady Help of the Sick')
        self.assertEqual(fin_rec.acct_announcement.sbc, 200)
        
        all_exp = {
            'jan': {
                'extension':1000.0, 
                'remittance':200, 
                'stationery':50, 
                'altar':0, 
                'others': {
                    'Edel Quinn Mass': 300, 
                },
            }, 
            'feb': {
                'extension':1000.0, 
                'remittance':200, 
                'stationery':50, 
                'bouquet':30, 
            }, 
            'mar': {
                'extension':1000.0, 
                'remittance':200, 
                'stationery':50, 
                'others': {
                    'Mary\'s birthday celebration': 300, 
                }, 
            }, 
        }
        def getExpensesTotals(monthly_exp):
            expenses = {
                'extension': 0,
                'remittance': 0,
                'stationery': 0,
                'bouquet': 0,
                'altar': 0,
                'others': 0
            }
            
            for month in monthly_exp: 
                for exp in monthly_exp[month]:
                    if exp == 'others': 
                        expenses[exp] += sum(monthly_exp[month][exp].values()) 
                    else: 
                        expenses[exp] += monthly_exp[month][exp]
                    
            return expenses

        expenses_total = getExpensesTotals(all_exp) 
        print('Expenses summary:', expenses_total)

        fin_summary = FinancialSummary.objects.create(
            report = self.report,
            abf = 1100, 
            sbc = 25500, 
            expenses = all_exp, 
            report_production = 350
        )

        self.assertEqual(fin_summary.sbc, 25500), 
        self.assertEqual(fin_summary.expenses['jan']['extension'], 1000.0)
        print(fin_summary.report.report_number)
        self.assertEqual(fin_summary.report.praesidium, self.p1)


