from django.contrib import admin
from appOne.models import Feedback, UserProfile, TeacherProfile, Subject

admin.site.register(Feedback)
admin.site.register(UserProfile)
admin.site.register(TeacherProfile)
admin.site.register(Subject)
