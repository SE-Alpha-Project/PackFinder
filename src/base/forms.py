#
# Created on Sun Oct 09 2022
#
# The MIT License (MIT)
# Copyright (c) 2022 Rohit Geddam, Arun Kumar, Teja Varma, Kiron Jayesh, Shandler Mason
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    """Build Sign up Form"""

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    """Build the User Profile Form"""

    # birth_date = forms.DateField(widget=AdminDateWidget)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for bound_field in self:
            if (
                hasattr(bound_field, "field")
                and bound_field.name in self.Meta.required_fields
            ):
                bound_field.field.widget.attrs["required"] = "required"

    class Meta:
        model = Profile
        fields = (
            "name",
            "bio",
            "profile_photo",
            "birth_date",
            "gender",
            "diet",
            "degree",
            "course",
            "hometown",
            "country",
            "visibility",
            "preference_gender",
            "preference_degree",
            "preference_diet",
            "preference_country",
            "preference_course",
        )
        required_fields = [
            "name",
            "bio",
            "birth_date",
            "gender",
            "diet",
            "degree",
            "course",
            "hometown",
            "country",
        ]
        widgets = {
            "birth_date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Select Date",
                    "type": "date",
                },
            )
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_picture', 
            'bio', 
            'major', 
            'year', 
            'interests', 
            'preferred_location',
            'sleep_schedule',
            'sleep_schedule_importance',
            'cleanliness',
            'cleanliness_importance',
            'noise_level',
            'noise_importance',
            'guests_preference',
            'guests_importance'
        ]
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tell us about yourself...'
            }),
            'major': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Computer Science'
            }),
            'year': forms.Select(attrs={
                'class': 'form-control'
            }),
            'interests': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'What are your hobbies and interests?'
            }),
            'preferred_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Wolf Village, College Inn'
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'sleep_schedule': forms.Select(attrs={
                'class': 'form-control'
            }),
            'cleanliness': forms.Select(attrs={
                'class': 'form-control'
            }),
            'noise_level': forms.Select(attrs={
                'class': 'form-control'
            }),
            'guests_preference': forms.Select(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'bio': 'About Me',
            'major': 'Major',
            'year': 'Year',
            'interests': 'Interests & Hobbies',
            'preferred_location': 'Preferred Housing Location',
            'profile_picture': 'Profile Picture'
        }
