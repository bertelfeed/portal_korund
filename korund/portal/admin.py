from django.contrib import admin
from .models import * # never use asterisk import

"""
Make use of Django Admin Models
See more: https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
"""

admin.site.register(Topic)
admin.site.register(Employee)
admin.site.register(Phone)
admin.site.register(News)
admin.site.register(File)
admin.site.register(Chat)
admin.site.register(ChatParticipant)
admin.site.register(Message)
admin.site.register(Education)
admin.site.register(ActivityLog)
admin.site.register(Notification)
admin.site.register(Event)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(DocumentArchive)
