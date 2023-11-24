from django.shortcuts import render

# Create your views here.
def balu(request):
    return render(request,'balu.html')

def venky(request):
    return render(request,'venky.html')