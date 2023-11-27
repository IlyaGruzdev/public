from django.db import models
from django.db import connection, connections
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.http.request import HttpRequest
import os
from datetime import datetime
# Create your models here.

def get_upload_path(instance, filename):
    current_date = datetime.now().strftime("%Y-%m-%d")
    return os.path.join("uploads", current_date, filename)

class QuestionManeger(models.Manager):
  def bestQuestions(self, count):
    return self.raw('''select * from "askmeApp_question" as a where a.id in 
  (select i.question_id from "askmeApp_instancetype" as i
  inner join "askmeApp_like_like_type" as l on i.id=l.instancetype_id
  inner join "askmeApp_repost_repost_type" as r on i.id=r.instancetype_id where i.type=0
  group by question_id order by count(question_id) desc limit %s)''', (count, ))

  def newQuestions(self, count):
    return self.order_by('-public_date')[:count]

class Tag(models.Model):
  name=models.CharField(unique=True,max_length=255)

class Question(models.Model):
  title=models.CharField(max_length=255)
  text=models.TextField()
  public_date=models.DateTimeField(auto_now=True)
  tags=models.ManyToManyField('Tag', related_name='questions')
  user=models.ForeignKey('Profile',null=True, blank=True, on_delete=models.SET_NULL)
  objects=QuestionManeger()
 
class Answer(models.Model):
  title=models.CharField(max_length=255)
  text=models.TextField()
  public_date=models.DateTimeField(auto_now=True)
  tags=models.ManyToManyField('Tag', related_name='answers')
  user=models.ForeignKey('Profile',null=True, blank=True, on_delete=models.SET_NULL)
  question=models.ForeignKey('Question', null=True, blank=True, on_delete=models.CASCADE)

class Profile(models.Model):
  user_id=models.BigIntegerField(unique=True, primary_key=True)
  avatar=models.ImageField(null=True, blank=True, upload_to=get_upload_path, default='no_avatar.jpg')
  age = models.PositiveIntegerField(validators=[MaxValueValidator(110)])
  birth_date=models.DateField(null=True, blank=True)
  profile_user=models.OneToOneField(User,related_name='user', on_delete=models.CASCADE)

class InstanceType(models.Model):
  type=models.PositiveIntegerField(validators=[MaxValueValidator(2)])
  question=models.OneToOneField('Question', related_name='questionInstance', null=True, blank=True, on_delete=models.CASCADE)
  answer=models.OneToOneField('Answer', related_name='answerInstance', null=True, blank=True, on_delete=models.CASCADE)
  def get(self):
    match self.type:
      case(0):
        return self.question
      case(1):
        return self.answer
      case _:
        raise ValueError(f"Incorrect type: {type}")

class Like(models.Model):
  type_id=models.PositiveIntegerField(validators=[MaxValueValidator(2)])
  public_date=models.DateTimeField(auto_now=True)
  user=models.OneToOneField('Profile', related_name='like', on_delete=models.CASCADE)
  like_type=models.ManyToManyField('InstanceType', related_name='likes')
 
  
class Repost(models.Model):
  type_id=models.PositiveIntegerField(validators=[MaxValueValidator(2)])
  public_date=models.DateTimeField(auto_now=True)
  user=models.OneToOneField('Profile', related_name='repost', on_delete=models.CASCADE)
  repost_type=models.ManyToManyField('InstanceType',related_name='reposts')
 