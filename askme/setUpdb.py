import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askme.settings')
django.setup()
from django.contrib.auth.models import User
from askmeApp.models import Question, Answer, Tag, Like, InstanceType, Profile, Repost 
from faker import *
from faker.providers import *
from datetime import datetime,date ,time
from django.contrib.auth.models import User
from django.utils import timezone
import random




# Создаем несколько тегов
t = ['C++', 'Assemble', 'Django', 'Mail.ru', 'Mysql',
         'Texnopark', 'Vk', 'Firefox', 'Python', 'Chrome', 'Development',
           'Ruby on rails', 'Tcp/ip', 'Css', 'Java', 'Kotlin', 'Software', 'Patterns', 'Bender', 
           'Migrations', 'Templates', 'Views', 'Algorithms', 'Data structures', 'Models', 'Qt', 'Faker',
             'Management', 'Vscode', 'Git', 'Docker', 'Redis', 'Postgresql', 'Nosql', 'Ajax', 'Async', 'Html', 'Javascript']

# Создаем несколько пользователей
fake=Faker()
def question_answers_add_tags():
  k=0
  questions=Question.objects.all()[10000:20000]
  for question in questions:
    tags=question.tags.all()
    for answer in question.answer_set.all():
      for tag in tags:
        answer.tags.add(tag)
    if(k%100==0):
      print(question.title)
    k+=1
def likes():
  likes=Like.objects.all()
  rand=0
  instanceTypes=InstanceType.objects.all()
  instanceTypesLength=len(instanceTypes)
  for like in likes:
    n=rand+random.randint(50, 350)
    if(n >= instanceTypesLength):
      break
    for instanceType in instanceTypes[rand:n]:
      like.like_type.add(instanceType)
    rand=n
    print(rand)

def create_tags_for_questions():
  for question in Question.objects.all():
    tags=random.sample(list(Tag.objects.all()), random.randint(0, 12))
    for tag in tags:
      question.tags.add(tag)
    question.save()
    question_answers_add_tags()
    


question_answers_add_tags()