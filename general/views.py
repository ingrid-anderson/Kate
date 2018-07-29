from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm



# Create your views here.
def general_main(request):
    context = {}
    form_class = ContactForm
    return(render(request, 'general/main.htm', context))

def general_immersion(request):
    context = {}

    return(render(request, 'general/immersion.htm', context))

def general_summer(request):
    context = {}

    return(render(request, 'general/summer.htm', context))


def general_school_year(request):
    context = {}
    return(render(request, 'general/schoolyear.htm', context))

def general_programs(request):
    context = {}
    return(render(request, 'general/programs.htm', context))