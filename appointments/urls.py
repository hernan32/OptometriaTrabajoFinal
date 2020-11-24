from django.conf.urls import url
from django.urls import path

from patient.views import PatientUpdate
from .decorators import group_required
from .views import *

urlpatterns = [
    # Medic URLS
    path('medico/mis_pacientes/<int:day>/<int:month>/<int:year>/',
         group_required('Medico')(MyPatientListByDay.as_view(month_format='%m')), name="by_day"),
    path('medico/mis_pacientes/<int:month>/<int:year>/',
         group_required('Medico')(MyPatientListByMonth.as_view(month_format='%m')), name="by_month"),
    path('medico/mis_pacientes/<int:year>/', group_required('Medico')(MyPatientListByYear.as_view()), name="by_year"),
    url(r'^medico/mis_pacientes/$', group_required('Medico')(MyPatientsList.as_view()), name='patients_list'),
    url(r'^medico/mis_pacientes/editar/(?P<pk>\d+)$', group_required('Medico')(PatientUpdate.as_view()),
        name='patient_edit'),

    # Secretary URLS
    url(r'^secretaria/turnos/$', group_required('Secretaria')(AppointmentList.as_view()), name='list'),
    url(r'^secretaria/(?P<pk>\d+)$', group_required('Secretaria')(AppointmentDetail.as_view()), name='detail'),
    url(r'^secretaria/nuevo$', group_required('Secretaria')(AppointmentCreation.as_view()), name='new'),
    url(r'^secretaria/editar/(?P<pk>\d+)$', group_required('Secretaria')(AppointmentUpdate.as_view()), name='edit'),
    url(r'^secretaria/borrar/(?P<pk>\d+)$', group_required('Secretaria')(AppointmentDelete.as_view()), name='delete'),

    # Manager URLS
    path('gerente/reportes/turnos/asistencia/<int:year>/semana/<int:week>/',
         group_required('Gerencia')(ReportAssistanceByWeek.as_view()), name="report_assistance_by_week"),
    path('gerente/reportes/turnos/inasistencia/<int:year>/semana/<int:week>/',
         group_required('Gerencia')(ReportNoAssistanceByWeek.as_view()), name="report_no_assistance_by_week"),
    path('gerente/reportes/turnos/asistencia/<int:month>/<int:year>/',
         group_required('Gerencia')(ReportAssistanceByMonth.as_view(month_format='%m')),
         name="report_assistance_by_month"),
    path('gerente/reportes/turnos/inasistencia/<int:month>/<int:year>/',
         group_required('Gerencia')(ReportNoAssistanceByMonth.as_view(month_format='%m')),
         name="report_no_assistance_by_month"),
    path('gerente/vista_general/turnos/',
         group_required('Gerencia')(OverviewAppointmentList.as_view()), name="appointments_overview"),
]
