from django.db import models
from django.forms import IntegerField

# Create your models here.
class DIRECTORIO(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()
    cargo = models.CharField(max_length=50)
    # Usuario = models.CharField(max_length=50)
class EMPLEADO(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()
    telefono = models.CharField(max_length=50)
    eMail = models.EmailField(max_length=50)
    puesto = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    horarioIngreso = models.TimeField()
    horarioSalida = models.TimeField()
    # Usuario = models.CharField(max_length=50)
class PRODUCTO(models.Model):
    monodroga = models.CharField(max_length=50)
    marca = models.CharField(max_length=50) # Del laboratorio productor - Ej. Rivero, Drawer, Klonal, Bayer, Bago, etc.
    presentacion = models.CharField(max_length=50) # Presentacion de la caja/BLISTER - Ej.: BLISTER x 15 Comp / CAJA x 100 Ampollas  
    formFarmaceutica = models.CharField(max_length=50) # Comprimido, Capsula, Sachet, Ampolla, Frasco Ampolla, etc.
    certificado = models.IntegerField() # ANMAT
    codigoProducto = models.CharField(max_length=50)
    stock = models.IntegerField()

class PROVEEDORES(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    razonSocial = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()
    telefono = models.CharField(max_length=50)
    eMail = models.EmailField(max_length=50)
    form_pago = models.CharField(max_length=50)
    codigo_Proveedor = models.CharField(max_length=50)
    tipo_Cliente = models.CharField(max_length=50) # Clinica, Hospitales, Ministerios, Municipio, Gobierno Provincial, etc

class CLIENTES(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    razonSocial = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    codigoPostal = models.IntegerField()
    telefono = models.CharField(max_length=50)
    eMail = models.EmailField(max_length=50)
    form_pago = models.CharField(max_length=50)
    codigo_Cliente = models.CharField(max_length=50)