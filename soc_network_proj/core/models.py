from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    HUNTER_NOT_VERIFIED = 'NF'
    HUNTER_VALID = 'VL'
    HUNTER_NOT_VALID = 'NV'

    HUNTER_VERIFY_CHOICES = [
        (HUNTER_NOT_VERIFIED, 'Not Verified'),
        (HUNTER_VALID, 'Valid'),
        (HUNTER_NOT_VALID, 'Not Valid')
    ]

    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    hunter_verified = models.CharField(max_length=2, choices=HUNTER_VERIFY_CHOICES, default=HUNTER_NOT_VERIFIED)
    clearbit_enriched = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class ClearBitProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clearbit')
    clearbit_id = models.PositiveBigIntegerField(blank=True, null=True)
    clearbit_full_name = models.CharField(max_length=300, blank=True)
    clearbit_given_name = models.CharField(max_length=100, blank=True)
    clearbit_family_name = models.CharField(max_length=200, blank=True)
    clearbit_comp_id = models.PositiveIntegerField(blank=True, null=True)
    clearbit_comp_name = models.CharField(max_length=100, blank=True)
    clearbit_comp_legal_name = models.CharField(max_length=200, blank=True)
    clearbit_comp_domain = models.URLField(blank=True)