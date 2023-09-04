from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username =username)
            newUser.set_password(password)
            newUser.save()
            #login(request,newUser)
            messages.success(request,"Başarıyla kayıt oldunuz.")
            return redirect("index") 
    else:
        context = {
            "form" : form
        } 
    return render(request,"register.html",context)
def loginUser(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request,"Başarıyla Giriş Yaptınız")
				return redirect("index")
			else:
				messages.warning(request,"Kullanıcı adı veya parola hatalı.")
		else:
			messages.warning(request,"Kullanıcı adı veya parola hatalı.")
	form = AuthenticationForm(request)
	return render(request, "login.html", {"form":form})
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız.")
    return redirect('index')