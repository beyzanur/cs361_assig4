
#asg4
from django.shortcuts import render
from django.shortcuts import HttpResponse
from project.settings import *
from django.shortcuts import render_to_response
from app.models import *

from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.template import Context

import datetime
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext
from app.forms import *

def addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            a = Student(first_name=form.cleaned_data["first_name"],
                       last_name=form.cleaned_data["last_name"],
                       email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-students/')
    else:
        form = StudentForm()
    return render_to_response('addstudent.html', {'form': form},
                              RequestContext(request))
def all_students(request):
    return render_to_response('all_students.html',
                              {'student_list': Student.objects.all()})

def addteacher(request):
    if request.method=="POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            a = Teacher(first_name=form.cleaned_data["first_name"],last_name=form.cleaned_data["last_name"],
                        office=form.cleaned_data["office"],phone=form.cleaned_data["phone"],
                        email=form.cleaned_data["email"] )
            a.save()
            return HttpResponseRedirect("/all-teachers/")
    else:
        form=TeacherForm()
    return render_to_response("addteachers.html",
                              {"form":form},RequestContext(request))

def all_teachers(request):
    return render_to_response("all_teachers.html",
                              {"teacher_list":Teacher.objects.all()})

def addcourse(request):
   if request.method=="POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            a = Course(name=form.cleaned_data["name"],code=form.cleaned_data["code"],
                       classroom=form.cleaned_data["classroom"],times=form.cleaned_data["times"])
            a.save()
            return HttpResponseRedirect("/all-courses/")
   else:
       form=CourseForm()
   return  render_to_response("addcourses.html",
                              {"form":form},RequestContext(request))

def all_courses(request):
    return render_to_response("all_courses.html",
                              {"course_list":Course.objects.all()})

def select_course(request):
    if request.method=="POST":
        form = EnrollForm(request.POST)
        if form.is_valid():
            print form.cleaned_data["students"]
            studentname = Student.objects.get(first_name=form.cleaned_data["students"])

            coursename= Course.objects.get(name=form.cleaned_data["courses"])
            coursename.student.add( studentname)
            return HttpResponseRedirect("/all_course_student/"+form.cleaned_data["courses"])

    form=EnrollForm()
    return render_to_response("addcourses_students.html",
                              {"form":form},RequestContext(request))

def all_course_student(request,a):
    c = Course.objects.get(name=a)
    return render_to_response("all_course_student.html",
                              {"course_student_list":c.student.all()})

# Create your views here.
