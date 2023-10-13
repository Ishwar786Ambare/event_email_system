from django.contrib import admin

from events.models import EmailLog, Employee

# Register your models here.

admin.site.register(EmailLog)
admin.site.register(Employee)
