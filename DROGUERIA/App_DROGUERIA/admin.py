from django.contrib import admin
from App_DROGUERIA.models import DIRECTORIO, EMPLEADO,PRODUCTO,PROVEEDORES,CLIENTES

# Register your models here.
admin.site.register(DIRECTORIO)
admin.site.register(EMPLEADO)
admin.site.register(PRODUCTO)
admin.site.register(PROVEEDORES)
admin.site.register(CLIENTES)
