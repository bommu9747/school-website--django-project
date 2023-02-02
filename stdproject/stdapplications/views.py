from django.shortcuts import render,redirect
from .models import admins
from .models import teacher
from .models import students
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .models import leave
from .models import viewexamlist
from .models import mark
from django.db.models import Q


# Create your views here.
def schl(request):
    return render(request,'index.html')
def pri(request):
    return render(request,'admin.html')

def hodd(request):
    return render(request,'hod.html')
def tech(request):
    return render(request,'teacher.html')
def stdd(request):
    return render(request,'student.html')
def log(request):
    return render(request,'login.html')
# def hod(request):
#     return render(request,'hodregister.html')
def hod(request):
    # data=admins.object.all()
    # data.save()
    # print(data)
    return render(request,'hodregister.html')
def add(request):
    if request.method=='POST':
        name=request.POST['name']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        department=request.POST['department']
        password=request.POST['password']
        conform=request.POST['conform']
        qualification=request.POST['qualification']
        years=request.POST['years']

        status='1'
        role ='hod'
         
        if password == conform:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('HOD')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('HOD')
            else:
                user=User.objects.create_user(
                    username=username,password=password)
                user.save()
                data=admins(user=user,name=name,lastname=lastname,username=username,email=email,phone=phone,department=department,password=password,conform=conform ,qualification=qualification,years=years,status=status,role=role)
                data.save()
                print(data)
        else:
            messages.info(request,'password is not matching')
            return redirect('HOD')
        return redirect('admin')
    else:

        # data=admins.object.all()
        # return render(request,'hodregister.html')
        return render(request,'hodregister.html')


def viewsh(request):
    # data1=admins.objects.all()
    dept=''
    sub=''
    hoduu=admins.objects.filter(role='hod').values()
    print( hoduu)
    for i in  hoduu:
        dept=i['department']
        # sub=i['subject']
    data1=admins.objects.filter(Q(department=dept))
        # print(i)
    

    return render(request,'viewhod.html',{'data':data1})

def techre(request):
    return render(request,'teachregistr.html')

def add2(request):
    if request.method=='POST':
        name=request.POST['name']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        department=request.POST['department']
        password=request.POST['password']
        conform=request.POST['conform']
        qualification=request.POST['qualification']
        years=request.POST['years']
        status='0'
        role ='teacher'

        if password == conform:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('techre')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('techre')
            else:
                user=User.objects.create_user(
                    username=username,password=password)
                user.save()
                data2=teacher(user=user,name=name,lastname=lastname,username=username,email=email,phone=phone,department=department,password=password,conform=conform ,qualification=qualification,years=years,status=status,role=role)
                data2.save()
                print(data2)
        else:
            messages.info(request,'password is not matching')
            return redirect('techre')
        return redirect('hod')
    else:
        # data=admins.object.all()

    #     return render(request,'techre')
    # else:
        return render(request,'teachregistr.html')


def viewst(request):
    # data5=teacher.objects.all()
    dept=''
    sub=''
    stuu=teacher.objects.filter(role='teacher').values()
    print(stuu)
    for i in stuu:
        dept=i['department']
        sub=i['subject']
        data5=teacher.objects.filter(Q(department=dept) & Q(subject=sub))
        print(i)
    return render(request,'viewtecher.html',{'data':data5})


    
def student(request):
    return render(request,'studentregi.html')

def add3(request):
    if request.method=='POST':
        name=request.POST['name']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        department=request.POST['department']
        password=request.POST['password']
        conform=request.POST['conform']
        years=request.POST['years']
        status='0'
        role ='student'
        if password == conform:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('student')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('student')
            else:
                user=User.objects.create_user(
                    username=username,password=password)
                user.save()
                data3=students(user=user,name=name,lastname=lastname,username=username,email=email,phone=phone,department=department,password=password,conform=conform,years=years,status=status,role=role)
                data3.save()
                print(data3)
        else:
            messages.info(request,'password is not matching')
            return redirect('student')
        return redirect('teacher')
    else:


        # return render(request,'studentregi.html')

        return render(request,'studentregi.html')
