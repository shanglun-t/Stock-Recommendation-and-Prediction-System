from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'start.html')

def q_01(request):
    return render(request, 'q_01.html')

def q_02(request):
    return render(request, 'q_02.html')

def q_03(request):
    return render(request, 'q_03.html')

def q_04(request):
    return render(request, 'q_04.html')

def q_05A(request):
    return render(request, 'q_05A.html')

def q_05B(request):
    return render(request, 'q_05B.html')

def q_05C(request):
    return render(request, 'q_05C.html')

def q_05D(request):
    return render(request, 'q_05D.html')

def q_disclaimer(request):
    return render(request, 'q_disclaimer.html')