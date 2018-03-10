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

# for sector calcualtions
import csv
import sys
from collections import OrderedDict
import numpy as np
import scipy as sp
import itertools
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
            # calcualtion
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
            # calcualtion
            result_F = StockSelection(clean_F1, clean_F2, clean_F3)  
            print(form.cleaned_data['result_F'])
    else:
        form = full_result_form()
        
    return render(request, 'q_resultF.html', {'form': form})

# calculations

class SectorSelection:
    

    def __init__(self, holdingPeriod, riskLevel):
        self.holdingPeriod = holdingPeriod
        self.riskLevel = riskLevel



    # returns list of Sector with value in range of high and low
    def reduceByValue(self, low, high, myDict):
        result = list()
        for k, v in myDict.items():
                if float(v) >= low and float(v) <= high:
                    result.append (k)
                    
        return result
    
    # provides list of Sector based on volatility and risk chosen by the user 
    def getSectorList(self):
        sectorVolatility = dict()
        sectorRisk = dict()
        sectorReturn = dict()
        
        
        
        with open('/Users/shangluntsai/Capstone/simple_stocks/static/stocks/sector_performance.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)

            for row in reader:
                sectorVolatility[row[0]] = row[1]
                sectorRisk[row[0]] = row[2]
                sectorReturn[row[0]] = row[3]
                
        low = min (float(sectorVolatility[k]) for k in sectorVolatility)
        high = max (float(sectorVolatility[k]) for k in sectorVolatility)
        diff = (high - low)/5
                
        print ('RANGE:', diff)
        print (low)

        if self.holdingPeriod == 'T1':
            pass
        if self.holdingPeriod == 'T2':
            low = low + diff 
        if self.holdingPeriod == 'T3':
            low = low + diff * 2
        if self.holdingPeriod == 'T4':
            low = low + diff * 3
        if self.holdingPeriod == 'T5':
            low = low + diff * 4
            
        high = low + diff
        
        result =self.reduceByValue(low, high ,sectorVolatility)

        

        sectorRisk = {k: sectorRisk[k] for k in result if k in sectorRisk}
        print ('list of risk', sectorRisk)

        low = min (float(sectorRisk[k]) for k in sectorRisk)
        high = max (float(sectorRisk[k]) for k in sectorRisk)
        diff = (high - low)/2

        if self.riskLevel == 'R1' or self.riskLevel == 'R2':
            pass
        if self.riskLevel == 'R3' or self.riskLevel == 'R4':
            low = low + diff 
            
        high = low + diff
        
        result =self.reduceByValue(low, high ,sectorRisk)

        

        sectorReturn = {k: sectorReturn[k] for k in result if k in sectorReturn}
        print ('list of return', sectorReturn)

        low = min (float(sectorReturn[k]) for k in sectorReturn)
        high = max (float(sectorReturn[k]) for k in sectorReturn)
        diff = (high - low)/2
            
        high = low + diff
        print (high, 'this is high for return')

        result = list()
        for k, v in sectorReturn.items():
                if float(v) > high:
                    result.append (k)
        
        
        return 'result of return', result


    
                 
class IndustrySelection:
    pass
class StockSelection:
    pass


S1 = SectorSelection ('T2', 'R3')
print (S1.getSectorList())


