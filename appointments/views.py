from django.forms import DateInput
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from appointments.models import Appointment


class AppointmentList(ListView):
    model = Appointment


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
