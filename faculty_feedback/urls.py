"""faculty_feedback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from appOne import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^analytics/$', views.analytics, name='analytics'),
    url(r'^teacher_analytics/$', views.teacher_analytics, name='teacher_analytics'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.logIn, name='login'),
    url(r'^logout/$', views.logOut, name='logout'),
    url(r'^teacher_signup/$', views.teacherSignup, name="teacher_signup"),
    url(r'^teacher_login/$', views.teacherLogin, name="teacher_login"),

]
