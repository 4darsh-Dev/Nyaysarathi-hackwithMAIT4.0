from django.shortcuts import render


# written by admin

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

