from django.test import TestCase
from .models import *
from curia.models import Curia 
from accounts.models import Legionary, User
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


class PraesidiumTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='Gamer', password='passG#me123'
        )
        self.leg1 = Legionary.objects.create(
            user=self.user1, 
            status='non-manager',
        )
        self.user2 = User.objects.create_user(
            username='Gamer2', password='passG#me123'
        )
        self.leg2 = Legionary.objects.create(
            user=self.user2, 
            status='non-manager',
        )
        self.curia = Curia.objects.create(
            name='Our Lady Queen of Mercy', 
            state='Plateau', 
            parish="St. Gabriel's", 
            spiritual_director="Fr. Gabriel"
        )

    def test_create_praesidium(self):
        praes_name = 'Our Lady Help of the Sick'
        p1 = Praesidium.objects.create(
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
        p1.managers.add(self.leg1)
        p1.managers.add(self.leg2) 

        # test model 
        self.assertEqual(p1.name, praes_name)
        self.assertNotEqual(p1.iden, getIden(praes_name))
        self.assertCountEqual(p1.managers.all(), [self.leg1, self.leg2])

        # test rel
        self.assertEqual(p1.curia, self.curia)
        self.assertIn(self.leg1, p1.managers.all())

    def test_create_reminder(self):
        praes_name = 'Our Lady Help of the Sick'
        p1 = Praesidium.objects.create(
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
        
        rem = Reminder.objects.create(
            praesidium=p1, 
            content="Perform quarterly auditing",
            deadline=date(2025, 10, 5)
        )
        today = date.today()

        self.assertEqual(rem.praesidium, p1) 
        self.assertGreater(rem.deadline, today)