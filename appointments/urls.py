from django.conf.urls import url
from django.urls import path

from patient.views import PatientUpdate
from .decorators import group_required
from .views import *

urlpatterns = [
    url(r'^turnos/$', group_required('Secretaria')(AppointmentList.as_view()), name='list'),
    path('mis_pacientes/<int:day>/<int:month>/<int:year>/', MyPatientListByDay.as_view(month_format='%m'), name="by_day"),
    path('mis_pacientes/<int:month>/<int:year>/', MyPatientListByMonth.as_view(month_format='%m'), name="by_month"),
    path('mis_pacientes/<int:year>/', MyPatientListByYear.as_view(), name="by_year"),
    url(r'^mis_pacientes/$', group_required('Medico')(MyPatientsList.as_view()), name='patients_list'),
    url(r'^(?P<pk>\d+)$', group_required('Secretaria')(AppointmentDetail.as_view()), name='detail'),
    url(r'^nuevo$', group_required('Secretaria')(AppointmentCreation.as_view()), name='new'),
    url(r'^editar/(?P<pk>\d+)$', group_required('Secretaria')(AppointmentUpdate.as_view()), name='edit'),
    url(r'^mis_pacientes/editar/(?P<pk>\d+)$', group_required('Medico')(PatientUpdate.as_view()), name='patient_edit'),
    url(r'^borrar/(?P<pk>\d+)$', group_required('Secretaria')(AppointmentDelete.as_view()), name='delete'),
]
