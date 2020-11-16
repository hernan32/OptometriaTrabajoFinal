from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q

from patient.models import Patient


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                                verbose_name="Paciente",
                                related_name="Paciente")
    date = models.DateTimeField(unique=True,
                                verbose_name="Fecha")
    medic = models.ForeignKey(settings.AUTH_USER_MODEL,
                              limit_choices_to=Q(groups__name='Medico'),
                              on_delete=models.CASCADE)
    was_present = models.BooleanField(default=False,
                                      verbose_name="¿Atendido?")

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

    def __str__(self):
        return f"{self.patient} {self.date} {self.was_present}"


def get_name(self):
    return f"{self.first_name}, {self.last_name}"


User.add_to_class("__str__", get_name)
