"""Defines URL patterns for stocks"""

from django.conf.urls import url
from . import views

urlpatterns = [
    #Home page
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    #Disclaimer
    url(r'^q_disclaimer/$', views.q_disclaimer, name='q_disclaimer'),
    #Questionnaire
    url(r'^q_start/$', views.q_start, name='q_start'),
    url(r'^q_formB/$', views.B_form, name='q_formB'),
    url(r'^q_formF/$', views.F_form, name='q_formF'),
    
    #url(r'^q_01', views.q_01, name='q_01'),
    #url(r'^q_02', views.q_02, name='q_02'),
    #url(r'^q_03', views.q_03, name='q_03'),
    #url(r'^q_04', views.q_04, name='q_04'),
    #url(r'^q_05A', views.q_05A, name='q_05A'),
    #url(r'^q_05B', views.q_05A, name='q_05B'),
    #url(r'^q_05C', views.q_05A, name='q_05C'),
    #url(r'^q_05D', views.q_05A, name='q_05D'),
]