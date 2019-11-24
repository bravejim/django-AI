from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
from pprint import pprint
# Create your views here.
def home_view(request, *args, **kwargs):
    questions = Question.objects.all()
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {'questions':questions})