
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static



from .views import (
	general_main,
	general_immersion,
    general_summer,
    general_school_year,
    general_programs

)


urlpatterns = [
    url(r'^$', general_main, name="home"),
    url(r'^immersion/$', general_immersion, name="immersion"),
    url(r'^summer/$', general_summer, name="summer"),
    url(r'^school-year/$', general_school_year, name="school_year"),
    url(r'^programs/$', general_programs, name="programs"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