def viewstudents(request):
    #  if request.user:
    #     user=request.user
    #     data=teacher.objects.filter(role=role).values()
    #     print
    #     for i in data:
    #         dept=i['department']
    #         sub=i['subject']
    #     dataa=students.object.fillter(Q(department=dept)&Q(subject=sub))
    # return render(request,'viewstudent.html',{'data':dataaa})
    dept=''
    sub=''
    stu=students.objects.filter(role='student').values()
    print(stu)
    for i in stu:
        dept=i['department']
        # sub=i['subject']
        dataa=students.objects.filter(Q(department=dept))
        print(i)
    return render (request,'viewstudent.html',{'data':dataa})
 
def adminhod(request):
    admih=admins.objects.all()
    print(admih)
    return render(request,'adminhod.html',{'data':admih})
def adminstudent(request):
    adminstud=students.objects.all()
    print(adminstud)
    return render(request,'adminstudent.html',{'data':adminstud})
def adminteacher(request):
    admintea=teacher.objects.all()
    print(admintea)
    return render(request,'adminteacher.html',{'data':admintea})

def deletehod(request,hoddel):
    hodde=admins.objects.get(id=hoddel)
    hodde.delete()
    return redirect('adminhod')
def formupdatehod(request,formhod):
    if request.method=='POST':
        AAHOD=admins.objects.get(id=formhod)
        AAHOD= name=request.POST['name']
        AAHOD=lastname=request.POST['lastname']
        AAHOD=username=request.POST['username']
        AAHOD=email=request.POST['email']
        AAHOD=phone=request.POST['phone']
        AAHOD=department=request.POST['department']
        AAHOD=password=request.POST['password']
        AAHOD=conform=request.POST['conform']
        AAHOD=qualification=request.POST['qualification']
        AAHOD=years=request.POST['years']
        AAHOD.save()
    return redirect('adminhod')


def delete(request,dele):
    addD=teacher.objects.get(id=dele)
    addD.delete()
    return redirect('adminteacher')
def formupdate(request,con):
    if request.method=='POST':
        ADD=teacher.objects.get(id=con)
        ADD.name=request.POST['name']
        ADD.lastname=request.POST['lastname']
        ADD.username=request.POST['username']
        ADD.email=request.POST['email']
        ADD.phone=request.POST['phone']
        ADD.department=request.POST['department']
        ADD.password=request.POST['password']
        ADD.conform=request.POST['conform']
        ADD.qualification=request.POST['qualification']
        ADD.years=request.POST['years']

        ADD.save()
    return redirect('adminteacher')

def deletestu(request,delstu):
    delstuu=students.objects.get(id=delstu)
    delstuu.delete()
    return redirect('adminstudent')
def formstudent(request,formstu):
    if request.method=='POST':
        ST=students.objects.get(id=formstu)
        ST=name=request.POST['name']
        ST=lastname=request.POST['lastname']
        ST=username=request.POST['username']
        ST=email=request.POST['email']
        ST=phone=request.POST['phone']
        ST=department=request.POST['department']
        ST=password=request.POST['password']
        ST=conform=request.POST['conform']
        ST=years=request.POST['years']
        ST.save()
    return redirect('adminstudent')


def approve_teacher(request,teacher_id):
    teachers=teacher.objects.get(id=teacher_id)
    teachers.status='1'
    teachers.save()
    return redirect('aprovete')

def approve_student(request,student_id):
    studentt=students.objects.get(id=student_id)
    studentt.status='1'
    studentt.save()
    return redirect('aprovestud')
def aprovete(request):
    app=teacher.objects.all()
    return render(request,'aproveteacher.html',{'data':app})
def aprovestud(request):
    appstu=students.objects.all()
    return render(request,'aprovestudent.html',{'data':appstu})

