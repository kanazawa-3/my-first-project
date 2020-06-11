from django import forms
from .models import MyModel


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

#class UploadFileForm(forms.ModelForm):
#        title = forms.CharField(max_length=50)
#        file = forms.FileField()