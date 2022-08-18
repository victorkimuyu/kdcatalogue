from django import forms
from .models import Kayak

fields = [
    'brand', 'model_name', 'material', 'description', 'key_features', 'model_code',
    'steering', 'paddling', 'length', 'width', 'height', 'weight', 'load_capacity', 'outer_cockpit_dimensions',
    'ideal_paddler_size', 'beluga_skirt_size', 'impulse_drive', 'is_new', 'in_stock', 'photo', 'side_view',
    'angle_view', 'action_shot'
]

url_fields = [
    'web_page', 'youtube',
]

select_fields = ['material', 'steering', 'paddling', 'in_stock', 'is_new']


class KayakForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Kayak
        exclude = ['slug', 'id']

        widgets = {
            'brand': forms.Select(attrs={'class': 'form-select'}),
            'model_name': forms.TextInput(attrs={'class': 'form-input'}),
            'material': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea'}),
            'key_features': forms.Textarea(attrs={'class': 'form-textarea'}),
            'model_code': forms.TextInput(attrs={'class': 'form-input'}),
            'web_page': forms.URLInput(attrs={'class': 'form-input'}),
            'youtube': forms.URLInput(attrs={'class': 'form-input'}),
            'steering': forms.Select(attrs={'class': 'form-input'}),
            'paddling': forms.Select(attrs={'class': 'form-input'}),
            'length': forms.TextInput(attrs={'class': 'form-input'}),
            'width': forms.TextInput(attrs={'class': 'form-input'}),
            'height': forms.TextInput(attrs={'class': 'form-input'}),
            'weight': forms.TextInput(attrs={'class': 'form-input'}),
            'load_capacity': forms.TextInput(attrs={'class': 'form-input'}),
            'outer_cockpit_dimensions': forms.TextInput(attrs={'class': 'form-input'}),
            'ideal_paddler_size': forms.TextInput(attrs={'class': 'form-input'}),
            'beluga_skirt_size': forms.TextInput(attrs={'class': 'form-input'}),
            'impulse_drive': forms.TextInput(attrs={'class': 'form-input'}),
            'is_new': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'in_stock': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
