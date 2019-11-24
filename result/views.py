from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def result_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello this is result page</h1>")
