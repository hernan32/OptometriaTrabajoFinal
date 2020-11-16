from django.db import models


class Patient(models.Model):
    document_id = models.IntegerField(primary_key=True,
                                      unique=True,
                                      verbose_name="DNI")
    first_name = models.CharField(max_length=64,
                                  verbose_name="Nombre")
    last_name = models.CharField(max_length=64,
                                 verbose_name="Apellido")
    medical_history = models.TextField(max_length=256,
                                       verbose_name="Historia Medica")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return f"{self.first_name}, {self.last_name} (DNI: {self.document_id})"
