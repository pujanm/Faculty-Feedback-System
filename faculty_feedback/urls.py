from django.conf.urls import url
from django.contrib import admin
from appOne import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^analytics/$', views.analytics, name='analytics'),
    url(r'^teacher_analytics/$', views.teacher_analytics, name='teacher_analytics'),
    url(r'^admin_analytics/$', views.admin_analytics, name='admin_analytics'),
    url(r'^admin_analytics/(?P<subject>[\w ]+)/$', views.admin_analytics_detailed, name="admin_analytics_detailed"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.logIn, name='login'),
    url(r'^logout/$', views.logOut, name='logout'),
    url(r'^teacher_signup/$', views.teacherSignup, name="teacher_signup"),
    url(r'^teacher_login/$', views.teacherLogin, name="teacher_login"),
    url(r'^teacher_names/(?P<subject>[\w ]+)/$', views.get_teacher_name, name="teacher_names"),
    url(r'^teacher_detailed/(?P<subject>[\w ]+)/$', views.teacher_detailed_analytics, name="teacher_detailed_analytics"),
    url(r'^get_subject_on_semester/(?P<semester>\d+)/$', views.get_subject_on_semester, name="get_subject_on_semester")

]
