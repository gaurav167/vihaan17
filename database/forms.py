from django import forms

class ImageUploadForm(forms.Form):
    """Image upload form."""
    u_id = forms.CharField(label='user_id', max_length=30)
    image = forms.ImageField()