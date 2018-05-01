from django.db import models
from time import gmtime, strftime

def upload_location(instance, filename):
	date = strftime("%Y/%m", gmtime())
	return 'products/{0}/{1}'.format(date, filename)

# Create your models here.
class Brand(models.Model):
    brand_owner = models.CharField(max_length=254)
    brand_name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    template_name = models.CharField(max_length=255, null=True, blank=True)
    site_url = models.TextField(blank=True)
    content_blurb =  models.TextField(blank=True)
    image_thumbnail = models.ImageField(
                    upload_to=upload_location,
                    null=True,
                    blank=True,
                )
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.brand_name

    def __str__(self):
        return self.brand_name


class BrandTestimonial(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    testimonial_by = models.CharField(max_length=254, blank=False)
    content =  models.TextField(blank=True)
    image_testimonial = models.ImageField(
                    upload_to=upload_location,
                    null=True,
                    blank=True,
                )
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

class Employee(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    position = models.TextField(blank=True)
    image = models.ImageField(
                    upload_to=upload_location,
                    null=True,
                    blank=True,
                )
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    display_order = models.PositiveIntegerField(default=25)

    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.first_name
    def __str__(self):
        return self.first_name


class WarriorMediaImage(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
                    upload_to=upload_location,
                    null=True,
                    blank=True,
                )
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class WarriorMediaVideo(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True)
    wistia_id = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name