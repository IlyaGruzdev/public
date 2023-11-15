from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader
from django.core.paginator import Paginator
from .models import Profile




def f():
  questions=[]
  answers=[]
  for i in range(20):
      questions.append({'title': 'title'  + str(i),'id': i, 'text': '''Lorem ipsum, dolor sit amet consectetur adipisicing elit.
          Non, iusto. Iste reiciendis vitae quam! 
          Exercitationem quaerat doloremque voluptates eveniet quo quos nemo ducimus, voluptatum,
            adipisci quidem rerum. Dolorum assumenda similique ad consectetur molestiae sint, eos ipsum 
            itaque alias in praesentium eligendi, officiis sed! Modi totam, optio vero facilis commodi obcaecati ab,
            quibusdam eius corrupti vitae accusamus reprehenderit sapiente sunt placeat nostrum eligendi enim labore 
            nihil doloremque saepe consequatur illo? Pariatur, minima voluptatem repudiandae nemo quae fugit veniam 
            accusantium ex commodi ullam enim earum dolor totam aspernatur corrupti libero quos minus vero reprehenderit id.
              Officia porro recusandae quia magni numquam accusantium saepe sit, aliquid eveniet quasi, in optio mollitia doloribus 
              fuga veritatis vero perspiciatis fugit dignissimos eaque ratione necessitatibus ducimus laudantium beatae.
              Perspiciatis, non molestias optio consequuntur numquam ratione repudiandae cum consequatur nisi 
              necessitatibus vitae veritatis pariatur doloremque, possimus quis reprehenderit fugiat dolores, excepturi 
             r eum, unde voluptas quisquam voluptatum.''' + str(i)
      })
  for i in range(4):
    answers.append({'title': 'title'  + str(i),'id': i, 'text': '''Lorem ipsuia porro recusandae quia magni numquam accusantium saepe sit, aliquid eveniet quasi, in optio mollitia doloribus 
              fuga veritatis vero perspiciatis fugit dignissimos eaque ratione necessitatibus ducimus laudantium beatae.
              Perspiciatis, non molestias optio consequuntur numquam ratione repudiandae cum consequatur nisi 
              necessitatibus vitae veritatis pariatur doloremque, possimus quis reprehenderit fugiat dolores, excepturi 
             r eum, unde voluptas quisquam voluptatum.'''})
  return questions, answers

def paginate(objects, number):
  p=Paginator(objects, 5)
  return p.page(number)
def index(request):
  page=request.GET.get('page',1)
  questions, answers=f()
  currect_questions=paginate(questions,page)
  return render(request,'index.html',{'page': page, 'questions': currect_questions, 'answers': answers})

def ask(request):
  return render(request,'ask.html')

def questions(request, question_id):
  return render(request,'question.html')

def register(request):
  return render(request,'register.html')

def login(request):
  return render(request,'login.html')

def tag_questions(request):
  return render (request, 'tag_questions.html')

def settings(request):
  return render (request, 'settings.html') 

def pageNotFound(request, exception):
  template = loader.get_template('notFound.html')
  return HttpResponseNotFound(template.render(request))


  
