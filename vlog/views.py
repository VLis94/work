from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def home(request):
    return HttpResponse('<h4> Привет </h4>')

class IndexView(TemplateView):
    template_name = "index.html"
