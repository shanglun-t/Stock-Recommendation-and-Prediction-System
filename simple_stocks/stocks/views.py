# for sector calcualtions

from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .forms import *
from .stock import *
import datetime



#import forms

class HomeView(TemplateView):
    template_name = 'stocks/start.html'
    def get(self, request):
        return render(request, self.template_name)

class q_disclaimer(TemplateView):
    template_name = 'stocks/q_disclaimer.html'
    def get(self, request):
        return render(request, self.template_name)


class q_start(TemplateView):
    template_name = 'stocks/q_start.html'
    def get(self, request):
        return render(request, self.template_name)

class getFormSelection ():
    def __init__(self, B1, B2):
        self.B1 = B1
        self.B2 = B2

    def get_B1(self):
        return self.__B1

    def set_B1(self, B1):
        self.__B1 = B1

    def get_B2(self):
        return self.__B2

    def set_B2(self, B2):
        self.__B2 = B2

tada = getFormSelection('out', 'out')
tada.set_B1('this is out')
form = None

class B_form(TemplateView):
    template_name = 'stocks/q_formB.html'


    def get(self, request):
        form = brief_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = brief_form(request.POST)
        if form.is_valid():
            time = form.cleaned_data['B1']
            risk = form.cleaned_data['B2']
            print (time, risk)
            self.result_B =  StockSelection(time, risk)
            self.resultList = self.result_B.getSelectedStockList()
        return render(request,'stocks/q_resultB.html', {'resultList': self.resultList})




