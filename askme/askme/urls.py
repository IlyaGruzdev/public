"""
URL configuration for askme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.conf.urls.static import static

from django.urls import path, re_path
from django.conf import *           
from askmeApp import views
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name="home"),
    path('signup/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('ask/', views.ask, name="ask"),
    path('question/<int:question_id>/', views.question, name="question"),
    re_path(r'tag/(?P<name>[\w+ ./-]+)/', views.tag_questions, name="tag_questions"),
    path('settings/', views.settings, name='settings'),
    path('hot/', views.bestQuestions, name='hot')
]

handler404 = views.pageNotFound

if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)