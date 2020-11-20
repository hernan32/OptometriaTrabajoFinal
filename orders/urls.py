from django.conf.urls import url

from appointments.decorators import group_required
from .views import *

urlpatterns = [
    url(r'^pedidos/$', group_required('Vendedor')(OrderList.as_view()), name='list'),
    url(r'^catalogo/$', group_required('Vendedor')(ProductList.as_view()), name='catalog'),
    url(r'^catalogo/nuevo$', group_required('Vendedor')(ProductCreation.as_view()), name='product_new'),
    url(r'^catalogo/editar/(?P<pk>\d+)$', group_required('Vendedor')(ProductUpdate.as_view()), name='product_edit'),
    url(r'^catalogo/borrar/(?P<pk>\d+)$', group_required('Vendedor')(ProductDelete.as_view()), name='product_delete'),
    url(r'^(?P<pk>\d+)$', group_required('Vendedor')(OrderDetail.as_view()), name='detail'),
    url(r'^nuevo$', group_required('Vendedor')(OrderCreation.as_view()), name='new'),
    url(r'^editar/(?P<pk>\d+)$', group_required('Vendedor')(OrderUpdate.as_view()), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', group_required('Vendedor')(OrderDelete.as_view()), name='delete'),
]
