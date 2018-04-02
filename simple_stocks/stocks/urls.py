"""Defines URL patterns for stocks"""
from django.conf.urls import url
from stocks.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Home page
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^home/$', HomeView.as_view(), name='home'),


    #about page
    url(r'^about/$', AboutView.as_view(), name='about'),

    #contact page
    url(r'^contact/$', ContactView.as_view(), name='contact'),

    #Disclaimer page
    url(r'^q_disclaimer/$', q_disclaimer.as_view(), name='q_disclaimer'),

    #Questionnaire Page
    url(r'^q_start/$', q_start.as_view(), name='q_start'),


    url(r'^q_formB/$', B_form.as_view(), name='q_formB.'),
    url(r'^q_formF/$', F_form.as_view(), name='q_formF.'),

    ]
