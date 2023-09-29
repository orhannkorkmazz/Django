from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)

        newUser.save()
        #login(request,newUser)
        messages.success(request, "Başarıyla kayıt oldunuz.")
        

        return redirect("index")
    else:
        context = {
            "form" : form
        }
    return render(request,"register.html",context)
def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        kullanıcı=authenticate(username=username,password=password)
        if kullanıcı is None:
            messages.info(request,"Böyle bir kullanıcı bulunmuyor ya da şifre yanlış")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,kullanıcı)
        return redirect("index")
    return render(request,"login.html",context)
def logoutUser(request):
    
    logout(request)
    messages.info(request,"Başarıyla çıkış yaptınız" )
    return redirect('index')
    




