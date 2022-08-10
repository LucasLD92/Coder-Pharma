from django.contrib import admin
from django.urls import path
from App_DROGUERIA.views import Inicio, Productos, Contacto, AcercadeCoderPharma, Directorio, Empleados, Proveedores, Clientes


urlpatterns = [
    path('', Inicio, name = "01_Inicio"),
    path('Productos', Productos, name = "02_Productos"),
    path('Contacto', Contacto, name = "03_Contacto"),
    path('AcercadeCoder-Pharma', AcercadeCoderPharma, name = "04_AcercadeCoderPharma"),
    path('Directorio', Directorio, name = "05_Directorio"),
    path('Empleados', Empleados, name = "06_Emplados"),
    path('Proveedores', Proveedores, name = "07_Proveedores"),
    path('Clientes', Clientes, name = "08_Clientes"),
]
