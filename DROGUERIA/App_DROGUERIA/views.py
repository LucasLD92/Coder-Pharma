from django.shortcuts import render
from django.http import HttpResponse
from App_DROGUERIA.models import DIRECTORIO, EMPLEADO,PRODUCTO,PROVEEDORES,CLIENTES
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# //////// Visualizacion de Templates ////////
def ORIGEN (request):
    return render(request, "00 - ORIGEN.html")
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

def ListaClientes(request):
    clientes = CLIENTES.objects.all()
    contexto = {"clientes": clientes}
    return render(request, "08 - VistaClientes.html", contexto)
    
# Edita Cliente
# Elimina Cliente
# Buscar Cliente <- 14/08_Lucas: Listo! Funciona :) - FALTA PULIR DETALLES.
def BuscarCliente(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cliente = CLIENTES.objects.filter(nombre__icontains=nombre)
        return render(request,"08 - BusquedaResultado.html", {"cliente": cliente, "nombre": nombre})
    else:
        resultado = "No hay resultados"
    return HttpResponse(resultado)



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
# Buscar Proveedor <- 14/08_Lucas: Listo! Funciona :) - FALTA PULIR DETALLES.
def BuscarProveedor(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        proveedor = PROVEEDORES.objects.filter(nombre__icontains=nombre)
        return render(request,"07 - BusquedaResultado.html", {"proveedor": proveedor, "nombre": nombre})
    else:
        resultado = "No hay resultados"
    return HttpResponse(resultado)

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
# Buscar Producto <- 14/08_Lucas: Listo! Funciona :) - FALTA PULIR DETALLES.
def BuscarProducto(request):
    if request.GET["monodroga"]:
        monodroga = request.GET["monodroga"]
        producto = PRODUCTO.objects.filter(monodroga__icontains=monodroga)
        return render(request,"02 - BusquedaResultado.html", {"producto": producto, "monodroga": monodroga})
    else:
        resultado = "No hay resultados"
    return HttpResponse(resultado)

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
# Edita Empleado
# Elimina Empleado
# Buscar Empleado <- 14/08_Lucas: Listo! Funciona :) - FALTA PULIR DETALLES.
def BuscarEmpleado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        empleado = EMPLEADO.objects.filter(nombre__icontains=nombre)
        return render(request,"06 - BusquedaResultado.html", {"empleado": empleado, "nombre": nombre})
    else:
        resultado = "No hay resultados"
    return HttpResponse(resultado)

def LoginView(request):
    if request.method == 'POST':
        miFormulario = AuthenticationForm(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]
            user = authenticate(username=usuario, password=psw)

            if user:
                login(request, user)
                return render(request, "01 - Inicio.html", {"mensaje": f'Bienvenido {usuario}'})


            return render(request, "01 - Inicio.html")
