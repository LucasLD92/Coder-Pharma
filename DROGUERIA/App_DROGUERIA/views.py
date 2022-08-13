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
# Agrega Cliente <- 12/08_Lucas: Listo! funciona :) - FALTA PULIR DETALLES.
def AgregaCliente(request):
    if request.method == 'POST':
        cliente = CLIENTES(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            razonSocial=request.POST['razonSocial'],
            direccion=request.POST['direccion'],
            codigoPostal=request.POST['codigoPostal'],
            telefono=request.POST['telefono'],
            eMail=request.POST['eMail'],
            form_pago=request.POST['form_pago'],
            codigo_Cliente=request.POST['codigo_Cliente'],
            tipo_Cliente=request.POST['tipo_Cliente'])
        cliente.save()
        return render(request, "01 - Inicio.html")
    return render(request, "08 - AgregaCliente.html")
# Edita Cliente
# Elimina Cliente
# Buscar Cliente


# Agrega Proveedor <- 12/08_Lucas: Listo! funciona :) - FALTA PULIR DETALLES.
def AgregaProveedor(request):
    if request.method == 'POST':
        proveedor = PROVEEDORES(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            razonSocial=request.POST['razonSocial'],
            direccion=request.POST['direccion'],
            codigoPostal=request.POST['codigoPostal'],
            telefono=request.POST['telefono'],
            eMail=request.POST['eMail'],
            form_pago=request.POST['form_pago'],
            codigo_Proveedor=request.POST['codigo_Proveedor'],
            tipo_Cliente=request.POST['tipo_Cliente'])
        proveedor.save()
        
        return render(request, "01 - Inicio.html")

    return render(request, "07 - AgregaProveedor.html")
# Edita Proveedor
# Elimina Proveedor
# Buscar Proveedor


# Agrega Producto <- 12/08_Lucas: Listo! funciona :) - FALTA PULIR DETALLES.
def AgregaProducto(request):

    if request.method == 'POST':
        producto = PRODUCTO(
            monodroga=request.POST['monodroga'],
            marca=request.POST['marca'],
            presentacion=request.POST['presentacion'],
            formFarmaceutica=request.POST['formFarmaceutica'],
            certificado=request.POST['certificado'],
            codigoProducto=request.POST['codigoProducto'],
            stock=request.POST['stock'])
        producto.save()
        return render(request, "01 - Inicio.html")

    return render(request, "02 - AgregaProducto.html")
# Edita Producto
# Elimina Producto
# Buscar Producto

# Agrega Empleado <- 12/08_Lucas: Listo! funciona :) - FALTA PULIR DETALLES.
def AgregaEmpleado(request):

    if request.method == 'POST':
        empleado = EMPLEADO(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            direccion=request.POST['direccion'],
            codigoPostal=request.POST['codigoPostal'],
            telefono=request.POST['telefono'],
            eMail=request.POST['eMail'],
            puesto=request.POST['puesto'],
            cargo=request.POST['cargo'],
            horarioIngreso=request.POST['horarioIngreso'],
            horarioSalida=request.POST['horarioSalida'])
        empleado.save()
        return render(request, "01 - Inicio.html")

    return render(request, "06 - AgregaEmpleado.html")
# Edita Proveedor
# Elimina Proveedor
# Buscar Proveedor