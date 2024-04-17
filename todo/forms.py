from .models import Todo
from django.forms import ModelForm
from django import forms

class TodoForm(ModelForm):
    field_order = ['title', 'description', 'isDone']

    class Meta:
        model = Todo
        fields = {'title', 'description', 'isDone'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'labels': ''}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description', 'labels': ''}),
        }