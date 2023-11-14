from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.http.request import HttpRequest
import os
from datetime import datetime
# Create your models here.

def get_upload_path(instance, filename):
    current_date = datetime.now().strftime("%Y-%m-%d")
    return os.path.join("uploads", current_date, filename)

class Tag(models.Model):
  name=models.CharField(max_length=255)

class Question(models.Model):
  title=models.CharField(max_length=255)
  text=models.TextField()
  public_date=models.DateTimeField(auto_now=True)
  tags=models.ManyToManyField('Tag', related_name='questions')
  user=models.ForeignKey('Profile',null=True, blank=True, on_delete=models.SET_NULL, )
 
class Answer(models.Model):
  title=models.CharField(max_length=255)
  text=models.TextField()
  public_date=models.DateTimeField(auto_now=True)
  tags=models.ManyToManyField('Tag', related_name='answers')
  user=models.ForeignKey('Profile',null=True, blank=True, on_delete=models.SET_NULL)
  question=models.ForeignKey('Question',null=True, on_delete=models.CASCADE)

class Profile(User):
  user_id=models.BigIntegerField(unique=True, primary_key=True)
  avatar=models.ImageField(null=True, blank=True, upload_to=get_upload_path)
  age = models.PositiveIntegerField(validators=[MaxValueValidator(110)])
  birth_date=models.DateField(null=True, blank=True)

class InstanceType(models.Model):
  type=models.PositiveIntegerField(validators=[MaxValueValidator(2)])
  question=models.OneToOneField('Question',null=True, blank=True, on_delete=models.CASCADE)
  answer=models.OneToOneField('Answer',null=True, blank=True, on_delete=models.CASCADE)
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
  user=models.OneToOneField('Profile', on_delete=models.CASCADE)
  like_type=models.ForeignKey('InstanceType', on_delete=models.CASCADE)
 
  
class Repost(models.Model):
  type_id=models.PositiveIntegerField(validators=[MaxValueValidator(2)])
  public_date=models.DateTimeField(auto_now=True)
  user=models.OneToOneField('Profile', on_delete=models.CASCADE)
  repost_type=models.ForeignKey('InstanceType', on_delete=models.CASCADE)
 