from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    #url(r'^home/$', views.home, name='home'),
    #url(r'^database/$', views.home, name='database'),
    url(r'^enter/$', views.enter, name='enter'),
    url(r'^report/$', views.report, name='report'),
    url(r'^enter1/$', views.enter1, name='enter1'),
    url(r'^enter2/$', views.enter2, name='enter2'),
    url(r'^enter3/$', views.enter3, name='enter3'),
    url(r'^displays/$', views.displays,name='displays'),


]