from django.http import HttpResponse
from django.shortcuts import render
from .models import Disease
from aima.logic import *

# Create your views here.
def result_view(request, *args, **kwargs):
    symptoms = []
    diseases = Disease.objects.all()
    for x in range(1,22):
        if(request.GET['answer' + str(x)] != ''):
            symptoms.append(request.GET['answer' + str(x)])
    return render(request, "result.html", {'diseases' : diseases})
