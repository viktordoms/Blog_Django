from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'text', 'photo', 'is_published', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input-url'}),
            'text': forms.Textarea(attrs={'class': 'form-input-text'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категорія не вибрана"

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('Довжина перевищує 100 символів')
        return title
