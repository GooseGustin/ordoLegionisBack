from django.test import TestCase
from .models import Curia, Announcement
from datetime import date 
from django.core.files.images import ImageFile 
# Create your tests here.

class CuriaTestCase(TestCase):

    def test_create_curia(self):
        curia = Curia.objects.create(
            name='Our Lady Queen of Mercy', 
            state='Plateau', 
            parish="St. Gabriel's", 
            spiritual_director="Fr. Gabriel"
        )

        # test model 
        self.assertIsNotNone(Curia.objects.all())
        self.assertEqual(curia.state, 'Plateau')

    def test_create_announcement(self):
        curia = Curia.objects.create(
            name='Our Lady Queen of Mercy', 
            state='Plateau', 
            parish="St. Gabriel's", 
            spiritual_director="Fr. Gabriel"
        )
        with open('C:/users/badungs/pictures/HERCULES.jpg', 'rb') as f:
            agr_img = ImageFile(f, name='herc.jpg')
            ann = Announcement(
                date = date(2020, 12, 15), 
                title='Annual General Reunion', 
                body="Get ready for it. It's gonna be lit!!", 
                image=agr_img, 
                curia=curia
            )
            ann.save()
            
        self.assertEqual(ann.title, "Annual General Reunion")
        self.assertTrue(ann.curia == curia)


# class Announcement(models.Model):
#     date = models.DateField(auto_now_add=True)
#     title = models.CharField(max_length=100)
#     body = models.TextField()
#     image = models.ImageField(upload_to='images/curia/')

#     def __str__(self):
#         return self.name[:20]