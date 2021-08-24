from django.contrib import admin
from .models import ReceivedMessage


class ReceivedMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'date_sent',)

admin.site.register(ReceivedMessage, ReceivedMessageAdmin)
