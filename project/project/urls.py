#asg4
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^addstudent/$',"app.views.addstudent"),
    url(r'^all-students/$',"app.views.all_students"),

    url(r'^addteacher/$',"app.views.addteacher"),
    url(r'^all-teachers/$',"app.views.all_teachers"),

    url(r'^addcourse/$',"app.views.addcourse"),
    url(r'^all-courses/$',"app.views.all_courses"),

    url(r'^select_course/$',"app.views.select_course"),
    url(r'^all_course_student/(.*)/$',"app.views.all_course_student"),
]
