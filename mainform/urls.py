from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name="index")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

admin.site.site_title = 'Book Site'
admin.site.index_title= 'Registration Site Administration'
admin.site.site_header = 'Registration Administration'
