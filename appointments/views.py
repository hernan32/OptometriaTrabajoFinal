from django.forms import DateInput
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, DayArchiveView, \
    MonthArchiveView, YearArchiveView

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

    def get_form(self):
        """add date picker in forms"""
        form = super(AppointmentCreation, self).get_form()
        form.fields['date'].widget = DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        return form


class AppointmentUpdate(UpdateView):
    model = Appointment
    success_url = reverse_lazy('appointments:list')
    fields = ['patient', 'date', 'medic', 'was_present']

    def get_form(self):
        """add date picker in forms"""
        form = super(AppointmentUpdate, self).get_form()
        form.fields['date'].widget = DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        return form


class AppointmentDelete(DeleteView):
    model = Appointment
    success_url = reverse_lazy('appointments:list')
