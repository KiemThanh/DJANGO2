
# Create your views here.
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question


def index(request):
    return render(request, 'polls/index.html')









