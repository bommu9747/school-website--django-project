from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class admins(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=250)
    lastname =models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    email =models.CharField(max_length=250)
    phone= models.IntegerField()
    department= models.CharField(max_length=250)
    password= models.CharField(max_length=250)
    conform=models.CharField(max_length=250)
    qualification=models.CharField(max_length=250)
    years=models.IntegerField()
    status=models.CharField(max_length=250)
    role=models.CharField(max_length=250)
    
   
    def __str__(self):
        return self.name
        
class teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    email =models.CharField(max_length=250)
    phone= models.IntegerField()
    department=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    conform=models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    qualification=models.CharField(max_length=250)
    years=models.IntegerField()
    status=models.CharField(max_length=250)
    role=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class students(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    email =models.CharField(max_length=250)
    phone= models.IntegerField()
    department=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    conform=models.CharField(max_length=250)
    years=models.IntegerField()
    status=models.CharField(max_length=250)
    role=models.CharField(max_length=250)
    def __str__(self):
        return self.name
class leave(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    date=models.CharField(max_length=250)
    reason=models.CharField(max_length=500)
    department=models.CharField(max_length=500)
    status=models.CharField(max_length=250)
    role=models.CharField(max_length=250)
    def __str__(self):
        return self.name
class viewexamlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=250)
    department=models.CharField(max_length=250)
    date=models.CharField(max_length=250)
    messages=models.CharField(max_length=250)
    status=models.CharField(max_length=250)
    def __str__(self):
        return self.subject

class mark(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    department=models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    total=models.CharField(max_length=250)
    mymark=models.CharField(max_length=250)
    status=models.CharField(max_length=250)
    def __str__(self):
        return self.name
