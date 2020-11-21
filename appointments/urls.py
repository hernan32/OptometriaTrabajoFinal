from django.conf.urls import url
from django.urls import path

from patient.views import PatientUpdate
from .decorators import group_required
from .views import *

urlpatterns = [
    # Medic URLS
    path('medico/mis_pacientes/<int:day>/<int:month>/<int:year>/', group_required('Medico')(MyPatientListByDay.as_view(month_format='%m')), name="by_day"),
    path('medico/mis_pacientes/<int:month>/<int:year>/', group_required('Medico')(MyPatientListByMonth.as_view(month_format='%m')), name="by_month"),
    path('medico/mis_pacientes/<int:year>/', group_required('Medico')(MyPatientListByYear.as_view()), name="by_year"),
    url(r'^medico/mis_pacientes/$', group_required('Medico')(MyPatientsList.as_view()), name='patients_list'),
    url(r'^medico/mis_pacientes/editar/(?P<pk>\d+)$', group_required('Medico')(PatientUpdate.as_view()), name='patient_edit'),

    # Secretary URLS
    url(r'^secretaria/turnos/$', group_required('Secretaria')(AppointmentList.as_view()), name='list'),
    url(r'^secretaria/(?P<pk>\d+)$', group_required('Secretaria')(AppointmentDetail.as_view()), name='detail'),
    url(r'^secretaria/nuevo$', group_required('Secretaria')(AppointmentCreation.as_view()), name='new'),
    url(r'^secretaria/editar/(?P<pk>\d+)$', group_required('Secretaria')(AppointmentUpdate.as_view()), name='edit'),
    url(r'^secretaria/borrar/(?P<pk>\d+)$', group_required('Secretaria')(AppointmentDelete.as_view()), name='delete'),
]
