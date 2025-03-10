from django import forms
from .models import Cars

class CarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(max_length=123)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=12)
    message = forms.CharField(widget=forms.Textarea)

def clean_name(self):
    name = self.cleaned_data['name']
    if len(name) < 3:
        raise forms.ValidationError("Ismingiz xato..!")
    return name



