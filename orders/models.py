from django.conf import settings
from django.db import models
from django.db.models import Q, Sum

from patient.models import Patient


class Product(models.Model):
    name = models.CharField(max_length=64,
                            verbose_name="Nombre")
    price = models.DecimalField(max_digits=32,
                                decimal_places=2,
                                verbose_name="Precio")
    is_glass = models.BooleanField(verbose_name="Lente", default=False)
    POS = (
        ('IZQ', 'Izquierda'),
        ('DER', 'Derecha'),
    )
    position = models.CharField(verbose_name="Posición",
                                max_length=3,
                                choices=POS,
                                blank=True,
                                null=True)
    TYPE = (
        ('LEJ', 'Lejos'),
        ('CER', 'Cerca'),
    )
    type = models.CharField(verbose_name="Tipo",
                            max_length=3,
                            choices=TYPE,
                            blank=True,
                            null=True)
    frame = models.BooleanField(verbose_name="Armazon",
                                blank=True,
                                null=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.name} - $ {self.price}"


class Order(models.Model):
    products = models.ManyToManyField(Product,
                                      verbose_name="Productos",
                                      related_name="Productos",
                                      blank=False,
                                      null=False)
    patient = models.ForeignKey(Patient,
                                on_delete=models.CASCADE,
                                verbose_name="Paciente")
    seller = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               limit_choices_to=Q(groups__name='Vendedor'),
                               related_name="Vendedor",
                               verbose_name="Vendedor")
    date = models.DateTimeField(auto_now=True,
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
    payment_method = models.CharField(verbose_name="Metodo de Pago",
                                      max_length=4,
                                      choices=METHODS,
                                      default='EFEC')

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    @property
    def total_price(self):
        total = 0
        for productPrice in self.products.all():
            total += productPrice.price
        return total
