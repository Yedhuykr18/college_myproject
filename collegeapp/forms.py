from django import forms
from .models import Admission

class AdmissionForm(forms.ModelForm):
    class Meta:
        model=Admission
        fields="__all__"
        
        labels={
            'p_name':"Name : ",
            'p_phone':"Phone : ",
            'p_email':"Email : ",
            'obt_marks':"12th obtained marks in Physics, Chemistry and Mathematics : "
        }