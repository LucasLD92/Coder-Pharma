from django.contrib import admin
from django.urls import path
from App_DROGUERIA.views import (Inicio, Productos, Contacto,
AcercadeCoderPharma, Directorio, Empleados, Proveedores, Clientes,
AgregaProducto, AgregaCliente, AgregaProveedor, AgregaEmpleado, ORIGEN,
BusquedaProducto, BuscarProducto, BusquedaProveedor, BuscarProveedor, EditaProveedor, EliminaProveedor,
EditaProducto, EliminaProducto, EditaEmpleado, EliminaEmpleado
)
from .views import EditaCliente, EliminaCliente



urlpatterns = [
    path('', Inicio, name = "01_Inicio"),
    path('Productos', Productos, name = "02_Productos"),
    path('AgregaProducto', AgregaProducto, name = "02_AgregaProducto"),
    path('EditaProducto/<producto_id>', EditaProducto, name = "02_EditaProducto"),
    path('EliminaProducto/<producto_id>', EliminaProducto, name = "02_EliminaProducto"),
    path('Buscar-Producto', BuscarProducto, name = "02_BuscarProducto"), # Esta es la que sirve    
    path('Contacto', Contacto, name = "03_Contacto"),
    path('AcercadeCoder-Pharma', AcercadeCoderPharma, name = "04_AcercadeCoderPharma"),
    path('Directorio', Directorio, name = "05_Directorio"),
    path('Empleados', Empleados, name = "06_Empleados"),
    path('AgregaEmpleado', AgregaEmpleado, name = "06_AgregaEmpleado"),
    path('EditaEmpleado/<empleado_id>', EditaEmpleado, name = "06_EditaEmpleado"),
    path('EliminaEmpleado/<empleado_id>', EliminaEmpleado, name = "06_EliminaEmpleado"),
    path('Proveedores/', Proveedores, name = "07_Proveedores"),
    path('AgregaProveedor/', AgregaProveedor, name = "07_AgregaProveedor"),    
    path('EditaProveedor/<proveedor_id>', EditaProveedor, name = "07_EditaProveedor"),
    path('EliminaProveedor/<proveedor_id>', EliminaProveedor, name = "07_EliminaProveedor"),
    path('Buscar-Proveedor', BuscarProveedor, name = "07_BuscarProveedor"),        
    path('Clientes', Clientes, name = "08_Clientes"),
    path('AgregaCliente', AgregaCliente, name = "08_AgregaCliente"),
    path('EditaCliente/<cliente_id>', EditaCliente, name = "08_EditaCliente"),
    path('EliminaCliente/<cliente_id>', EliminaCliente, name = "08_EliminaCliente"),
    path('ORIGEN', ORIGEN),
]
