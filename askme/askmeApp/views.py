from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Profile

def index(request):
  page=request.GET.get('page',1)
  return render(request,'index.html', context={'page': page})

def ask(request):
  return render(request,'ask.html')

def questions(request):
  return render(request,'question.html')

def register(request):
  return render(request,'register.html')

def login(request):
  return render(request,'login.html')

def tag_questions(request):
  return render (request, 'tag_questions.html')

def settings(request):
  return render (request, 'settings.html') 