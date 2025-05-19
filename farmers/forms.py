# forms.py
from django import forms
from .models import Symptom
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegistrationForm(forms.ModelForm):
    """
    Form for user registration.

    Allows users to input their phone number and address when registering.

    :param forms.ModelForm: Model form for user registration.
    """

    class Meta:
        model = Profile
        fields = ('farm_name', 'farm_size', 'agriculture_type')
