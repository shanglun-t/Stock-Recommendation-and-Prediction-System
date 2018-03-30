# for sector calcualtions

from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .forms import *
from .stock import *
<<<<<<< HEAD
from .prediction import *
=======
>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab
import datetime



#import forms

class HomeView(TemplateView):
<<<<<<< HEAD
    template_name = 'stocks/home.html'
    def get(self, request):
        return render(request, self.template_name)


class AboutView(TemplateView):
    template_name = 'stocks/about.html'
    def get(self, request):
        return render(request, self.template_name)

class ContactView(TemplateView):
    template_name = 'stocks/contact.html'
=======
    template_name = 'stocks/start.html'
    def get(self, request):
        return render(request, self.template_name)

class q_disclaimer(TemplateView):
    template_name = 'stocks/q_disclaimer.html'
    def get(self, request):
        return render(request, self.template_name)


class q_start(TemplateView):
    template_name = 'stocks/q_start.html'
>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab
    def get(self, request):
        return render(request, self.template_name)


<<<<<<< HEAD
class q_disclaimer(TemplateView):
    template_name = 'stocks/q_disclaimer.html'
    def get(self, request):
        return render(request, self.template_name)


class q_start(TemplateView):
    template_name = 'stocks/q_start.html'
    def get(self, request):
        return render(request, self.template_name)


=======
>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab
class B_form(TemplateView):
    template_name = 'stocks/q_formB.html'


    def get(self, request):
        form = brief_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
<<<<<<< HEAD

=======
>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab
        form = brief_form(request.POST)
        if form.is_valid():
            time = form.cleaned_data['B1']
            risk = form.cleaned_data['B2']
<<<<<<< HEAD
            self.result_B =  StockSelection(time, risk)
            self.resultList = self.result_B.getSelectedStockList()
            self.predictionObj = StockPrediction(self.resultList)
            self.predictionList = self.predictionObj.getStockPrediction()
        return render(request,'stocks/q_resultB.html', {'resultList': self.resultList, 'predictionList': self.predictionList })
=======
            self.result_B =  StockSelection(time, time)
            self.resultList = self.result_B.getSelectedStockList()
        return render(request,'stocks/q_resultB.html', {'resultList': self.resultList})

>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab



class F_form(TemplateView):
    template_name = 'stocks/q_formF.html'


    def get(self, request):
        form = full_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = full_form(request.POST)
        if form.is_valid():
            time = form.cleaned_data['F1']
            risk = form.cleaned_data['F2']
            industryList = form.cleaned_data['F3']
<<<<<<< HEAD
            self.result_B =  StockSelection(time, risk)
            self.resultList = self.result_B.getUserSelectedStockList(industryList)
            self.predictionObj = StockPrediction(self.resultList)
            self.predictionList = self.predictionObj.getStockPrediction()
        return render(request,'stocks/q_resultB.html', {'resultList': self.resultList, 'predictionList': self.predictionList})
=======
            self.result_B =  StockSelection(time, time)
            self.resultList = self.result_B.getUserSelectedStockList(industryList)

        return render(request,'stocks/q_resultB.html', {'resultList': self.resultList, 'industryList': industryList})

>>>>>>> 564850d547b22da8f2fff1a2f2fd569ee6eb5fab
