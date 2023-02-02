"""stdproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from stdapplications import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.schl,name='school'),
    path('adm',views.pri,name='admin'),
    path('hodd',views.hodd,name='hod'),
    path('techer',views.tech,name='teacher'),
    path('stdd',views.stdd,name='studentt'),
    path('logg',views.log,name='login'),
    path('hod',views.hod,name='HOD'),
    path("add",views.add,name="add"),
    path('viewsh',views.viewsh,name='view'),
    path('techre',views.techre,name='techre'),
    path('add2',views.add2,name='add2'),
    path('viewst',views.viewst,name='viewstt'),
    path('student',views.student,name='student'),
    path('add3',views.add3,name='add3'),
    path('viewstudents',views.viewstudents,name='viewstudents'),
    path('adminhod',views.adminhod,name='adminhod'),
    path('adminstudent',views.adminstudent,name='adminstudent'),
    path('adminteacher',views.adminteacher,name='adminteacher'),
    path('delete/<int:dele>',views.delete,name='delete'),
    path('formupdate/<int:con>',views.formupdate,name='formupdate'),
    path('deletehod/<int:hoddel>',views.deletehod,name='deletehod'),
    path('formupdatehod/<int:formhod>',views.formupdatehod,name='formupdatehod'),
    path('deletestu/<int:delstu>',views.deletestu,name='deletest'),
    path('formstudent/<int:formstu>',views.formstudent,name='formstudent'),
    path('approve_teacher/<int:teacher_id>',views.approve_teacher,name='approve_teacher'),
    path('approve_student/<int:student_id>',views.approve_student,name='approve_student'),
    path('aprovete',views.aprovete,name='aprovete'),
    path('aprovestud',views.aprovestud,name='aprovestud'),
    path('login',views.login,name='loginn'),
    path('profilehod',views.profilehod,name='profilehod'),
    path('profilestudents',views.profilestudents,name='profilestudents'),
    path('profileteachers',views.profileteachers,name='profileteachers'),
    path('edit/<int:ed>',views.edit,name='edit'),
    path('<int:con>/formadmin',views.formadmin,name='formadmin'),
    path('editst/<int:edst>',views.editst,name='editst'),
    path('<int:frmst>/formstud',views.formstud,name='formstud'),
    path('editte/<int:edte>',views.editte,name='editte'),
    path('<int:frmtech>/formteach',views.formteach,name='formteach'),
    path('leavehoodd',views.leavehoodd,name='leavehoodd'),
    path('reqhod',views.reqhod,name='reqhod'),
    path('leaveteacher',views.leaveteacher,name='leaveteacher'),
    path('reqteacher',views.reqteacher,name='reqteacher'),
    path('leavestudent',views.leavestudent,name='leavestudent'),
    path('reqstud',views.reqstud,name='reqstud'),
    # path('viewall',views.viewall,name='viewall'),
    path('viewsleavehod',views.viewsleavehod,name='viewsleavehod'),
    path('deleteleavehod/<int:leaa>',views.deleteleavehod,name='deleteleavehod'),
    path('formupdateleave/<int:leav>',views.formupdateleave,name='formupdateleave'),
    # path('reapp',view.reapp,name='reapp'),
    path('approve_LEAVE/<int:leave_id>',views.approve_LEAVE,name='approve_LEAVE'),
    path('viewsleaveteacher',views.viewsleaveteacher,name='viewsleaveteacher'),
    path('deleteleaveteacher/int:leate>',views.deleteleaveteacher,name='deleteleaveteacher'),
    path('formupdateleavete/int:leavte>',views.formupdateleavete,name='formupdateleavete'),
    path('approve_teacher_leave/<int:leave_idteacher>',views.approve_teacher_leave,name='approve_teacher_leave'),
    path('viewsleavestudent',views.viewsleavestudent,name='viewsleavestudent'),
    path('deleteleavestudent/int:least>',views.deleteleavestudent,name='deleteleavestudent'),
    path(' approve_student_leave/int:leave_idstudent>',views. approve_student_leave,name=' approve_student_leave'),
    path('examlist',views.examlist,name='examlist'),
    path('examstd',views.examstd,name='examstd'),
    path('examlistsview',views.examlistsview,name='examlistsview'),
    path('hodviewexam',views.hodviewexam,name='hodviewexam'),
    path('deleteexam/<int:delexam>',views.deleteexam,name='deleteexam'),
    path('formupdateexam/<int:delexamlist>',views.formupdateexam,name='formupdateexam'),
    path('stdnotification',views.stdnotification,name='stdnotification'),
    path('approve_student_exam/<int:exam_idstudent>',views.approve_student_exam,name='approve_student_exam'),
    path('marks',views.marks,name='marks'),
    path('publish',views.publish,name='publish'),
    path('publishview',views.publishview,name='publishview'),
    path('publishmarkview',views.publishmarkview,name='publishmarkview'),

]

