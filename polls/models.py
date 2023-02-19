from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    school_id = models.CharField(max_length=200)