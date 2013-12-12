hatherleigh.net
***************

Development
===========

Install
-------

Virtual Environment
-------------------

Note: replace ``patrick`` with your name (checking in the ``settings`` folder
to make sure a file has been created for you).

::

  mkvirtualenv p_hatherleigh_net
  pip install -r requirements/local.txt

  echo "export DJANGO_SETTINGS_MODULE=settings.dev_patrick" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate
  echo "export SECRET_KEY=\"the_secret_key\"" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset SECRET_KEY" >> $VIRTUAL_ENV/bin/postdeactivate

  add2virtualenv ../../app/base
  add2virtualenv ../../app/story
  add2virtualenv ../../app/login
  add2virtualenv .
  deactivate

To check the order of the imports::

  workon p_hatherleigh_net
  cdsitepackages
  cat _virtualenv_path_extensions.pth

Check the imports are in the correct order e.g::

  /home/patrick/repo/dev/project/hatherleigh_net
  /home/patrick/repo/dev/app/login
  /home/patrick/repo/dev/app/story
  /home/patrick/repo/dev/app/base

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
      django-admin.py demo_data_story && \
      django-admin.py runserver

Release and Deploy
==================

https://github.com/pkimber/cloud_docs

Demo
====

Home page displays stories which have been published:
http://hatherleigh.info/
http://localhost:8000/

Create a story (as a non-trusted user):
http://hatherleigh.info/story/create/anon/
http://localhost:8000/story/create/anon/

Admin view:
http://hatherleigh.info/story/
http://localhost:8000/story/

FTP
http://hatherleigh.info/article/andrea.html

Issues
======

- Captcha image is being cut-off:
  https://github.com/mbi/django-simple-captcha/pull/50

  Workaround by installing an earlier version of pillow...
