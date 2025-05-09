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


    def test_create_meeting(self):
        meet = Meeting.objects.create(
            date=date(2024, 3, 2), 
            praesidium=self.p1, 
            no_present=13, 
            officers_meeting_attendance=[
                'president', 'treasurer', 'secretary'],
            officers_curia_attendance=[
                'president', 'vice_president', 'treasurer'
            ]
        )

        # test model 
        self.assertEqual(meet.praesidium, self.p1) 
        self.assertEqual(meet.no_present, 13)
        
        praesidium_inaug = self.p1.inaug_date
        self.assertGreaterEqual(meet.date, praesidium_inaug)

        # test relationship
        self.assertEqual(self.curia, meet.praesidium.curia) 