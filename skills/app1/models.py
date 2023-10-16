from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'categoria'


class Ingrediente(models.Model):
    id_ingrediente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'ingrediente'


class Orden(models.Model):
    id_orden = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'orden'


class OrdenPlatillo(models.Model):
    id = models.IntegerField(primary_key=True)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, blank=True, null=True)
    platillo = models.ForeignKey('Platillo', on_delete=models.CASCADE, blank=True, null=True)
    cantidad_platillo = models.IntegerField(blank=True, null=True)
    total_platillo = models.IntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'orden_platillo'


class Platillo(models.Model):
    id_platillo = models.IntegerField(primary_key=True)
    nombre_platillo = models.CharField(max_length=30, blank=True, null=True)
    costo = models.IntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'platillo'


class PlatilloIngrediente(models.Model):
    id = models.IntegerField(primary_key=True)
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE, blank=True, null=True)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'platillo_ingrediente'