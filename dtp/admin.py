from django.contrib import admin

# Register your models here.

from .models import Doctor, Examination

admin.site.register(Doctor)
admin.site.register(Examination)
