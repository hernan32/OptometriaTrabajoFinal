from django.core.exceptions import ValidationError
from django.forms import ModelForm

from orders.models import Product


class ProductCreationForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'is_glass', 'position', 'type', 'frame']

    def clean(self):
        cleaned_data = super(ProductCreationForm, self).clean()

        is_glass = cleaned_data.get('is_glass')
        position = cleaned_data.get('position')
        type_field = cleaned_data.get('type')
        frame = cleaned_data.get('frame')

        if is_glass:
            msg = 'Seleccione una Opción.'
            if position is None:
                self.add_error('position', ValidationError(msg, code='position_field_error'))
            if type_field is None:
                self.add_error('type', ValidationError(msg, code='type_field_error'))
            if frame is None:
                self.add_error('frame', ValidationError(msg, code='frame_field_error'))

        return cleaned_data
