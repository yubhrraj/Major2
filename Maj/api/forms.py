from django import forms

from .models import Kid

class PostForm(forms.ModelForm):

    class Meta:
        model = Kid
        fields = '__all__'