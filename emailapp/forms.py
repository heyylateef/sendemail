from django import forms
from django.forms import ModelForm


class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Your email address", required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    message = forms.CharField(label="Type your message...", required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'5'}))
