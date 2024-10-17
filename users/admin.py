from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import StudentProfile
from .models import AgentProfile

User = get_user_model()

admin.site.register(User)
admin.site.register(StudentProfile)
admin.site.register(AgentProfile)



