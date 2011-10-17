Instructions
============

First, create a virtual environment and install django::

    $ virtualenv --python=python2.6 --no-site-packages ./django-test
    $ cd django-test
    django-test$ ./bin/pip install django

Then get the code::

    django-test$ git clone http://cpsaltis@github.com/unweb/simple-archive.git ./simple-archive

Finally, populate the database and run the app::

    django-test$ cd simple-archive
    django-test$ ../bin/python manage.py syncdb
    django-test$ ../bin/python manage.py loaddata fixtures
    django-test$ ../bin/python manage.py runserver
