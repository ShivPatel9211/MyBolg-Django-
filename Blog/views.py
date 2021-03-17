from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate , login, logout 


code =0


def index(request):
    return render(request,'index.html',)
    

def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        image1=request.FILES['image1']

        try:
            if User.objects.filter(username=username).first():
                messages.success(request,"User of this username is already exist ")
                return redirect('register')
            if User.objects.filter(email=email).first():
                messages.success(request," This email id is already is used ")
                return redirect('register')

            
            user_obj = User(first_name=firstname,last_name=lastname,username=username , email=email)
            user_obj.set_password(password)
            user_obj.save()
            global code 
            code = random.randint(2000, 9000)
            profile_obj =Profile.objects.create(user=user_obj,code=code , profile_img=image1)
            profile_obj.save()
            sendMail(email , code)
            return redirect('mailsent')
        except Exception as e:
            messages.success(request, e)
            return redirect('register')


       

    return render(request,'register.html')

def login_attemp(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'User not found plz create your account ')
            return redirect('login')
        else:
            profile_obj = Profile.objects.filter(user=user_obj).first()
            if profile_obj.is_varified:
                user = authenticate(username=username,password=password)
                if user is None:
                    messages.success(request, "Please enter correct password or username")
                    return redirect('login')
                else:
                    login(request, user)
                    return redirect('home')
    

    return render(request,'login.html')


def verify(request):
    global code
    if request.method == "POST":
        code1=request.POST['code']
       

        # print("this is orginal code " + str(code))
        # print("this is optained code " + code1)
    
        if str(code) == code1:
            profile_obj =Profile.objects.filter(code=code).first()
            profile_obj.is_varified=True
            profile_obj.save()
            return redirect("login")
        else:
            messages.success(request, 'Please enter correct code')
            return redirect('mailsent')
    context={
        'code1':code
    }

    return render(request,'mailsent.html' , context )


def sendMail(email , code):
    subject ='Your account need to be varified'
    message = f'Hi !! Your configuration code is   '+  str(code)  
    email_from = settings.EMAIL_HOST_USER
    recpient_list = [email]
    send_mail(subject,message,email_from,recpient_list)


def logout_attemp(request):
    logout(request)
    return redirect('home')

def about(request):
    return render(request, 'about.html')

def contact(request):
       return render(request, 'contact.html')
