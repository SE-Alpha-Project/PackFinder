# Generated by Django 4.1.1 on 2022-10-09 04:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "password",
                    models.CharField(max_length=128, verbose_name="password"),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="date joined",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=100)),
                ("bio", models.TextField(blank=True, max_length=500)),
                ("birth_date", models.DateField(blank=True, null=True)),
                (
                    "hometown",
                    models.CharField(blank=True, default="", max_length=100),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Other", "Other"),
                        ],
                        max_length=128,
                    ),
                ),
                (
                    "degree",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Bachelors", "Bachelors Program (BS)"),
                            ("Masters", "Masters Program (MS)"),
                            ("Phd", "Post Docterate (PHD)"),
                        ],
                        max_length=128,
                    ),
                ),
                (
                    "diet",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Vegetarian", "Veg"),
                            ("Non Vegetarian", "Non Veg"),
                        ],
                        max_length=128,
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(
                        blank=True, max_length=2
                    ),
                ),
                (
                    "course",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Computer Science", "Computer Science"),
                            ("Computer Engineering", "Computer Engg."),
                            ("Electrical Engineering", "Electrical Engg."),
                            ("Mechanical Engineering", "Mechanical Engg."),
                        ],
                        max_length=128,
                    ),
                ),
                ("visibility", models.BooleanField(default=True)),
                ("is_profile_complete", models.BooleanField(default=False)),
                (
                    "profile_photo",
                    models.ImageField(
                        default="default.png", upload_to="profile_pics"
                    ),
                ),
                (
                    "preference_gender",
                    models.CharField(
                        choices=[
                            ("No Preference", "No Preference"),
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Other", "Other"),
                        ],
                        default="No Preference",
                        max_length=128,
                    ),
                ),
                (
                    "preference_degree",
                    models.CharField(
                        choices=[
                            ("No Preference", "No Preference"),
                            ("Bachelors", "Bachelors Program (BS)"),
                            ("Masters", "Masters Program (MS)"),
                            ("Phd", "Post Docterate (PHD)"),
                        ],
                        default="No Preference",
                        max_length=128,
                    ),
                ),
                (
                    "preference_diet",
                    models.CharField(
                        choices=[
                            ("No Preference", "No Preference"),
                            ("Vegetarian", "Veg"),
                            ("Non Vegetarian", "Non Veg"),
                        ],
                        default="No Preference",
                        max_length=128,
                    ),
                ),
                (
                    "preference_country",
                    django_countries.fields.CountryField(
                        blank=True, default="No Preference", max_length=2
                    ),
                ),
                (
                    "preference_course",
                    models.CharField(
                        choices=[
                            ("No Preference", "No Preference"),
                            ("Computer Science", "Computer Science"),
                            ("Computer Engineering", "Computer Engg."),
                            ("Electrical Engineering", "Electrical Engg."),
                            ("Mechanical Engineering", "Mechanical Engg."),
                        ],
                        default="No Preference",
                        max_length=128,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