#LOGIN
stat=''
rol=''
def login(request):
    global stat
    global rol
    global u_id

    if request.method=='POST':
        username=request.POST.get('username')
        print(username)
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        data=User.objects.filter(username=username).values()

        for i in data:
            user_name=i['username']
            print('username',user_name)

            id =i['id']
            u_id=id
            print('id',id)

            student_data=students.objects.filter(user_id=id).values()
            print('st-data',student_data)

            for i in student_data:
                stat=i['status']
                rol=i['role']
                 

                print('role',rol)
                print('status',stat)
            
            teacher_data=teacher.objects.filter(user_id=id).values()

            for i in teacher_data:
                stat=i['status']
                rol=i['role']
                print('role',rol)
                print('status',stat)
            
            hod_data=admins.objects.filter(user_id=id).values()
            for i in hod_data:
                stat=i['status']
                rol=i['role']
                print('role',rol)
                print('status',stat)

            if user is not None and rol == 'student' and username == user_name and stat=='1':
                auth_login(request,user)
                return redirect('studentt')
            elif user is not None and rol =='teacher' and username==user_name and stat=='1':
                auth_login(request,user)
                return redirect('teacher')
            elif user is not None and rol =='hod' and username==user_name and stat=='1':
                auth_login(request,user)
                return redirect('hod')
            elif username is not None and rol =='admin' and password =='admin123':
                print('user =',user)
                auth_login(request,user)
                return redirect('admin')
            else:
                pass
        else:
            messages.info(request,'invalid credential')
            return redirect('loginn')
    else:
        return render(request,'login.html')


def logout_profile(request):
    logout(request)
    return redirect('logn')
def profilehod(request):
    if request.user:
        user=request.user
        aing=admins.objects.filter(user=user)
        print(aing)
    return render(request,'profileadmin.html',{'data':aing})
def profilestudents(request):
    if request.user:
        user=request.user
        ding=students.objects.filter(user=user)
        print(ding)
    return render(request,'profilestudent.html',{'data':ding})
def profileteachers(request):
    if request.user:
        user=request.user
        sing=teacher.objects.filter(user=user)
        print(sing)
    return render(request,'profileteacher.html',{'data':sing})

def edit(request,ed):
    data=admins.objects.get(id=ed)
    return render(request,'editadmin.html',{'data':data})

def formadmin(request,con):
    if request.method=='POST':
        AAHODD=admins.objects.get(id=con)
        AAHODD.name=request.POST['name']
        AAHODD.lastname=request.POST['lastname']
        AAHODD.username=request.POST['username']
        AAHODD.email=request.POST['email']
        AAHODD.phone=request.POST['phone']
        AAHODD.department=request.POST['department']
        AAHODD.password=request.POST['password']
        AAHODD.conform=request.POST['conform']
        AAHODD.qualification=request.POST['qualification']
        AAHODD.years=request.POST['years']
        AAHODD.save()
    # return render(request,'profileadmin.html',{'data':AAHODD})
    return redirect('profilehod')

def editst(request,edst):
    dataas=students.objects.get(id=edst)
    return render(request,'editstudent.html',{'data':dataas})
def formstud(request,frmst):
    if request.method=='POST':
       
        ST=students.objects.get(id=frmst)
        ST.name=request.POST['name']
        ST.lastname=request.POST['lastname']
        ST.username=request.POST['username']
        ST.email=request.POST['email']
        ST.phone=request.POST['phone']
        ST.department=request.POST['department']
        ST.password=request.POST['password']
        ST.conform=request.POST['conform']
        ST.years=request.POST['years']
        ST.save()
    return redirect('profilestudents')
def editte(request,edte):
    dataass=teacher.objects.get(id=edte)
    return render(request,'editteacher.html',{'data':dataass})
def formteach(request,frmtech):
    if request.method=='POST':
        ADD=teacher.objects.get(id=frmtech)
        ADD.name=request.POST['name']
        ADD.lastname=request.POST['lastname']
        ADD.username=request.POST['username']
        ADD.email=request.POST['email']
        ADD.phone=request.POST['phone']
        ADD.department=request.POST['department']
        ADD.password=request.POST['password']
        ADD.conform=request.POST['conform']
        ADD.qualification=request.POST['qualification']
        ADD.years=request.POST['years']

        ADD.save()
    return redirect('profileteachers')
  

def leavehoodd(request):
    return render(request,'leavehod.html')

def reqhod(request):
    if request.method:
        user=request.user
    if request.method=='POST':
        user=request.user
        name=request.POST['name']
        department=request.POST['department']
        date=request.POST['date']
        reason=request.POST['reasons']
        role=request.POST['role']
        status='0'
     
        datta=leave(user=user,name=name,date=date, department=department,reason=reason,status=status,role=role)
        datta.save()
       
        return render(request,'hod.html')
    else:
        return render(request,'hod.html')




def leaveteacher(request):
    return render(request,'leaveteacher.html')

