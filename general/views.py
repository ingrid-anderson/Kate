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

def general_events(request):
    context = {}

    return(render(request, 'general/events.htm', context))


def general_school_year(request):
    context = {}
    return(render(request, 'general/schoolyear.htm', context))

def general_programs(request):
    context = {}
    return(render(request, 'general/programs.htm', context))