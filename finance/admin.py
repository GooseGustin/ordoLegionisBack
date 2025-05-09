from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Expenses)
admin.site.register(AcctAnnouncement)
admin.site.register(AcctStatement)
admin.site.register(FinancialRecord)
admin.site.register(FinancialSummary)