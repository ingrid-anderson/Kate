from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand, BrandTestimonial, Employee



# Create your views here.
def general_main(request):
    context = {}
    # Get Brands to display in the "BRANDS" section
    brand_list = Brand.objects.filter(active=True)
    context.update({
        "brands": brand_list,
    })
    return(render(request, 'general/main.htm', context))

def general_brands(request, slug=None):
    context = {}

     # Get Brands to display in the "BRANDS" section
    brand = Brand.objects.filter(active=True, slug=slug).first()    
    template_name = brand.template_name

    testimonials = BrandTestimonial.objects.filter(brand_id=brand.pk, active=True)

    context.update({
        'brand_name': brand.brand_name,
        'brand_owner': brand.brand_owner,
        'brand_url': brand.site_url,
        'blurb_content': brand.content_blurb, 
        'testimonials': testimonials,
    })

    print("Context: ", context)
    return(render(request, 'include/brand/' + template_name, context))

def general_about(request):
    context = {}
    warriors = Employee.objects.filter(active=True).order_by('display_order','last_name')
    print("EMPLOYEE OBJ : ", warriors)
    context.update({
        "warriors": warriors,
    })


    return(render(request, 'general/about.htm', context))
    
def general_term(request):
    context = {}
    return(render(request, 'general/terms.htm', context))

def general_privacy(request):
    context = {}
    return(render(request, 'general/privacy.htm', context))