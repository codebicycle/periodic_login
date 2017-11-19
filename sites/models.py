from django import forms
from django.db import models
from encrypted_model_fields.fields import EncryptedCharField


class Site(models.Model):
    name = models.CharField(max_length=200)
    login_url = models.URLField()
    username = models.CharField(max_length=200)
    username_label = models.CharField(max_length=200, default='username')
    password = EncryptedCharField(max_length=200)
    password_label = models.CharField(max_length=200, default='password')
    success = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
