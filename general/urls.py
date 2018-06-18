
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static



from .views import (
	general_main,
	general_about,
	general_brands,
    general_term,
    general_privacy

)


urlpatterns = [
    url(r'^$', general_main, name="home"),
    url(r'^about/$', general_about, name="about"),
    url(r'^terms/$', general_term, name="term"),
    url(r'^privacy-policy/$', general_privacy, name="privacy"),

    url(r'^brands/(?P<slug>[-\w]+)/$', general_brands, name="brands"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
