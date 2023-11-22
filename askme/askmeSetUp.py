import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askme.settings')
django.setup()
import random
from django.contrib.auth.models import User
from askmeApp.models import Question, Answer, Tag, Like, InstanceType, Profile, Repost 
from faker import Faker
from datetime import datetime,date ,time
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import Error
fake=Faker()
t = ['C++', 'Assemble', 'Django', 'Mail.ru', 'Mysql',
         'Texnopark', 'Vk', 'Firefox', 'Python', 'Chrome', 'Development',
           'Ruby on rails', 'Tcp/ip', 'Css', 'Java', 'Kotlin', 'Software', 'Patterns', 'Bender', 
           'Migrations', 'Templates', 'Views', 'Algorithms', 'Data structures', 'Models', 'Qt', 'Faker',
             'Management', 'Vscode', 'Git', 'Docker', 'Redis', 'Postgresql', 'Nosql', 'Ajax', 'Async', 'Html', 'Javascript']

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="askmeuser",
                                  password="passaskme",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="askme")
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # for i in range(len(t)):
    #     query="""INSERT INTO "askmeApp_tag" VALUES (%s,%s)"""#17:11
    #     item_tuple=(i, t[i])
    #     cursor.execute(query,item_tuple) 
    count=0
    # for i in range(1,10000):
    #     query="""INSERT INTO "askmeApp_profile" VALUES (%s,%s,%s, %s, %s)"""#17:11
    #     item_tuple=(i,"no_avatar.jpg",fake.random_int(7,90),fake.date_between(),i)
    #     cursor.execute(query, item_tuple)
    # connection.commit()
    # for i in range(100000):
    #     query="""INSERT INTO "askmeApp_question" VALUES (%s,%s,%s, %s, %s)"""#17:11
    #     title=str(fake.text(max_nb_chars=30))
    #     text= str(fake.text(max_nb_chars=fake.random_int(10, 500)))
    #     public_date=fake.date_between()
    #     user_id=str(fake.random_int(1, 9999))
    #     item_tuple=(i, title,text, public_date, user_id)
    #     cursor.execute(query,item_tuple)
    #     r=fake.random_int(1, 25)
    #     for j in range(1,r):
    #         query="""INSERT INTO "askmeApp_answer" VALUES (%s,%s,%s,%s, %s, %s)"""#17:11
    #         title=fake.text(max_nb_chars=30)
    #         text= fake.text(max_nb_chars=fake.random_int(10, 500))
    #         public_date=fake.date_between()
    #         question_id=i
    #         user_id=str(fake.random_int(1, 9999))
    #         item_tuple=(i*25+j, title, text,public_date, question_id, user_id)
    #         cursor.execute(query, item_tuple)
    #     count+=r
    #     if(i%1000==0 and i!=0):
    #         connection.commit()
    #         print(i)
     # m=random.sample([i for i in range (len(t)-1)], len(t)-1)
        # j=random.sample()
        # for j in range(0,10): 
        #     query="""INSERT INTO "askmeApp_answer_tags" VALUES (%s,%s,%s)"""
        #     random.seed(0)
        #     item_tuple=(i*10+j, i*25,m[j])
        #     cursor.execute(query,item_tuple)  
        # if(i>1000):
        #     connection.commit()
    # Faker.seed()
    # connection.commit()
    # instance_type=[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
    # random_questions=list(random.sample([i for i in range(1,len(list(Question.objects.all()))-1)], 70000))
    # random_answers=list(random.sample([i for i in range(1,len(list(Answer.objects.all()))-1)], 700000))
    # q=0
    # a=0
    # questionsLength=len(list(Question.objects.all()))
    # for i in range(0,7700000):#2000000 - likes 400000 - reposts
    #     query="""INSERT INTO "askmeApp_instancetype" VALUES (%s, %s, %s, %s)"""#17:11
    #     id=i
    #     type=instance_type[random.randint(0,len(instance_type)-1)]
    #     if(type):
    #         answer_id=random_answers[a]
    #         question_id=None
    #         a+=1
    #     elif(type==0):
    #         question_id=random_questions[q]
    #         answer_id=None 
    #         q+=1   
    #     item_tuple=(id, type, answer_id, question_id)
    #     cursor.execute(query, item_tuple) 
    #     if(i%10000==0):
    #         connection.commit()
    #         print(i)
    instance_type=[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]  
    # random_user=random.sample([i for i in range(len(User.objects.all())-1)],int(len(User.objects.all())/2))#половина пользователей поставила лайк
    # userLength=len(random_user)
    # for i in range(userLength):
    #     query="""INSERT INTO "askmeApp_like" VALUES (%s, %s, %s, %s)"""
    #     id=i
    #     type_id=instance_type[random.randint(0, len(instance_type)-1)]
    #     public_date=fake.date_between()
    #     user_id=random_user[i]
    #     item_tuple=(id, type_id, public_date, user_id)
    #     cursor.execute(query,item_tuple)  
    #     if(i%10000==0):
    #         connection.commit()
    #         print(i)
    random_user=random.sample([i for i in range(len(User.objects.all())-1)],int(len(User.objects.all())/5))#половина пользователей поставила лайк
    userLength=len(random_user)
    for i in range(userLength):
        query="""INSERT INTO "askmeApp_repost" VALUES (%s, %s, %s, %s)"""
        id=i
        type_id=instance_type[random.randint(0, len(instance_type)-1)]
        public_date=fake.date_between()
        user_id=random_user[i]
        item_tuple=(id, type_id, public_date, user_id)
        cursor.execute(query,item_tuple)  
        if(i%10000==0):
            connection.commit()
            print(i)
    # for i in range(1000000):
    #     query="""INSERT INTO client VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    #     dat=fake.date_between()
    #     two_days = dat
    #     new_date=fake.date_between()
    #     item_tuple=(i,fake.name(),dat, fake.pybool(),new_date, random.randint(0,1000000),fake.address(),fake.date_between(),random.randint(0,149))
    #     cursor.execute(query,item_tuple) 
    #     if (i%50000==0 and i!=0):
    #         print("select 50000")
   
    connection.commit()
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")