import re

import requests
from django.core.management.base import BaseCommand

from sites.models import Site


class Command(BaseCommand):
    help = 'Login to sites'

    def handle(self, *args, **kwargs):
        for site in Site.objects.all():
            self._check_site(site)

    def _check_site(self, site):
        params = {
            site.username_label: site.username,
            site.password_label: site.password,
        }

        r = requests.post(site.login_url, params=params)
        if r.status_code != requests.codes.ok:
            raise CommandError(r.status_code)

        match = re.search(site.success, r.text)
        if match:
            print(f'{site.name} OK')
        else:
            print(f'{site.name} ERROR Success string not found')
