from django.db import models
from accounts.models import Legionary

# Create your models here.
'''
Question: 
    - content
    - legionary
    - flags

Answer: 
    - content
    - legionary
    - question
    - upvote
    - downvote
    - flags

Post: 
    - title
    - content
    - image
    - legionary
    - upvote
    - downvote
    - flags

'''

class Question(models.Model):
    legionary = models.ForeignKey(Legionary, on_delete=models.CASCADE, related_name="questions")
    creator_name = models.CharField(max_length=200, blank=False)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    legionary = models.ForeignKey(Legionary, on_delete=models.CASCADE, related_name="answers")
    creator_name = models.CharField(max_length=200, blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to="images/posts/", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    legionary = models.ForeignKey(Legionary, on_delete=models.CASCADE, related_name="posts")
    creator_name = models.CharField(max_length=200, blank=False)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

class Comment(models.Model):
    legionary = models.ForeignKey(Legionary, on_delete=models.CASCADE, related_name="comments")
    creator_name = models.CharField(max_length=200, blank=False)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    date = models.DateTimeField(auto_now_add=True)

class PrayerRequest(models.Model):
    legionary = models.ForeignKey(Legionary, on_delete=models.CASCADE, related_name="prayer_requests")
    creator_name = models.CharField(max_length=200, blank=False)
    content = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

flag_choices = [
    ('not relevant', 'Not relevant'), 
    ('false', 'False'),
    ('incorrect', 'Incorrect'),
    ('inappropriate', 'Inappropriate'),
    ('sexually explicit', 'Sexually explicit'),
    ('other', 'Other')
]

class QuestionFlag(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='flags')
    reason = models.CharField(max_length=100, choices=flag_choices)

class AnswerFlag(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='flags')
    reason = models.CharField(max_length=100, choices=flag_choices)

class PostFlag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='flags')
    reason = models.CharField(max_length=100, choices=flag_choices)

class CommentFlag(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='flags')
    reason = models.CharField(max_length=100, choices=flag_choices)

class PrayerRequestFlag(models.Model):
    request = models.ForeignKey(PrayerRequest, on_delete=models.CASCADE, related_name='flags')
    reason = models.CharField(max_length=100, choices=flag_choices)

# class 
