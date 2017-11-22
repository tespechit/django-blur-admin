## It's not finished

# BlurAdmin AngularJS admin panel front-end framework and back-end based on Django Python

Basic REST API based on Django Python

Customizable admin panel framework made by [Akveo team](http://akveo.com/).

## Back-end dependencies (Linux)
- Python 2.7
- PIP
- Django 1.11
- virtualenv
- virtualenvwrapper

## Front-end dependencies
- NodeJS
- NPM
- Bower
- Gulp

## First steps back-end (Linux)
1. Go to your favorite folder `cd ~/my_projects/`
2. Clone this repo `git clone https://github.com/cmchecha/django-blur-admin.git`
3. If you don't have a virtualenv created: `mkvirtualenv my_venv`
4. Activate your virtualenv with virtualenvwrapper `workon my_venv`
5. Install back-end dependencies `pip install -r requirements.txt`
6. Run django development server `python manage.py runserver 0.0.0.0:8000`
7. Your REST API is running in `localhost:8000`

## For your AngularJS front-end
1. Go to the frontend folder `cd frontend/`
2. Install front-end dependencies `npm install`
3. Install bower dependencies `bower install`
4. Run this command `gulp serve`
5. Your frontend is running in `localhost:3000`

## Front-end documentation
Installation, customization and other useful articles: https://akveo.github.io/blur-admin/

## How can I support developers?
- Star our GitHub repo
- Create pull requests, submit bugs, suggest new features or documentation updates

License
-------------
<a href=/LICENSE.txt target="_blank">MIT</a> license.

### From akveo and cmchecha
