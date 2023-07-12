from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(label="", max_length="30",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}))
    last_name = forms.CharField(label="", max_length="30",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password1')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted">Required. 150</span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li> pass cant be similar to infos ' \
                                     '</li><li> at least 8 chars </li><li> cant be all numeric </li> </ul> '

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted">Enter password as before, ' \
                                     'as verification</span> '


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': "First name", 'class': 'form-control'}), label='')
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': "Last name", 'class': 'form-control'}), label='')
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': "Email", 'class': 'form-control'}), label='')
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': "Address", 'class': 'form-control'}), label='')
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': "City", 'class': 'form-control'}), label='')
    state = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': "State", 'class': 'form-control'}), label='')
    zipcode = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': "Zipcode", 'class': 'form-control'}), label='')
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': "Phone", 'class': 'form-control'}), label='')

    class Meta:
        model = Record
        exclude = ("user",)
