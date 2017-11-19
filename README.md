# Periodic Login

Check-in to sites requiring periodic logins.

Uses Django admin for CRUD and a management command to visit sites.

## Install

1. Use pipenv to install dependencies and manage the virtual environment

        pipenv install
        pipenv shell

2. Create `secrets.py` in the same directory with `settings.py` and populate the constants `SECRET_KEY` and `FIELD_ENCRYPTION_KEY`.

    `FIELD_ENCRYPTION_KEY` should be a 32-bit url-safe base64-encoded bytestrings.
    Here's how to generate it:

        import base64
        import os

        base64.urlsafe_b64encode(os.urandom(32))

3. Create superuser

        ./manage.py createsuperuser


## Run

- Populate sites
    1. Run django server

            ./manage.py runserver

    2. Add sites credentials with django admin

- Run command to visit sites

        ./manage.py checksites


## Security

Password fields are stored encrypted in the database, but they are not encrypted in memory. Whoever has access to the Django shell can view the stored passwords.
