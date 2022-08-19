from django.contrib import admin
from django.urls import path
from App_DROGUERIA.views import (Inicio, Productos, Contacto,
AcercadeCoderPharma, Directorio, Empleados, Proveedores, Clientes,
AgregaProducto, AgregaCliente, AgregaProveedor, AgregaEmpleado, ORIGEN,
BuscarProducto, BuscarProveedor, BuscarCliente, BuscarEmpleado, ListaClientes
)

urlpatterns = [
    path('', Inicio, name = "01_Inicio"),
    path('Productos', Productos, name = "02_Productos"),
    path('AgregaProducto', AgregaProducto, name = "02_AgregaProducto"),
    path('Buscar-Producto', BuscarProducto, name = "02_BuscarProducto"), # Esta es la que sirve    
    path('Contacto', Contacto, name = "03_Contacto"),
    path('AcercadeCoder-Pharma', AcercadeCoderPharma, name = "04_AcercadeCoderPharma"),
    path('Directorio', Directorio, name = "05_Directorio"),
    path('Empleados', Empleados, name = "06_Empleados"),
    path('AgregaEmpleado', AgregaEmpleado, name = "06_AgregaEmpleado"),
    path('Buscar-Empleado', BuscarEmpleado, name = "06_BuscarEmpleado"),
    path('Proveedores', Proveedores, name = "07_Proveedores"),
    path('AgregaProveedor', AgregaProveedor, name = "07_AgregaProveedor"),    
    path('Buscar-Proveedor', BuscarProveedor, name = "07_BuscarProveedor"),        
    path('Clientes', Clientes, name = "08_Clientes"),
    path('AgregaCliente', AgregaCliente, name = "08_AgregaCliente"),
    path('Buscar-Cliente', BuscarCliente, name = "08_BuscarCliente"),
    path('ListaClientes', ListaClientes , name = "08_VistaCliente"),
    path('ORIGEN', ORIGEN),
]
