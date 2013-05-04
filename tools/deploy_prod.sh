#!/bin/bash

git push git@heroku.com:birthdaystarter.git
heroku run python manage.py migrate --app birthdaystarter
heroku run python manage.py collectstatic --noinput --app birthdaystarter
