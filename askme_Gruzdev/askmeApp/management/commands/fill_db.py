import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askme.settings')
django.setup()
from django.contrib.auth.models import User
from askmeApp.models import *
from faker import *
from faker.providers import *
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import random

# теги
tags = ['C++', 'Assemble', 'Django', 'Mail.ru', 'Mysql',
         'Texnopark', 'Vk', 'Firefox', 'Python', 'Chrome', 'Development',
           'Ruby on rails', 'Tcp/ip', 'Css', 'Java', 'Kotlin', 'Software', 'Patterns', 'Bender', 
           'Migrations', 'Templates', 'Views', 'Algorithms', 'Data structures', 'Models', 'Qt', 'Faker',
             'Management', 'Vscode', 'Git', 'Docker', 'Redis', 'Postgresql', 'Nosql', 'Ajax', 'Async', 'Html', 'Javascript']

class Command(BaseCommand):
  fake=Faker()
  instance_type=[1, 1, 1, 0, 1, 1, 1, 1, 1, 1] #отсюда будем брать рандомный тип(0-вопрос, 1-ответ) получится соотношение примерно 1 к 9

  def instancetype(self, count):
    answers=Answer.objects.all()
    questions=Question.objects.all()
    random.shuffle(list(answers))
    random.shuffle(list(questions))
    a=0
    q=0
    instanceTypes=[]
    for i in range(count):
      answer=None
      question=None
      type=self.instance_type[random.randint(0, len(self.instance_type)-1)]
      if(type):
        answer=answers[a]
        a+=1
      elif(type==0):
        question=questions[q]
        q+=1
      instanceTypes.append(InstanceType(id=i, type=type,answer=answer, question=question)) 
    print('Saving instancetypes')
    InstanceType.objects.bulk_create(instanceTypes)
    print('Done')

  def questions(self, count):
    users=Profile.objects.all()
    tags=Tag.objects.all()
    questions=[Question(title=self.fake.text(max_nb_chars=30), text=self.fake.text(max_nb_chars=2000), 
    public_date=self.fake.date_this_year(), tags=random.choice(tags), user=random.choice(users)) for i in range(count)]
    print('Saving questions')
    Question.objects.bulk_create(questions)
    print('Done')

  def users(self, count):
    users=[User(password=self.fake.password(), username=self.fake.first_name()+self.fake.last_name()+self.fake.text(max_nb_chars=5), 
    email=self.fake.email()) for i in range(count)]
    print('Saving users')
    User.objects.bulk_create(users)
    print('Done')
    users=list(User.objects.all())
    profiles=[Profile(user_id=i, age=random.randint(7, 90), birth_date=self.fake.date_of_birth(), profile_user=users[i]) for i in range(count)]
    print('Saving profiles')
    Profile.objects.bulk_create(profiles)
    print('Done')

  def answers(self, count):
    users=Profile.objects.all()
    tags=Tag.objects.all()
    questions=Question.objects.all()
    answers=[Answer(title=self.fake.text(max_nb_chars=30), text=self.fake.text(max_nb_chars=800), 
    public_date=self.fake.date_this_year(), tags=random.choice(tags), user=random.choice(users), question=random.choice(questions)) for i in range(count)]
    print('Saving answers')
    Answer.objects.bulk_create(answers)
    print('Done')

  def tags(self):
    print('Saving tags')
    Tag.objects.bulk_create(tags)
    print('Done')

  def likes(self, ratio, count, like_type):
    users=Profile.objects.all()
    random.shuffle(list(users))
    likes=[Like(type_id=self.instance_type[random.randint(0, len(self.instance_type)-1)], public_date=self.fake.date_this_year(), user=users[i]) for i in range(ratio)]
    print('Saving users likes')
    Like.objects.bulk_create(likes)
    print('Done')
    likes=Like.objects.all()
    instanceTypes=InstanceType.objects.filter(type_id=like_type)
    instanceTypesLength=len(instanceTypes)
    r=0
    i=0
    if(like_type==0):
      print('Saving likes for questions')
    elif(like_type==1):
      print('Saving likes for answers')
    while (r < count):
      rand=random.randint(0, 8)
      r+=rand
      for i in range(rand):
        instanceTypes[i].likes.add(likes[random.randint(0, len(likes)-1)])
      i+=1
      if(i>=instanceTypesLength):
        break
      print('Done')

  def reposts(self, ratio, count, repost_type):
    users=Profile.objects.all()
    random.shuffle(list(users))
    reposts=[Repost(type_id=self.instance_type[random.randint(0, len(self.instance_type)-1)], public_date=self.fake.date_this_year(), user=users[i]) for i in range(ratio)]
    print('Saving reposts')
    Repost.objects.bulk_create(reposts)
    print('Done')
    reposts=Repost.objects.all()
    instanceTypes=InstanceType.objects.filter(type_id=repost_type)
    instanceTypesLength=len(instanceTypes)
    r=0
    i=0
    if(repost_type==0):
      print('Saving reposts for questions')
    elif(repost_type==1):
      print('Saving reposts for answers')
    while (r < count):
      rand=random.randint(0, 4)
      r+=rand
      for i in range(rand):
        instanceTypes[i].likes.add(reposts[random.randint(0, len(reposts)-1)])
      i+=1
      if(i>=instanceTypesLength):
        break

  def add_arguments(self, parser):
    parser.add_argument('ratio', type=int)

  def handle(self, *args, **options):
    ratio = options['ratio']
    users_count = ratio
    questions_count = ratio * 10
    answers_count = ratio * 100
    instancetypes_count = int((questions_count+answers_count)*0.8)# instancetype соответствует одному вопросу или ответу, в зависимости от поля type_id,
    questions_likes_count = ratio * 20# значит количество таких записей должно быть равно количеству вопросов + количеству ответов, которые содержат лайки или репосты. Множитель 0.8 означает, что 80% ответов и вопросов будут иметь лайк или репост или все вместе
    answers_likes_count = ratio * 180
    questions_reposts_count = ratio * 5
    answers_reposts_count = ratio * 45
    self.users(users_count)
    self.tags()
    self.questions(questions_count)
    self.answers(answers_count)
    self.instancetype(instancetypes_count)
    self.likes(int(ratio*0.7), questions_likes_count, 0)# ratio*0.7 - количество пользователей, ставивших лайк - 70% пользователей
    self.likes(int(ratio*0.7), answers_likes_count, 1)# последний аргумент означает тип: 0 - вопрос, 1 - ответ
    self.reposts(int(ratio*0.3), questions_reposts_count, 0)# ratio*0.3 - количество пользователей, ставивших репост - 30% пользователей
    self.reposts(int(ratio*0.3), answers_reposts_count, 1)
