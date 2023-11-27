from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader
from django.core.paginator import Paginator
from .models import Profile, Question, Answer, Tag, InstanceType, QuestionManeger
from django.db.models import *

def paginate(objects, request, count=5):
  page=int(request.GET.get('page',1))
  p=Paginator(objects, count)
  last_page=p.page_range.stop-1
  if(page>last_page):
    page=last_page
  if(page<1):
    page=1
  page_object=p.page(page)
  return page_object

def index(request):
  questions=Question.objects.all()
  page_object=paginate(questions, request)
  context={'questions': page_object}
  return render(request,'index.html', context)

def ask(request):
  return render(request,'ask.html')

def question(request, question_id):
  question=Question.objects.get(id=question_id)
  context={'question': question}
  return render(request,'question.html', context)

def register(request):
  return render(request,'register.html')

def login(request):
  return render(request,'login.html')

def tag_questions(request, name):
  tag=Tag.objects.get(name=name)
  questions=tag.questions.all()
  page_object=paginate(questions, request)
  context={'questions': page_object, 'tag': tag}
  return render (request, 'tag_questions.html', context)

def settings(request):
  return render (request, 'settings.html') 


def bestQuestions(request):
  questions=Question.objects.bestQuestions(20)
  page_object=paginate(questions,request, 20)
  return render (request, 'bestQuestions.html', context={'questions': page_object})

def newQuestions(request):
  questions=Question.objects.newQuestions(20)
  page_object=paginate(questions,request, 20)
  return render (request, 'bestQuestions.html', context={'questions': page_object})


def pageNotFound(request, exception):
  template = loader.get_template('notFound.html')
  return HttpResponseNotFound(template.render(request))



  
