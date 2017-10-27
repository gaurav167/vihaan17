from django import forms

from . import models

class DataSaveForm(forms.ModelForm):
    class Meta:
        model = models.Hash
        fields = ['data']
