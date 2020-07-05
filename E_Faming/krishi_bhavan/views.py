from django.shortcuts import render
from django.views.generic import ListView, DetailView, View 
from django.http import HttpResponse

# Create your views here.

def HomeView(request):
    return render(request, "E-Faming.html")
    