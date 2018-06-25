from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand, BrandTestimonial, Employee, WarriorMediaImage
from .forms import ContactForm



# Create your views here.
def general_main(request):
    context = {}
    # Get Brands to display in the "BRANDS" section
    brand_list = Brand.objects.filter(active=True)
    form_class = ContactForm

    context.update({
        'brands': brand_list,
        'form': form_class,
    })
    return(render(request, 'general/main.htm', context))

def general_immersion(request):
    context = {}

    return(render(request, 'general/immersion.htm', context))

def general_summer(request):
    context = {}
    # warriors = Employee.objects.filter(active=True).order_by('display_order','last_name')
    # print("EMPLOYEE OBJ : ", warriors)
    # # Filter out Executives from Employees object
    # warriors_leaders = Employee.objects.filter(active=True, executive=True).order_by('display_order')
    # warriors = Employee.objects.filter(active=True, executive=False).order_by('department','display_order','first_name')
    # images = WarriorMediaImage.objects.filter(active=True).order_by('display_order')[:25]
    # context.update({
    #     "warriors_leaders":warriors_leaders,
    #     "warriors": warriors,
    #     "images": images,
    # })

    return(render(request, 'general/summer.htm', context))


def general_school_year(request):
    context = {}
    return(render(request, 'general/privacy.htm', context))

def general_programs(request):
    context = {}
    return(render(request, 'general/privacy.htm', context))