from distutils.command.upload import upload
from re import M
from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()
    dep_image=models.ImageField(upload_to='departments')

    def __str__(self):
        return self.dep_name + self.dep_description


class Admission(models.Model):
    p_name=models.CharField(max_length=255)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    obt_marks=models.PositiveIntegerField()

    
    

    