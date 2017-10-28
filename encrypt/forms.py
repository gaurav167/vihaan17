from django import forms

class DataSaveForm(forms.Form):
    u_id = forms.CharField(label='user_id', max_length=30)
    data = forms.CharField(label="data", widget=forms.Textarea)