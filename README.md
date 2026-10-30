# CookItYourself

**Find something to cook with the ingredients already in your kitchen.**

A five-person **engineering-school hackathon-style class project**, built in one week in November 2023.

## What we built

A Django recipe-sharing application with user registration/login, recipe creation, photos, ingredient-based matching, and recipe browsing/search. The central interaction is simple: select ingredients you have, then see recipes whose required ingredients are all available.

## Run locally

This project uses Django 4.2 and is intended for local demonstration.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export DJANGO_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
export DJANGO_DEBUG=true
python manage.py migrate
python manage.py loaddata demo
python manage.py runserver 127.0.0.1:8000
```

Open `http://127.0.0.1:8000`. The demo fixture contains sample recipes; create an account through the app to add your own. The interface is in French.

## Status

The application supports recipe sharing and ingredient-based search. Ratings, comments, carbon estimates, and nutritional analysis remain outside the completed workflow.

Account and upload handling are basic; use the application locally.

## Team

Amandine Rondot, Olga Lopez-Bodoque, Elie Juvenspan, Daouda Keita, and Mathieu Gautier.
