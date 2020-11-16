from django.conf.urls import url

from .decorators import group_required
from .views import AppointmentList, AppointmentDetail, AppointmentCreation, AppointmentDelete, AppointmentUpdate

urlpatterns = [
    url(r'^$', group_required('Secretaria')(AppointmentList.as_view()), name='list'),
    url(r'^(?P<pk>\d+)$', group_required('Secretaria')(AppointmentDetail.as_view()), name='detail'),
    url(r'^nuevo$', group_required('Secretaria')(AppointmentCreation.as_view()), name='new'),
    url(r'^editar/(?P<pk>\d+)$', group_required('Secretaria')(AppointmentUpdate.as_view()), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', group_required('Secretaria')(AppointmentDelete.as_view()), name='delete'),
]
