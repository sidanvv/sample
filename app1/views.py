from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    person={
        'name':['adil','banan','catrin','david']
    }
    return render(request,'ss.html',person)



def teacher(request):
     teachers={
        'teacher':Teachers.objects.all()
    }
     return render(request,'teacher.html',teachers)


def student(request):
    return render(request,'student.html')



def details(request):
    dic_details={
        'dtls':Details.objects.all()
    }
    return render(request,'details.html',dic_details)



from .forms import UserForm
def contact(request):
    form=UserForm()
    return render(request,'contact.html',{'form':form})

def sucess_view(request):
    return render(request,'sucess.html')


def user_form_view(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form=UserForm()
    return render(request,'contact.html',{'form':form})


def contact_details(request):
    cont={
        'dtls':Contact.objects.all()
    }
    return  render(request,'contact_details.html',cont)

def contact2(request):
    return render(request,'contact2.html')

def employlist(request):
    employlist={
        'dtls':Employ.objects.all()
    }
    return render(request,'employlist.html',employlist)


def employee_form_view(request):
    if request.method=='POST':
        empy_id=request.POST['emp_id']
        fullname=request.POST['name']
        email=request.POST['email']
        phone=request.POST['number']

        employ =Employ()
        employ.Employ_Id=empy_id
        employ.fullname=fullname
        employ.email=email
        employ.phone=phone
        employ.save()
        return redirect('employlist')
    
    return render(request,'contact2.html')

def emp_detele(request,id):
    emp = Employ.objects.get(pk=id)
    emp.delete()
    return redirect('employlist')

def emp_edit(request,id):
    emp=Employ.objects.get(pk=id)
    return render(request,'update.html',{'emp_up':emp})


def emp_update_form(request,id):

    if request.method=='POST':
        empy_id=request.POST['emp_id']
        fullname=request.POST['name']
        email=request.POST['email']
        phone=request.POST['number']

        employ=Employ.objects.get(pk=id)
        employ.Employ_Id=empy_id
        employ.fullname=fullname
        employ.email=email
        employ.phone=phone
        employ.save()
        return redirect('employlist') 
    return render(request,'update.html')


from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
def register(request):
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print('sidhan')
            username=form.cleaned_data.get('username')
            messages.success(request,f'account created for {username}')
            return redirect('userlogin')
    else:
        form =CreateUserForm()
    return render (request,'register.html',{'form':form})



from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect ('main')
        else:
            return redirect('register')
    else:
        form=AuthenticationForm()
    return render(request,'login.html')

# def logout(request):
#     return render(request,'ss.html')
