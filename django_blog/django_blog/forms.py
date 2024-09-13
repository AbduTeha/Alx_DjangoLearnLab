from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagWidget
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    tags = forms.CharField(widget=TagWidget)