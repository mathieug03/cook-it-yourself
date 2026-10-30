# CookItYourself

**Find something to cook with the ingredients already in your kitchen.**

A five-person **engineering-school hackathon-style class project**, built during CentraleSupelec's one-week Coding Weeks in November 2023.

## What we built

A Django recipe-sharing application with user registration/login, recipe creation, photos, ingredient-based matching, and recipe browsing/search. The central interaction is simple: select ingredients you have, then see recipes whose required ingredients are all available.

## Run locally

This is a historical Django 4.2 application. Use a virtual environment and keep it local.

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

Open `http://127.0.0.1:8000`. The optional fixture contains fictional recipes and a non-login demo author. Create your own account through the app; no shared password is distributed. The app retains its original French interface.

## Scope and archive notes

The source comes from the final `ciy` project, including its November 24 “site fini” work and later documentation. Earlier storefront exercises and sandbox copies are excluded.

This is a class prototype, not a production service. Password policy and upload handling are basic; ratings, comments, carbon and nutrition fields are not presented as complete product flows. The original database, uploaded recipe photos, and embedded Django secret are excluded. Public-copy changes add setup instructions, a fictional fixture, a missing search import, an empty-photo fallback using a bundled template image, and environment-based local configuration; they do not turn the application into a new product.

## Team and credits

Amandine Rondot, Olga Lopez-Bodoque, Elie Juvenspan, Daouda Keita, and Mathieu Gautier. This repository presents the team's class work, not sole authorship.

The original French project description is in [the archive notes](docs/ORIGINAL_README.fr.md). The interface incorporates the Feane / HTML Design template and a Colorlib login template, plus Bootstrap, jQuery, and Font Awesome. Existing notices and footer credits are retained; bundled materials retain their original rights. No new blanket license is asserted over team or third-party work.
