from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# //////// Visualizacion de Templates ////////
def Inicio(request):
    return render(request,"01 - Inicio.html")
def Productos(request):
    return render(request,"02 - Productos.html")
def Contacto (request):
    return render(request,"03 - Contacto.html")
def AcercadeCoderPharma (request):
    return render(request,"04 - AcercadeCoderPharma.html")
def Directorio (request):
    return render(request,"05 - Directorio.html")
def Empleados (request):
    return render(request,"06 - Empleados.html")
def Proveedores (request):
    return render(request,"07 - Proveedores.html")
def Clientes (request):
    return render(request,"08 - Clientes.html")


# //////// Funciones ////////
# Agrega Cliente
# Edita Cliente
# Elimina Cliente
# Buscar Cliente

# Agrega Proveedor
# Edita Proveedor
# Elimina Proveedor
# Buscar Proveedor

# Agrega Producto
# Edita Producto
# Elimina Producto
# Buscar Producto