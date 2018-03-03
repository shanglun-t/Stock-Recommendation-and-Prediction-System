from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .forms import brief_form
from .forms import full_form

# Create your views here.
def q_start(request):
    return render(request, 'q_start.html')

def B_form(request):
    if request.method == 'POST':
        form = brief_form(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = brief_form()
    return render(request, 'q_formB.html', {'form': form})

def F_form(request):
    if request.method == 'POST':
        form = full_form(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = full_form()
    return render(request, 'q_formF.html', {'form': form})

def home(request):
    return render(request, 'start.html')

def q_disclaimer(request):
    return render(request, 'q_disclaimer.html')

#def q_01(request):
    #return render(request, 'q_01.html')

#def q_02(request):
    #return render(request, 'q_02.html')

#def q_03(request):
    #return render(request, 'q_03.html')

#def q_04(request):
    #return render(request, 'q_04.html')

#def q_05A(request):
    #return render(request, 'q_05A.html')

#def q_05B(request):
    #return render(request, 'q_05B.html')

#def q_05C(request):
    #return render(request, 'q_05C.html')

#def q_05D(request):
    #return render(request, 'q_05D.html')


