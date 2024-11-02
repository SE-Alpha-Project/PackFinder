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

from email.policy import default
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from django_countries.fields import CountryField


from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager
from .utils import check_ncsu_email


class CustomUser(AbstractUser):
    """Custom User Model"""

    username = None
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        email = self.email

        if not check_ncsu_email(email):
            raise ValueError("Please use NCSU Email Id!")
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.email


class Profile(models.Model):
    """Model for User Profile"""

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"

    DEGREE_BS = "Bachelors"
    DEGREE_MS = "Masters"
    DEGREE_PHD = "Phd"

    DIET_VEG = "Vegetarian"
    DIET_NON_VEG = "Non Vegetarian"

    COURSE_CS = "Computer Science"
    COURSE_CE = "Computer Engineering"
    COURSE_EE = "Electrical Engineering"
    COURSE_MEC = "Mechanical Engineering"

    BLANK = "--"
    NO_PREF = "No Preference"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    DEGREE_CHOICES = (
        (DEGREE_BS, "Bachelors Program (BS)"),
        (DEGREE_MS, "Masters Program (MS)"),
        (DEGREE_PHD, "Post Docterate (PHD)"),
    )

    COURSE_CHOICES = (
        (COURSE_CS, "Computer Science"),
        (COURSE_CE, "Computer Engg."),
        (COURSE_EE, "Electrical Engg."),
        (COURSE_MEC, "Mechanical Engg."),
    )

    DIET_CHOICES = ((DIET_VEG, "Veg"), (DIET_NON_VEG, "Non Veg"))

    PREF_GENDER_CHOICES = (
        (NO_PREF, "No Preference"),
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    PREF_DEGREE_CHOICES = (
        (NO_PREF, "No Preference"),
        (DEGREE_BS, "Bachelors Program (BS)"),
        (DEGREE_MS, "Masters Program (MS)"),
        (DEGREE_PHD, "Post Docterate (PHD)"),
    )

    PREF_DIET_CHOICES = (
        (NO_PREF, "No Preference"),
        (DIET_VEG, "Veg"),
        (DIET_NON_VEG, "Non Veg"),
    )

    PREF_COURSE_CHOICES = (
        (NO_PREF, "No Preference"),
        (COURSE_CS, "Computer Science"),
        (COURSE_CE, "Computer Engg."),
        (COURSE_EE, "Electrical Engg."),
        (COURSE_MEC, "Mechanical Engg."),
    )

    """User Profile Model"""
    name = models.CharField(max_length=100, default="")
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    hometown = models.CharField(max_length=100, default="", blank=True)

    gender = models.CharField(
        max_length=128, choices=GENDER_CHOICES, blank=True
    )
    degree = models.CharField(
        max_length=128, choices=DEGREE_CHOICES, blank=True
    )
    diet = models.CharField(max_length=128, choices=DIET_CHOICES, blank=True)
    country = CountryField(blank_label="Select Country", blank=True)
    course = models.CharField(
        max_length=128, choices=COURSE_CHOICES, blank=True
    )

    visibility = models.BooleanField(default=True)
    is_profile_complete = models.BooleanField(default=False)
    profile_photo = models.ImageField(
        default="default.png", upload_to="profile_pics"
    )

    # preferences

    preference_gender = models.CharField(
        max_length=128, choices=PREF_GENDER_CHOICES, default=NO_PREF
    )
    preference_degree = models.CharField(
        max_length=128, choices=PREF_DEGREE_CHOICES, default=NO_PREF
    )
    preference_diet = models.CharField(
        max_length=128, choices=PREF_DIET_CHOICES, default=NO_PREF
    )
    preference_country = CountryField(
        blank_label="No Preference", blank=True, default="No Preference"
    )
    preference_course = models.CharField(
        max_length=128, choices=PREF_COURSE_CHOICES, default=NO_PREF
    )

    email_confirmed = models.BooleanField(default=False)

    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    major = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=20, choices=[
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Graduate', 'Graduate')
    ], blank=True)
    interests = models.TextField(max_length=300, blank=True)
    preferred_location = models.CharField(max_length=100, blank=True)

    sleep_schedule = models.CharField(max_length=20, choices=[
        ('Early_Bird', 'Early Bird (Before 10 PM)'),
        ('Night_Owl', 'Night Owl (After 10 PM)'),
        ('Flexible', 'Flexible'),
    ], default='Flexible')
    sleep_schedule_importance = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="How important is sleep schedule matching? (1-10)"
    )

    cleanliness = models.IntegerField(
        choices=[(i, i) for i in range(1, 11)],
        default=5,
        help_text="How clean do you keep your space? (1-10)"
    )
    cleanliness_importance = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="How important is cleanliness matching? (1-10)"
    )

    noise_level = models.CharField(max_length=20, choices=[
        ('Quiet', 'Prefer Quiet'),
        ('Moderate', 'Moderate Noise OK'),
        ('Active', 'Active/Social Environment'),
    ], default='Moderate')
    noise_importance = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="How important is noise level matching? (1-10)"
    )

    guests_preference = models.CharField(max_length=20, choices=[
        ('Rarely', 'Rarely/Never'),
        ('Sometimes', 'Sometimes'),
        ('Often', 'Often'),
    ], default='Sometimes')
    guests_importance = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="How important is guest preference matching? (1-10)"
    )

    def __str__(self):
        return f"{self.user.email}-profile"


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    """Create User Profile"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=get_user_model())
def save_user_profile(sender, instance, **kwargs):
    """Save User Profile"""
    instance.profile.save()
