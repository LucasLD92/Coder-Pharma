from django.shortcuts import render
from django.http import HttpResponse
from App_DROGUERIA.models import DIRECTORIO, EMPLEADO,PRODUCTO,PROVEEDORES,CLIENTES

# Create your views here.

# //////// Visualizacion de Templates ////////
def Inicio(request):
    return render(request,"01 - Inicio.html")
def Productos(request):
    productos = PRODUCTO.objects.all()
    return render(request,"02 - Productos.html", {"Vademecum": productos})
def Contacto (request):
    return render(request,"03 - Contacto.html")
def AcercadeCoderPharma (request):
    return render(request,"04 - AcercadeCoderPharma.html")
def Directorio (request):
    return render(request,"05 - Directorio.html")
def Empleados (request):
    empleados = EMPLEADO.objects.all()
    return render(request,"06 - Empleados.html", {"Personal": empleados})
def Proveedores (request):
    proveedores = PROVEEDORES.objects.all()
    return render(request,"07 - Proveedores.html", {"Proveedores": proveedores})
def Clientes (request):
    clientes = CLIENTES.objects.all()
    return render(request,"08 - Clientes.html", {"Clientes": clientes})


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