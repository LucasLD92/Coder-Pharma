from django.contrib import admin
from django.urls import path
from App_DROGUERIA.views import Inicio 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio),
]
