# Django Photo Gallery with Bootstrap Carousel

[![Build Status](https://travis-ci.org/dubirajara/django_carousel_photos.svg?branch=master)](https://travis-ci.org/dubirajara/django_carousel_photos)
[![Updates](https://pyup.io/repos/github/dubirajara/django_carousel_photos/shield.svg)](https://pyup.io/repos/github/dubirajara/django_carousel_photos/)
[![Coverage Status](https://coveralls.io/repos/github/dubirajara/django_carousel_photos/badge.svg?branch=master)](https://coveralls.io/github/dubirajara/django_carousel_photos?branch=master)
[![Python 3](https://pyup.io/repos/github/dubirajara/django_carousel_photos/python-3-shield.svg)](https://pyup.io/repos/github/dubirajara/django_carousel_photos/)



- Clone the repository:

```sh
git clone https://github.com/dubirajara/django_carousel_photos.git && cd django_carousel_photos
```
- Install the dependencies with pipenv:

```sh
pipenv install --dev
pipenv shell
```
- Run the migrations:

```sh
python manage.py migrate
```
- Create a django admin user:

```sh
python manage.py createsuperuser
```
- Run tests and run server:
```sh
python manage.py test 
python manage.py runserver
```
- And so, open django admin and add your photos in the carousel.