def reqteacher(request):
    if request.method:
        user=request.user
    if request.method=='POST':
        user=request.user
        name=request.POST['name']       
        date=request.POST['date']
        department=request.POST['department']
        reason=request.POST['reason']
        role=request.POST['role']
        
        status='0'
     
        reteh=leave(user=user,name=name,date=date,department=department,reason=reason,status=status,role=role)
        reteh.save()
       
        return render(request,'teacher.html')
    else:
        return render(request,'teacher.html')



def leavestudent(request):
    return render(request,'leavestudent.html')

def reqstud(request):
    if request.method:
        user=request.user
    if request.method=='POST':
        
        name=request.POST['psname']
        date=request.POST['date']
        department=request.POST['department']
        reason=request.POST['reason']
        role=request.POST['role']
        status='0'
        
        restd=leave(user=user,name=name,date=date,department=department,reason=reason,status=status,role=role)
        restd.save()
        
        return render(request,'student.html')
    else:
        return render(request,'student.html')

# def hodview(request):
#     data=admins.objects.filter(role='hod').values()
#     for i in data:
#         role=i['role']
#         leavess=leave.objects.filter(role=role).values()
#     return render(request,'leaveapprovedstudent.html',{'data':leavess})

    
# roles=''
# dept=''
# def teacherview(request):
#     global roles
#     global dept
#     if request.user:
#         user=request.user
#         print(user)

#         data=admins.objects.filter(user=user).values()
#         for i in data:
#             dept=i['department']
#             print(dept)
#         data11=teacher.objects.filter(department=dept).values()
#         print(data11)
#         for i in data11:
#             roles=i['role']
#             print(roles)
#             leavee=leave.objects.filter(role=roles).values()
#             return render(request,'appteacher.html',{'data':leavee})
#         else:
#             return render(request,'appteacher.html')
# def studentview(request):
#     if request.user:
#         user=request.user
#         print(user)
#         data=admins.objects.filter(user=user).values()
#         for i in data:
#             dept=i['department']
#             data22=students.objects.filter(department=dept).values()
#             print(data22)
#             for i in data22:
#                 roless=i['role']
#                 leaved=leave.objects.filter(roless).values()
#                 return render(request,'appstudent.html',{'data':leaved})
#             else:
#                 return render(request,'appstudent.html')
# def hodappview(request):
#     data=admins.objects.filter(role='hod').values()
#     for i in data:
#         id=i['username']
#         leavve=leave.objects.filter(user=id)
#     return render(request,'apphod.html',{'data':leavve})
# def hodleavebutton(request,user_id):
#     data=leave.objects.get(id=user_id)
#     data.status='1'
#     data.save()
#     return render('reqhod') 
# def hodleavedel(request,user_id):


def viewsleavehod(request):
    if request.user:
        user=request.user
        # dep=''

        hoddd_data=admins.objects.filter(user=user)
        # for i in hoddd_data:
            # dep=i['department']                                
        hod_data=leave.objects.filter(role='hod') 

    return render(request,'leaveapprovestudent.html',{'data':hod_data})

# def viewall(request):
#     a_view=admins.objects,filter(role="hod")
#     for i in a_view:
#         role=i['role']
#         b_view=leave.objects.filter(role=role)
#         return render(request.'leaveapprovestudent.html')
#     else:
#         return render(request.leaveapprovestudent.html)
# def viewsleavehod(request):
    # viewhod_leave=leave.objects.filter(role='hod')
    # print(viewhod_leave)
    # # for i in viewhod_leave:
    # #     print(i)
    # return render (request,'leaveapprovestudent.html',{'data':viewhod_leave})
    # if request.user:
    #      user=request.user
    #      dept=''
    # sub=''
    # viewhodle=admins.objects.filter(role='hod').values()
    # print('kkkkkkkkk',viewhodle)
    # for i in viewhodle:
    #     dept=i['department']
    #     print(dept)
    #     # sub=i['subject']
    # data4=leave.objects.filter(department=dept)
    #     # print(data4)
    # return render(request,'leaveapprovestudent.html',{'data':data4})




    

def deleteleavehod(request,leaa):
    leahod=leave.objects.get(id=leaa)
    leahod.delete()
    print(leahod)
    return redirect('viewsleavehod')
def formupdateleave(request,leav):
    if request.method=='POST':
        ADDE=leave.objects.get(id=leav)
        ADDE.name=request.POST['name']
        ADDE.date=request.POST['date']
        ADDE.department=request.POST['department']
        ADDE.reason=request.POST['reason']
        ADDE.role=request.POST['role']

        ADDE.save()
    return redirect('admin')
