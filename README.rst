hatherleigh.net
***************

Development
===========

Install
-------

Virtual Environment
-------------------

Note: replace ``patrick`` with your name (checking in the ``settings`` folder
to make sure a file has been created for you)::

  mkvirtualenv p_hatherleigh_net
  pip install -r requirements/local.txt

  echo "export DJANGO_SETTINGS_MODULE=settings.dev_patrick" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate
  echo "export SECRET_KEY=\"the_secret_key\"" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset SECRET_KEY" >> $VIRTUAL_ENV/bin/postdeactivate

  add2virtualenv .
  deactivate

Testing
-------

We use ``pytest-django``::

  workon p_hatherleigh_net
  find . -name '*.pyc' -delete
  py.test

To stop on first failure::

  py.test -x

Usage
-----

::

  workon p_hatherleigh_net

  py.test -x && \
      touch temp.db && rm temp.db && \
      django-admin.py syncdb --noinput && \
      django-admin.py migrate --all --noinput && \
      django-admin.py demo_data_login && \
      django-admin.py demo_data_pump && \
      django-admin.py runserver

Release and Deploy
==================

https://github.com/pkimber/cloud_docs
