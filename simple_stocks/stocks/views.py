from django.shortcuts import render 
from django.shortcuts import redirect
from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import brief_form   
from .forms import full_form
from .forms import brief_result_form
from .forms import full_result_form
from .models import b_answers 
from .models import f_answers 
from .models import b_result 
from .models import f_result

# for calcualtions
import csv
import sys
from collections import OrderedDict
import numpy as np
import scipy as sp
import itertools
from stocks.sector import *
from stocks.performance import *
from stocks.industry import *
from stocks.DailyUpdate import *
from stocks.stock import *
#import forms 


# Create your views here.
def q_start(request):
    return render(request, 'q_start.html')


def B_form(request):
    if request.method == 'POST':
        form = brief_form(request.POST)
        if form.is_valid():
            clean_B1 = form.cleaned_data['B1']
            clean_B2 = form.cleaned_data['B2']
            return redirect('q_resultB', clean_B1 = 'clean_B1', clean_B2 = 'clean_B2')
            #cd = form.cleaned_data
            #return redirect('q_resultB', cd)
    else:
        form = brief_form()
        
    return render(request, 'q_formB.html', {'form': form})


def F_form(request):
    if request.method == 'POST':
        form = full_form(request.POST)
        if form.is_valid():
            clean_F1 = form.cleaned_data['F1']
            clean_F2 = form.cleaned_data['F2']
            clean_F3 = form.cleaned_data['F3']
            return redirect('q_resultF', clean_F1 = 'clean_F1', clean_F2 = 'clean_F2', clean_F3 = 'clean_F3')
    else:
        form = full_form()
        
    return render(request, 'q_formF.html', {'form': form})


def home(request):
    return render(request, 'start.html')


def q_disclaimer(request):
    return render(request, 'q_disclaimer.html')

# views of result pages

def q_resultB(request):   
    if request.method == 'POST':
        form = brief_form(request.POST)
        if form.is_valid():
            clean_B1 = form.cleaned_data['clean_B1']
            clean_B2 = form.cleaned_data['clean_B2']
            result_B = StockSelection(clean_B1, clean_B2) 
            print(form.cleaned_data['result_B'])
    else:
        form = brief_result_form()
        
    return render(request, 'q_resultB.html', {'form': form})


def q_resultF(request):   
    if request.method == 'POST':
        form = full_form(request.POST)
        if form.is_valid():
            clean_F1 = form.cleaned_data['clean_F1']
            clean_F2 = form.cleaned_data['clean_F2']
            clean_F3 = form.cleaned_data['clean_F3']
            result_F = StockSelection(clean_F1, clean_F2, clean_F3)  
            print(form.cleaned_data['result_F'])
    else:
        form = full_result_form()
        
    return render(request, 'q_resultF.html', {'form': form})














