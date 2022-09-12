from ast import arg
from email import message
import email
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from form.models import Users
# Create your views here.
# class MyForm(forms.Form) : 
#     email = forms.EmailField(label="Email",max_length=256)
#     password = forms.CharField(label="",widget=forms.PasswordInput(attrs={"autocomplete":"off"}), min_length=8)
#     confirm = forms.CharField(label="",widget=forms.PasswordInput(attrs={"autocomplete":"off"}), min_length=8)


def index(request) : 
    if request.method == "POST" :
        if request.POST["pass"] != request.POST["conf"] :
            return render(request,"forms/index.html",{
                "message" : "passwords don't match"
            })
         
        auth = authenticate(request, username= request.POST['username'], password =request.POST['pass'])
        if auth is not None : 
            return render(request,"forms/login.html",{
            "message" : "username already exists"
        })
        try :
            user = Users.objects.create_user(username=request.POST['username'], email= request.POST['email'],password= request.POST['pass'])
            login(request, user)
            return HttpResponseRedirect(reverse("spongebob:sponge"))
        except:
            return render(request,"forms/index.html",{
                "message" : "user exists"
            })
         

        
    else: 
        return render(request,"forms/index.html")



def login_user(request):
    if request.method =="POST":
        username= request.POST["email"]
        password = request.POST['pass']
        auth = authenticate(request, username=username, password=password)
        if auth is not None : 
            user = Users.objects.get(username=username)
            login(request, user)
            return HttpResponseRedirect(reverse("spongebob:sponge"))
        else :
            return render(request, "forms/login.html",{
                "message" : "user doesn't exist"
            })
    else: 
        return render(request, "forms/login.html")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("form:register"))