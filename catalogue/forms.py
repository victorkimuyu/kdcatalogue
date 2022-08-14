from django.forms import ModelForm
from .models import Kayak


class KayakForm(ModelForm):
    class Meta:
        model = Kayak
        exclude = ['slug', 'id']