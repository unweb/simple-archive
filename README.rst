Instructions
============

First, create a virtual environment and install django::

    $ virtualenv --python=python2.6 --no-site-packages ./django-test
    $ cd django-test
    $ ./bin/pip install django

Then get the code::

    $ git clone http://cpsaltis@github.com/unweb/simple-archive.git simple-archive/

Finally, populate the database and run the app::

    $ ./bin/python simple-archive/manage.py syncdb
    $ ./bin/python simple-archive/manage.py loaddata fixtures
    $ ./bin/python simple-archive/manage.py runserver
