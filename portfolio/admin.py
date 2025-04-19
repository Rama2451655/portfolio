from django.contrib import admin
from .models import Project

admin.site.register(Project)
from .models import Skill, Education, Certificate

admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Certificate)
