from django import forms
from core.models import OBUser


def get_validation_errors(form):
    errors = {}
    for field, error in form.errors.items():
        errors[field] = error
    return errors


class StandardForm(forms.Form):

    def __init__(self, *args, **kwargs):
        try:
            # A request parameter can be passed
            self.request = kwargs.pop('request')
        except:
            self.request = None
        try:
            # A data dictionary parameter can be passed
            self.param_data = kwargs.pop('param_data')
        except:
            self.param_data = {}
        super(StandardForm, self).__init__(*args, **kwargs)


class UserRegisterForm(StandardForm):

    email = forms.EmailField(label='E-mail Address', max_length=200, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    password = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))
    password_conf = forms.CharField(label='Confirm Password', max_length=128, widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        try:
            _ = OBUser.objects.get(email=email)
            raise forms.ValidationError('Email is already in use.')
        except OBUser.DoesNotExist:
            return email

    def clean_password_conf(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password_conf = self.cleaned_data['password_conf']
            if password != password_conf:
                raise forms.ValidationError('Passwords do not match.')
            return password