# def reapp(request):
#     return render(request,'appstudent.html')

def approve_LEAVE(request,leave_id):
    hodleaves=leave.objects.get(id=leave_id)
    hodleaves.status='1'
    hodleaves.save()
    
    joy=leave.objects.filter(id=leave_id).values()
    print(joy)
    return render(request,'appstudent.html',{'data':joy})


def viewsleaveteacher(request):
    # viewteacher_leave=leave.objects.filter(role='teacher')
    # print(viewteacher_leave)
    # for i in viewteacher_leave:
    #     print(i)
    # dept=''
    # sub=''
    # viewteachle=leave.objects.filter(role='teacher').values()
    # print('hhhh',viewteachle)
    # for i in viewteachle:
    #     dept=i['department']
    #     print(dept)
    #     # sub=i['subject']
    # teacherleave=teacher.objects.filter(department=dept)
    #     # print(i)
    # return render (request,'leaveapprovestudent.html',{'data':teacherleave})
    # return render(request,'leaveapprovestudent.html',{'data':data4})
    if request.user:
        user=request.user
        dep=''
        teacher_data=admins.objects.filter(user=user).values()
        for i in teacher_data:
            dep=i['department']
            # print(dep)                                
        hod_data=leave.objects.filter(Q (role='teacher') & Q (department=dep))

    return render(request,'leaveapprovestudent.html',{'data':hod_data})
       


      

def deleteleaveteacher(request,leate):
    leatacher=leave.objects.get(id=leate)
    leatacher.delete()
    print(leatacher)
    return redirect('viewsleavehod')
def formupdateleavete(request,leavte):
    if request.method=='POST':
        ADDT=leave.objects.get(id=leavte)
        ADDT.name=request.POST['name']
        ADDT.date=request.POST['date']
        ADDT.department=request.POST['department']
        ADDT.reason=request.POST['reason']
        ADDT.role=request.POST['role']

        ADDT.save()
    return redirect('hod')

def approve_teacher_leave(request,leave_idteacher):
    teacherleaves=leave.objects.get(id=leave_idteacher)
    teacherleaves.status='1'
    teacherleaves.save()
    
    joyy=leave.objects.filter(id=leave_idteacher).values()
    print(joyy)
    return render(request,'appstudent.html',{'data':joyy})

def viewsleavestudent(request):
    # viewstudent_leave=leave.objects.filter(role='student')
    # print(viewstudent_leave)
    # for i in viewstudent_leave:
    #     print(i)
    # dept=''
    # sub=''
    # viewstdle=leave.objects.filter(role='student').values()
    # print('heloo',viewstdle)
    # for i in viewstdle:
    #     dept=i['department']
    #     print(dept)
    #     # sub=i['subject']
    # viewstudent_leave=students.objects.filter(department=dept)
    #     # print(i)
    # return render (request,'leaveapprovestudent.html',{'data':viewstudent_leave})
    if request.user:
        user=request.user
        dep=''
        student_data=teacher.objects.filter(user=user).values()
        for i in student_data:
            dep=i['department']
            # print(dep)                                
        std_data=leave.objects.filter(Q (role='student') & Q (department=dep))

    return render(request,'leaveapprovestudent.html',{'data':std_data})


def deleteleavestudent(request,least):
    leastudent=leave.objects.get(id=least)
    leastudent.delete()
    print(leastudent)
    return redirect('viewsleavehod')
def formupdateleavest(request,leavst):
    if request.method=='POST':
        ADDS=leave.objects.get(id=leavst)
        ADDS.name=request.POST['name']
        ADDS.date=request.POST['date']
        ADDS.department=request.POST['department']
        ADDS.reason=request.POST['reason']
        ADDS.role=request.POST['role']
        
        ADDS.save()
    return redirect('teacher')

def approve_student_leave(request,leave_idstudent):
    studentleaves=leave.objects.get(id=leave_idstudent)
    studentleaves.status='1'
    studentleaves.save()
    
    joyyy=leave.objects.filter(id=leave_idstudent).values()
    print(joyyy)
    return render(request,'appstudent.html',{'data':joyyy})

def examlist(request):
    return render(request,'examlist.html')

