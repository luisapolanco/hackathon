from ast import Raise
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# class UserManager(BaseUserManager):
#     def _create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError('Debes ingresar un correo electronico institucional')
#         user = self.model(
#             email = email, 
#             username = email
#         )
#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_user(self, email, password):
#         return self._create_user(email, password)
    
#     def create_superuser(self, email, password):
#         user = self._create_user(email, password )
#         user.admin_user = True
#         user.save()

#         return user
    
# Create your models here.
class Teacher(AbstractBaseUser):
    id = models.BigAutoField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)


class Monitor(AbstractBaseUser):
    id = models.BigAutoField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)

class Course(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    # id_teacher = models.ForeignKey(Teacher, to_field='id', null=False, blank=False, on_delete=models.CASCADE)
    # id_monitor = models.ForeignKey(Monitor, to_field='id', null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)  


class Student(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    id_course = models.ForeignKey(Course,  to_field='id', null=False, blank=False, on_delete=models.CASCADE, default='111')

   
        
class TestLost(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40)
    id_course = models.ForeignKey(Course, to_field='id', null=False, blank=False, on_delete=models.CASCADE)

class Site(models.Model):
    id = models.BigAutoField(primary_key=True)
    nameSite = models.CharField(max_length=140)
    capacity = models.IntegerField()

class Supplementary(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_student = models.ForeignKey(Student, to_field='id', null=False, blank=False, on_delete=models.CASCADE)
    id_course = models.ForeignKey(Course, to_field='id', null=False, blank=False, on_delete=models.CASCADE, default='1111')
    workshop = models.BooleanField(default=False)
    monitoring = models.BooleanField(default=False)
    id_sitio = models.ForeignKey(Site, to_field='id', null=True, blank=True, on_delete=models.DO_NOTHING)
    supplementaryDate = models.DateTimeField()

    

    