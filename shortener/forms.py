from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class UserUpdateForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=('email','first_name','last_name')

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. A valid email address.')
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

class URLForm(forms.Form):
    url=forms.URLField(
        label="URL",
        max_length=2048,
        widget=forms.URLInput(attrs={
            'class':'form-control form-control-lg',
            'placeholder': 'https://your-long-url.com/goes/here'
        })
    )