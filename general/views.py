from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def general_main(request):
    return(render(request, 'general/main.htm'))

def general_brands(request):
    context = {}
    template_name = 'brand_template.htm'
    context.update({
        'brand_name': 'Brand Name',
        'brand_owner': 'Brand Owner',
        'brand_url': 'Brand Url',
        'blurb_content': 'Curabitur imperdiet lectus quis iaculis tristique. Aliquam efficitur ipsum eget nibh mollis, et lobortis sapien elementum. Nulla vitae ex tempus, tristique justo ut, varius urna. Ut nisi eros, rutrum non imperdiet ut, tempor id metus. Etiam quam lorem, feugiat vel elit vel, volutpat viverra orci. Morbi lorem nisl, egestas id lacinia vitae, maximus non enim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae'
    })
    print("Context: ", context)
    return(render(request, 'include/brand/' + template_name, context))

def general_about(request):
    context = {}
    return(render(request, 'general/about.htm', context))


def get_brand(request):
    return True