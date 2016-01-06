from django.db import models



class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    office = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField()





class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()


class Course(models.Model):
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=6)
    classroom = models.CharField(max_length=6)
    times= models.CharField(max_length=10)
    teacher=models.ForeignKey(Teacher, null=True)
    student=models.ManyToManyField(Student, null = True)
# Create your models here.
