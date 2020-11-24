from django.forms import DateInput
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, DayArchiveView, \
    MonthArchiveView, YearArchiveView, WeekArchiveView

from appointments.models import Appointment


class AppointmentList(ListView):
    model = Appointment


class MyPatientsList(ListView):
    model = Appointment
    template_name_suffix = '_my_patients_list'

    def get_queryset(self):
        return Appointment.objects.filter(medic=self.request.user)


class MyPatientListByDay(DayArchiveView):
    model = Appointment
    template_name_suffix = '_by_day'
    queryset = Appointment.objects.all()
    date_field = "date"
    allow_empty = True
    allow_future = True

    def get_queryset(self):
        return Appointment.objects.filter(medic=self.request.user)


class MyPatientListByMonth(MonthArchiveView):
    model = Appointment
    template_name_suffix = '_by_month'
    queryset = Appointment.objects.all()
    date_field = 'date'
    allow_empty = True
    allow_future = True

    def get_queryset(self):
        return Appointment.objects.filter(medic=self.request.user)


class MyPatientListByYear(YearArchiveView):
    model = Appointment
    template_name_suffix = '_by_year'
    queryset = Appointment.objects.all()
    date_field = 'date'
    make_object_list = True
    allow_empty = True
    allow_future = True

    def get_queryset(self):
        return Appointment.objects.filter(medic=self.request.user)


class AppointmentDetail(DetailView):
    model = Appointment


class AppointmentCreation(CreateView):
    model = Appointment
    success_url = reverse_lazy('appointments:list')
    fields = ['patient', 'date', 'medic']

    def get_form(self, form_class=None):
        """add date picker in forms"""
        form = super(AppointmentCreation, self).get_form()
        form.fields['date'].widget = DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        return form


class AppointmentUpdate(UpdateView):
    model = Appointment
    success_url = reverse_lazy('appointments:list')
    fields = ['patient', 'date', 'medic', 'was_present']

    def get_form(self, form_class=None):
        """add date picker in forms"""
        form = super(AppointmentUpdate, self).get_form()
        form.fields['date'].widget = DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        return form


class AppointmentDelete(DeleteView):
    model = Appointment
    success_url = reverse_lazy('appointments:list')


class OverviewAppointmentList(ListView):
    model = Appointment
    template_name_suffix = "_overview"


class ReportAssistanceByWeek(WeekArchiveView):
    queryset = Appointment.objects.filter(was_present=True)
    date_field = "date"
    week_format = "%W"
    allow_future = True
    allow_empty = True
    template_name_suffix = '_report_by_week'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ReportAssistanceByWeek, self).get_context_data(**kwargs)
        # Add in the publisher
        context['assistance'] = "Asistencia"
        return context


class ReportNoAssistanceByWeek(WeekArchiveView):
    queryset = Appointment.objects.filter(was_present=False)
    date_field = "date"
    week_format = "%W"
    allow_future = True
    allow_empty = True
    template_name_suffix = '_report_by_week'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ReportNoAssistanceByWeek, self).get_context_data(**kwargs)
        # Add in the publisher
        context['assistance'] = "Inasistencia"
        return context


class ReportAssistanceByMonth(MonthArchiveView):
    queryset = Appointment.objects.filter(was_present=True)
    date_field = "date"
    allow_future = True
    allow_empty = True
    template_name_suffix = '_report_by_month'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ReportAssistanceByMonth, self).get_context_data(**kwargs)
        # Add in the publisher
        context['assistance'] = "Asistencia"
        return context


class ReportNoAssistanceByMonth(MonthArchiveView):
    queryset = Appointment.objects.filter(was_present=False)
    date_field = "date"
    allow_future = True
    allow_empty = True
    template_name_suffix = '_report_by_month'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ReportNoAssistanceByMonth, self).get_context_data(**kwargs)
        # Add in the publisher
        context['assistance'] = "Inasistencia"
        return context
