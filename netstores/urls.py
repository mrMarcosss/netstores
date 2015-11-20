from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.flatpages.views import flatpage
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.i18n import javascript_catalog, set_language

urlpatterns = [
    url(r'^$', cache_page(15*60)(TemplateView.as_view(template_name='base.html')), name='main_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'persons/', include('person.urls')),
    url(r'stores/', include('store.urls')),
    url(r'places/', include('place.urls')),
    url(r'storages/', include('storage.urls')),

    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', javascript_catalog, name='jsi18n'),
    url(r'^jsi18n/set_lang/$', csrf_exempt(set_language), name='set_language'),

    url(r'^pages(?P<url>.*)$', flatpage, name='flatpage')
]
