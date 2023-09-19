from django.shortcuts import render
from django.http import HttpResponse
from django.urls import is_valid_path

from collegeapp.forms import AdmissionForm
from .models import Departments,Admission

# Create your views here.
def index(request):
    return render(request,"index.html")


def aboutus(request):
    return render(request,"aboutus.html")

def departments(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request,"departments.html",dict_dept)

def admission(request):
    if request.method=="POST":
        form=AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html') 
    form=AdmissionForm()
    dict_form={
        'form':form
    }
    return render(request,"admission.html",dict_form)

def placement(request):
    return render(request,"placement.html")

def contactus(request):
    return render(request,"contactus.html")