# Thunau

## about

A [djangobaseproject](https://github.com/acdh-oeaw/djangobaseproject) based web application to publish (metadata of) resources related to some exavations in Thunau. 

## install

1. Download or Clone this repo
2. Create an virtual environment and run `pip install -r requirements.txt`

### first steps

This projects uses modularized settings (to keep sensitiv information out of version control or being able to use the same code for developement and production). Thefore you'll have to append all `manage.py` commands with a `--settings` parameter pointing to the settings file you'd like to run the code with. For developement just append `--settings=thunau.settings.dev` to the following commands, e.g. `python manage.py makemigrations --settings=thunau.settings.dev`

3. Run `makemigrations`, `migrate`, and `runserver` and check [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Tests

To get needed software you can run

    pip install -r requirements_test.txt

To run the tests execute

    python manage.py test --settings=thunau.settings.test
