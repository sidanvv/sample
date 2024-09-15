from django.db import models

# Create your models here.


class Details(models.Model):
    course_name=models.CharField(max_length=36,null=True,blank=True)
    course_details=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.course_name

class Teachers(models.Model):
    teachers_name=models.CharField(max_length=36,null=True,blank=True)
    course_name=models.ForeignKey(Details,on_delete=models.CASCADE)
    teacher_image=models.ImageField(upload_to='teacher')

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10)

class Employ(models.Model):
    Employ_Id=models.CharField(max_length=50,unique=True)
    fullname=models.CharField( max_length=50)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10)




