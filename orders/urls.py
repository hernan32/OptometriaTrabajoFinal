from django.conf.urls import url
from django.urls import path

from appointments.decorators import group_required
from .views import *

urlpatterns = [
    # Seller URLS (with Catalog)
    url(r'^catalogo/$', group_required('Vendedor')(ProductList.as_view()), name='catalog'),
    url(r'^catalogo/nuevo$', group_required('Vendedor')(ProductCreation.as_view()), name='product_new'),
    url(r'^catalogo/editar/(?P<pk>\d+)$', group_required('Vendedor')(ProductUpdate.as_view()), name='product_edit'),
    url(r'^catalogo/borrar/(?P<pk>\d+)$', group_required('Vendedor')(ProductDelete.as_view()), name='product_delete'),
    url(r'^vendedor/(?P<pk>\d+)$', group_required('Vendedor')(OrderDetail.as_view()), name='detail'),
    url(r'^vendedor/pedidos/$', group_required('Vendedor')(OrderList.as_view()), name='list'),
    url(r'^vendedor/nuevo$', group_required('Vendedor')(OrderCreation.as_view()), name='new'),
    url(r'^vendedor/editar/(?P<pk>\d+)$', group_required('Vendedor')(OrderUpdate.as_view()), name='edit'),
    url(r'^vendedor/borrar/(?P<pk>\d+)$', group_required('Vendedor')(OrderDelete.as_view()), name='delete'),

    # Workshop URLS
    url(r'^tallerista/pedidos/$', group_required('Taller')(WorkShopList.as_view()), name='workshop_list'),
    url(r'^tallerista/(?P<pk>\d+)$', group_required('Taller')(WorkShopDetail.as_view()), name='workshop_detail'),
    url(r'^tallerista/editar/(?P<pk>\d+)$', group_required('Taller')(WorkShopUpdate.as_view()), name='workshop_edit'),

    # Manager URLS
    url(r'^gerente/vista_general/pedidos$', group_required('Gerencia')(OverviewOrderList.as_view()),
        name='orders_overview'),
    url(r'^gerente/vista_general/catalogo$', group_required('Gerencia')(OverviewProductList.as_view()),
        name='products_overview'),
    path('gerente/reportes/pedidos/<int:month>/<int:year>/',
         group_required('Gerencia')(PatientsWithOrdersByMonth.as_view(month_format='%m')),
         name='report_patient_orders_by_month'),
    path('gerente/reportes/pedidos/<int:year>/semana/<int:week>/',
         group_required('Gerencia')(PatientsWithOrdersByWeek.as_view()), name="report_patient_orders_by_week"),
    path('gerente/reportes/catalogo/<int:month>/<int:year>/',
         group_required('Gerencia')(BestSellerByMonth.as_view(month_format='%m')),
         name='report_best_seller_by_month'),
    path('gerente/reportes/catalogo/ventas/<int:month>/<int:year>/',
         group_required('Gerencia')(BestSalesByMonth.as_view(month_format='%m')),
         name='report_best_sales_by_month'),

]
