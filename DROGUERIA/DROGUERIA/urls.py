from django.contrib import admin
from django.urls import path, include
from App_DROGUERIA.views import Inicio 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio, name = "Inicio"),
    path('App-Drogueria/', include("App_DROGUERIA.urls")),
]
