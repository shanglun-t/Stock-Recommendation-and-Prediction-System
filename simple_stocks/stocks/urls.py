"""Defines URL patterns for stocks"""
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    url(r'^q_resultB/$',views.q_resultB, name='q_resultB'),
    url(r'^q_resultF/$',views.q_resultF, name='q_resultF'),  
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
