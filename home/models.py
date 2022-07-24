from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    outstanding_fees = models.IntegerField()
    is_indebted = models.BooleanField(default='false')
    is_contending_debt = models.BooleanField(default='false')

    def __str__(self):
        return self.first_name + self.last_name

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default='false')
    is_school_admin = models.BooleanField(default='false')
    is_visitor = models.BooleanField(default='false')
    school_name = models.CharField(max_length=100, null=True, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.comment[:10]
