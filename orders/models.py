from django.conf import settings
from django.db import models

from patient.models import Patient


class Product(models.Model):
    id = models.AutoField(primary_key=True,
                          unique=True)
    name = models.CharField(max_length=64,
                            verbose_name="Nombre")
    price = models.DecimalField(max_digits=32,
                                decimal_places=2,
                                verbose_name="Precio")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    products = models.ManyToManyField(Product,
                                      related_name="Productos")
    patient = models.ForeignKey(Patient,
                                on_delete=models.CASCADE,
                                verbose_name="Paciente")
    seller = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="Vendedor")
    date = models.DateTimeField(auto_now_add=True,
                                verbose_name="Fecha")
    STATUS = (
        ('PED', 'Pedido'),
        ('TAL', 'Taller'),
        ('PEN', 'Pendiente'),
    )
    status = models.CharField(max_length=3,
                              choices=STATUS,
                              default='PEN')
    METHODS = (
        ('CRED', 'Tarjeta de Credito'),
        ('DBTO', 'Tarjeta de Debito'),
        ('VIRT', 'Billetera Virtual'),
        ('EFEC', 'Efectivo')
    )
    payment_method = models.CharField(max_length=4,
                                      choices=METHODS,
                                      default='EFEC')

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
