Hello!
My project can:

-Authenticate

-Registration

-Search

-Db(Postgresql)

-Frontend(css, html)


1. Clone repository

`https://github.com/ShadowDubina/Django-full-stack-app.git`

2. Go to the direcroty

`cd work_board`

`cd table`

3. Create vertual venv

`python -m venv env`

4. Go to the env

`env/Scripts/activate`

5. install requirements

`pip install -r requirements.txt`

6. Install Postgresql
When you will be create database from postgresql, see you should check settings.py specifically 'DATABASE' data or create and replace exiting data

7.Create first migrations:

`python manage.py makemigrations`

apply migrations:

`python manage.py migrate`

8. start website(if install Postgresql)

`python manage.py runserver`
