from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(Post)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(PostFlag)
admin.site.register(AnswerFlag)
admin.site.register(CommentFlag)
admin.site.register(QuestionFlag)
admin.site.register(PrayerRequest)
admin.site.register(PrayerRequestFlag)