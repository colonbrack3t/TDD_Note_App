from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
import re
# Create your views here.
def login(request):
    pass
def signup(request):

    signup_parameters= ['username','email','password']
    if request.POST and all(parameter in request.POST for parameter in signup_parameters):
        if len(User.objects.filter(email= request.POST['email'])) > 0:
            # User has used email that exists in db
            # Tell user to log in instead - redirect to login
            pass
        elif len(User.objects.filter(username= request.POST['username'])) > 0:
            # User has used username that exists in db
            # Tell user to log in instead - redirect to login
            pass
        else:
            # check email address validity
            email_regex = r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$"
            if re.search(email_regex,request.POST['email']):
                user = User.objects.create_user(
                    request.POST['username'],
                    request.POST['email'],
                    request.POST['password']
                )
                request.user = user
                return redirect('/')
        return 
