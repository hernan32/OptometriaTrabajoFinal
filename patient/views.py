# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from patient.models import Patient


class PatientUpdate(UpdateView):
    model = Patient
    success_url = reverse_lazy('appointments:patients_list')
    fields = ['document_id', 'first_name', 'last_name', 'medical_history']

    def get_form(self, form_class=None):
        form = super(PatientUpdate, self).get_form()
        form.fields['document_id'].disabled = True
        form.fields['first_name'].disabled = True
        form.fields['last_name'].disabled = True
        return form
