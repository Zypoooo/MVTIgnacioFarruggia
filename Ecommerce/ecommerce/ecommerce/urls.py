from django.contrib import admin
from django.urls import path
from ecommerce.views import padre_template, madre_template, hijo_template


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('padre_template/', padre_template, name='padre_template'),
    path('madre_template/', madre_template, name='madre_template'),
    path('hijo_template/', hijo_template, name='hijo_template')
]