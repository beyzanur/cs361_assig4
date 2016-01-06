#assigment3
from django import forms
from app.models import *


class TeacherForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    office = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=12)
    email = forms.EmailField()


class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()

class CourseForm(forms.Form):
    name = forms.CharField(max_length=10)
    code = forms.CharField(max_length=6)
    classroom = forms.CharField(max_length=6)
    times= forms.CharField(max_length=10)

courses = [(course.name,course.name) for course in Course.objects.all()]

students = [(student.first_name,student.first_name) for student in Student.objects.all()]

class EnrollForm(forms.Form):
    courses = forms.ChoiceField(courses, required=False,widget=forms.Select())
    students =forms.ChoiceField(students,required=False,widget=forms.Select())
