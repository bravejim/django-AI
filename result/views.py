from django.http import HttpResponse
from django.shortcuts import render
from .models import Disease
from logic import *

disease_kb = FolKB([
    expr('(Mengalami(x,G01) & Mengalami(x,G02) & Mengalami(x,G03) & Mengalami(x,G04)) ==> Terjangkit(x,P01)'),
    expr('(Mengalami(x,G01) & Mengalami(x,G02) & Mengalami(x,G05) & Mengalami(x,G06) & Mengalami(x,G07) & Mengalami(x,G14) & Mengalami(x,G15) & Mengalami(x,G16)) ==> Terjangkit(x,P02)'),
    expr('(Mengalami(x,G08) & Mengalami(x,G09) & Mengalami(x,G10) ) ==> Terjangkit(x,P03)'),
    expr('(Mengalami(x,G11) & Mengalami(x,G12)) ==> Terjangkit(x,P04)'),
    expr('(Mengalami(x,G13) & Mengalami(x,G14)) ==> Terjangkit(x,P05)'),
    expr('(Mengalami(x,G15) & Mengalami(x,G16) & Mengalami(x,G17)) ==> Terjangkit(x,P06)'),
    expr('(Mengalami(x,G08) & Mengalami(x,G18) & Mengalami(x,G19) & Mengalami(x,G20)) ==> Terjangkit(x,P07)'),
    expr('(Mengalami(x,G21) & Mengalami(x,G22)) ==> Terjangkit(x,P08)'),
])

# Create your views here.
def result_view(request, *args, **kwargs):
    symptoms = []
    diseases = Disease.objects.all()
    for x in range(1,23):
        if(request.GET['answer' + str(x)] != ''):
            symptoms.append(request.GET['answer' + str(x)])
    for i in symptoms:
        disease_kb.tell(expr('Mengalami(Alex,' + i + ')'))
    result = check()
    print(result)
    for i in symptoms:
        disease_kb.retract(expr('Mengalami(Alex,' + i + ')'))
    return render(request, "result.html", {'diseases' : diseases, 'result' : result})

def check():
    return disease_kb.ask(expr('Terjangkit(Alex,x)'))[x]
