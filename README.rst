============
Instructions
============

1. Create a virtual environment for your project and install django
-------------------------------------------------------------------
``$ virtualenv --python=python2.6 --no-site-packages ./django-test``
``$ cd django-test``
``django-test$ ./bin/pip install django``

2. Clone this repository
------------------------
``django-test$ git clone http://cpsaltis@github.com/unweb/simple-archive.git ./simple-archive``

3. Populate the database and run the app
----------------------------------------
``django-test$ cd simple-archive``
``django-test$ ../bin/python manage.py syncdb``
``django-test$ ../bin/python manage.py loaddata fixtures``
``django-test$ ../bin/python manage.py runserver``
