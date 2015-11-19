from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.views.i18n import javascript_catalog, set_language
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'persons/', include('person.urls')),
    url(r'stores/', include('store.urls')),
    url(r'places/', include('place.urls')),
    url(r'storages/', include('storage.urls')),

    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', javascript_catalog, name='jsi18n'),
    url(r'^jsi18n/set_lang/$', csrf_exempt(set_language), name='set_language'),
]
