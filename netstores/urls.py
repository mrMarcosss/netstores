from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'persons/', include('person.urls')),
    url(r'stores/', include('store.urls')),
    url(r'places/', include('place.urls')),
    url(r'storages/', include('storage.urls')),
]
