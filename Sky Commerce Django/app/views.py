from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect


def index(request):
    return render(request,'main.html')

def register(request):
    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        if password == password2:
            if User.objects.filter(username = username).exists():
                return redirect("register")
            elif User.objects.filter(email = email).exists():
                return redirect('register')   
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                auth.login(request,user)
                return redirect('index')
        else:
            return redirect('register')




    return render(request,'register.html')


def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')