def examstd(request):
    if request.method:
        user=request.user
        if request.method=='POST':
            
            subject=request.POST['subject']
            department=request.POST['department']
            date=request.POST['date']
            messages=request.POST['messages']
            status='0'
            
            examstd=viewexamlist(user=user,subject=subject,department=department,date=date,messages=messages,status=status)
            examstd.save()
            
            return render(request,'teacher.html')
        else:
            return render(request,'teacher.html')

# def examlistsview(request):
#      viewexam=viewexamlist.objects.filter(department='department')
#      print(viewexam)
#      return render (request,'hodviewexamlist.html',{'data':viewexam})
def hodviewexam(request):
    return render(request,'hodviewexamlist.html')
def examlistsview(request):
    if request.user:
        user=request.user
        print('user--->',user)
        dep=''
        exam_data=admins.objects.filter(user=user).values()
        print('///////////////////',exam_data)
        for i in exam_data:
            dep=i['department']
            print(dep)
            # print(dep)                                
        ex_data=viewexamlist.objects.filter(department=dep).values()
        print('&&&&&&&&&&&&&&&&&&&&&&&',ex_data)

    return render(request,'hodviewexamlist.html',{'data':ex_data})



def deleteexam(request,delexam):
    delexa=viewexamlist.objects.get(id=delexam)
    delexa.delete()
    print(delexa)
    return redirect('hodviewexam')
def formupdateexam(request,delexamlist):
    if request.method=='POST':
        ADDex=viewexamlist.objects.get(id=delexamlist)
        ADDex.name=request.POST['name']
        ADDex.date=request.POST['date']
        ADDex.department=request.POST['department']
        ADDex.reason=request.POST['messages']
        

        ADDTex.save()
    return redirect('hod')



def approve_student_exam(request,exam_idstudent):
    studentexamlist=viewexamlist.objects.get(id=exam_idstudent)
    studentexamlist.status='1'
    studentexamlist.save()
    return render(request,'hod.html')
    
def stdnotification(request):
    exl=viewexamlist.objects.all()
    print(exl)
    for i in exl:
        print(i)
    return render(request,'viewexamstudent.html',{'data':exl})
    # dept=''
    # sub=''
    # exl=leave.objects.filter(role='student').values()
    # print(exl)
    # for i in exl:
    #     dept=i['department']
    #     # sub=i['subject']
    # examviewstd=students.objects.filter(Q(department=dept))
  
    # return render(request,'viewexamstudent.html',{'data':examviewstd})

def marks(request):
    return render(request,'publishmarklist.html')

def publish(request):
     if request.method:
        user=request.user
        if request.method=='POST':
            
            name=request.POST['name']
            department=request.POST['department']
            subject=request.POST['subject']
            total=request.POST['total']
            mymark=request.POST['mymark']
            status='0'
            
            publishstd=mark(user=user,name=name,department=department,subject=subject,total=total,mymark=mymark,status=status)
            publishstd.save()
            
            return render(request,'teacher.html')
        else:
            return render(request,'teacher.html')  
# def publishview(request):
#     if request.user:
#         user=request.user
#         dept=''
#         sub=''
#         data=students.objects.filter(user=user).values()
#         for i in data:
#             dept=i['department']
#             sub=i['subject']
#         dataa=mark.object.fillter(Q(department=dept)&Q(subject=sub))
#     return render(request,'publishmark',{'data':})
def publishview(request):
    return render(request,'publishmark.html')
def publishmarkview(request):
    # if request.user:
    #     user=request.user
    #     dept=''
    #     sub=''
    #     data=students.objects.filter(user=user).values()
    #     for i in data:
    #         dept=i['department']
    #         sub=i['subject']
    #     dataa=mark.object.fillter(Q(department=dept)&Q(subject=sub))
    # return render(request,'publishmark.html',{'data':})
    mar=mark.objects.all()
    print(mar)
    for i in mar:
        print(i)
    return render (request,'publishmark.html',{'data':mar})
    # if request.user:
    #      user=request.user
    #      dep=''
         
    #      mar=mark.objects.filter(user=user).values()
    #      print(mar)

    #      for i in mar:
    #         dep=i['department']
    #         print(dep)
    #     # sub=i['subject']
    #      markview=students.objects.filter(department=dep)
    #     #   print(i)
    # return render(request,'publishmark.html',{'data': markview})