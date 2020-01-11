# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asistente(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='Cedula', max_length=10)  # Field name made lowercase.
    nombre1 = models.CharField(db_column='Nombre1', max_length=15)  # Field name made lowercase.
    nombre2 = models.CharField(db_column='Nombre2', max_length=15)  # Field name made lowercase.
    apellido1 = models.CharField(db_column='Apellido1', max_length=15)  # Field name made lowercase.
    apellido2 = models.CharField(db_column='Apellido2', max_length=15)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=10)  # Field name made lowercase.
    gmail = models.CharField(db_column='Gmail', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asistente'


class Clientes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='Cedula', max_length=10)  # Field name made lowercase.
    nombre1 = models.CharField(db_column='Nombre1', max_length=15)  # Field name made lowercase.
    nombre2 = models.CharField(db_column='Nombre2', max_length=15)  # Field name made lowercase.
    apellido1 = models.CharField(db_column='Apellido1', max_length=15)  # Field name made lowercase.
    apellido2 = models.CharField(db_column='Apellido2', max_length=15)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=10)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=40)  # Field name made lowercase.
    gmail = models.CharField(db_column='Gmail', max_length=30)  # Field name made lowercase.
    fecha_nacimiento = models.DateField(db_column='Fecha Nacimiento')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'clientes'



class Herramientas(models.Model):
    codigo = models.AutoField(db_column='Codigo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    disponibilidad = models.IntegerField(db_column='Disponibilidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'herramientas'


class Odontologos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='Cedula', max_length=10)  # Field name made lowercase.
    nombre1 = models.CharField(db_column='Nombre1', max_length=15)  # Field name made lowercase.
    nombre2 = models.CharField(db_column='Nombre2', max_length=15)  # Field name made lowercase.
    apellido1 = models.CharField(db_column='Apellido1', max_length=15)  # Field name made lowercase.
    apellido2 = models.CharField(db_column='Apellido2', max_length=15)  # Field name made lowercase.
    titulo_academico = models.CharField(db_column='Titulo Academico', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    telefono = models.CharField(db_column='Telefono', max_length=10)  # Field name made lowercase.
    gmail = models.CharField(db_column='Gmail', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'odontologos'


class Pedidos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    herramienta = models.ForeignKey(Herramientas, models.DO_NOTHING, db_column='Herramienta')  # Field name made lowercase.
    proveedor = models.ForeignKey('Proovedores', models.DO_NOTHING, db_column='Proveedor')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedidos'


class Proovedores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proovedores'


class Reservas(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    fecha_consulta = models.DateField(db_column='Fecha Consulta')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hora = models.DateTimeField(db_column='Hora')  # Field name made lowercase.
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='Cliente')  # Field name made lowercase.
    odontologo = models.ForeignKey(Odontologos, models.DO_NOTHING, db_column='Odontologo')  # Field name made lowercase.
    asistente = models.ForeignKey(Asistente, models.DO_NOTHING, db_column='Asistente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reservas'

class Servicios(models.Model):
    Id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    precio = models.FloatField(db_column='Precio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'herramientas'

class Detalle_reservas(models.Model):
    num_Reserva = models.ForeignKey(Reservas, models.DO_NOTHING, db_column='Id')
    Id_servicio = models.ForeignKey(Servicios, models.DO_NOTHING, db_column='Id')  # Field name made lowercase.
    tratamiento = models.CharField(db_column='Tratamiento', max_length=100)  # Field name made lowercase.
    medicamento = models.CharField(db_column='Medicamento', max_length=100)  # Field name made lowercase.
    instrucciones = models.CharField(db_column='Instrucciones', max_length=100)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'detalle_reservas'