from django import forms

class UploadFileForm(forms.Form):
    resume = forms.FileField( widget=forms.ClearableFileInput(attrs={'accept': 'application/pdf'}))