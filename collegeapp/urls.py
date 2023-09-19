from django import views
from django.urls import path,include
from . import views

urlpatterns = [
    path ('',views.index, name='home'),
    path('aboutus',views.aboutus, name='aboutus'),
    path('departments',views.departments, name='departments'),
    path('admission',views.admission, name='admission'),
    path('placement',views.placement, name='placement'),
    path('contactus',views.contactus, name='contactus'),
]