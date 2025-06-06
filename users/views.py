from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import CustomuserCreationForm


def register(request):
    if request.method == "POST":
        register_form = CustomuserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            print("new user created!!")
            return redirect("login")
    else:    
        register_form = CustomuserCreationForm()
        
    return render(request, "register.html", {'register_form': register_form})
    
def login(request):
    return HttpResponse("Welcome to Login Page!!")