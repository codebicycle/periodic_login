from django.contrib import admin
from django import forms

from .models import Site


class SiteAdminForm(forms.ModelForm):
    class Meta:
        model = Site
        widgets = {
            'password': forms.PasswordInput(render_value = True)
        }
        fields = '__all__'


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    form = SiteAdminForm
    fields = (
        'name',
        'login_url',
        ('username', 'username_label'),
        ('password', 'password_label'),
        'success',
    )
