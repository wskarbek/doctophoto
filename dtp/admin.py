from django.contrib import admin

# Register your models here.

from .models import Doctor, Examination, ExaminationPhoto

admin.site.register(Doctor)
admin.site.register(Examination)
admin.site.register(ExaminationPhoto)
