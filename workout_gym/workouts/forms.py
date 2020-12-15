from .models import Workouts
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class WorkoutsForm(ModelForm):
    class Meta:
        model = Workouts
        fields = ['type_of_training', 'anons', 'full_text', 'date']

        widgets = {
            'type_of_training': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'type of training'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article announcement'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'publication date'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text news'
            }),
        }