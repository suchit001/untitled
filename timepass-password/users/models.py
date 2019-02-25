from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    name = models.CharField(blank=True, max_length=255)
    M = 'M'
    F = 'F'
    GENDER_CHOICES = (
        (M, 'Male'),
        (F, 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')

    first = "Whats your pet's name"
    SEC_CHOICE =(
        (first, 'Whats your pets name'),
        ("Whats your best friend's name", "Whats your best friend's name"),
        ('What is your postal code','What is your postal code'),
        ('What is your first phone number','What is your first phone number'),
        ('Which is your favorite book','Which is your favorite book'),
    )
    security_question=models.CharField(max_length=200,choices=SEC_CHOICE,default=first)

    birth_date = models.DateField(("Birth Date"), default=date.today)

    answer = models.CharField(max_length=255,help_text="<ul><li>Security Answer are case sensitive</li><li>They can be used to recover your password.</li></ul>")

    resume = models.FileField(blank=True)

    contact_number = models.CharField(max_length=14,blank=True)

    blood_group = models.CharField(max_length=20,blank=True)

    emergency_contact_name = models.CharField(max_length=255,blank=True)

    emergency_contact_number = models.CharField(max_length=14,blank=True)

    address = models.TextField(blank=True)

    def __str__(self):
        return str(self.username)
