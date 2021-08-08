from django.db import models


# Create your models here.

class Type(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="nombre")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipo"
        db_table = "tipo"
        ordering = ["id"]


class Categoria(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="nombre")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ["id"]


class Empleado(models.Model):
    categ = models.ManyToManyField(Categoria)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique=True, verbose_name="Cedula")
    date_joined = models.DateField(auto_now_add=True, verbose_name="Fecha de registro")
    date_created = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=0)
    state = models.BooleanField(default=True)
    # gender = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)  # Valores nulos
    cvitae = models.FileField(upload_to='cv/%Y/%m/%d')

    # Reprecentacion de toString

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleado"
        db_table = "empleado"
        ordering = ["id"]
