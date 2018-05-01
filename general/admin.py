from django.contrib import admin

# Register your models here.
from .models import Brand, BrandTestimonial, Employee, WarriorMediaImage, WarriorMediaVideo

class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'slug', 'template_name','site_url','updated','active')
    search_fields = ['brand_name']

    class meta:
        model = Brand

class BrandTestimonialAdmin(admin.ModelAdmin):
    list_display = ('testimonial_by', 'brand', 'active')
    search_fields = ['testimonial_by', 'brand']

    class meta:
        model = BrandTestimonial

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position','display_order', 'active','created')
    search_fields = ['first_name', 'last_name']

    class meta:
        model = Employee

class WarriorMediaImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description','active')

    class meta:
        model = WarriorMediaImage

class WarriorMediaVideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description','wistia_id','active')
    class meta:
        model = WarriorMediaVideo


admin.site.register(Brand, BrandAdmin)
admin.site.register(BrandTestimonial, BrandTestimonialAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(WarriorMediaImage, WarriorMediaImageAdmin)
admin.site.register(WarriorMediaVideo,WarriorMediaVideoAdmin)