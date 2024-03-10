from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .forms import userLoginForm, userRegistrationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def userLogin(request):
    page = 'login'
    form = userLoginForm()
    if request.method == "POST":
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        form = userLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:    
                user =User.objects.get(username=username)
                print(user)
                user = authenticate(request, username=username, password=password)
                print(user)
                if user is not None:
                    login(request, user)
                    return redirect("/jobs/dashboard")
                else:
                    messages.error(request, "Invalid username or password")
            except:
                form["username"].field.widget.attrs['class'] += ' is-invalid'
                form["password"].field.widget.attrs['class'] += ' is-invalid'
                messages.error(request, "Invalid username or password")
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
            
    context = {'page':page,"form":form}
    return render(request, "Auth/Authentication.html", context)

def userRegister(request):
    form = userRegistrationForm()
    if request.method == "POST":
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            user  = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            user.save()
            login(request, user)
            messages.success(request, "User created successfully")
            return redirect("/jobs/dashboard")
        else:
            print(form.errors)
            for field in form.errors:
                print(field)
                form[field].field.widget.attrs['class'] += ' is-invalid'
    
    context = {"form":form}
    return render(request, "Auth/Authentication.html", context)

def userLogout(request):
    logout(request)
    return redirect('/')