from django.contrib import admin
from .models import Departments,Admission

# Register your models here.
admin.site.register(Departments)

class AdmissionAdmin(admin.ModelAdmin):
    list_display=('p_name','p_phone','p_email','obt_marks')
admin.site.register(Admission,AdmissionAdmin)

