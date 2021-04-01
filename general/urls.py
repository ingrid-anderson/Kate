
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static



from .views import (
	general_main,
	general_immersion,
    	general_events,
    	general_school_year,
    	general_programs,
	general_newpage

)


urlpatterns = [
    url(r'^$', general_main, name="home"),
    url(r'^new-students/$', general_immersion, name="immersion"),
    url(r'^events/$', general_events, name="events"),
    url(r'^existing-students/$', general_school_year, name="school_year"),
    url(r'^programs/$', general_programs, name="programs"),
    url(r'^newpage/$', general_newpage, name="newpage"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
