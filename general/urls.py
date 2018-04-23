
from django.conf.urls import url
from django.contrib import admin


from .views import (
	general_main,
	general_about,
	general_brands,
)


urlpatterns = [
    url(r'^$', general_main, name="home"),
    url(r'^about/$', general_about, name="about"),
    url(r'^brands/$', general_brands, name="brands"),
]
