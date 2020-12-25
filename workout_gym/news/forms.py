from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text', 'pub_date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'News article title'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article announcement'
            }),
            'pub_date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'publication date'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text news'
            }),
        }