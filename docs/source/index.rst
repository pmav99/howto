.. django-howto documentation master file, created by
   sphinx-quickstart on Sat Oct 19 13:09:06 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-howto's documentation!
========================================

Contents:

.. toctree::
   :maxdepth: 2

   create_site_with_no_apps
   create_site_with_apps
   use_builtin_auth_system

Prerequisites and other resources
=================================

Before reading the recipes presented in this how-to-guide you must have finished
the official django tutorial.

If you need more introductory material, we whole-heartedly recommend:

* `Effective Django`_ (written guide)
* `Getting started with Django`_ (videos + written guide)
* If you are more of a video-type learner, then definitely watch
  `Mike Hibbert's excellent tutorials on YouTube`_.

All three of them are excellent resources.

Terminology
===========

Generally speaking, the structure of a Django project will look a bit like the
following::

    root
    ├── manage.py
    ├── mywebsite
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── views.py
    │   └── wsgi.py
    ├── sample_app1
    │   ├── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── sample_app2
        ├── __init__.py
        ├── models.py
        ├── tests.py
        └── views.py

As we can see there is the ``root`` directory where everything else resides in.
The name of the ``root`` directory is not really important.  When you create
a new site using ``django-admin.py`` the ``root`` directory is given the same
name as your website.

Inside the ``root`` directory there is the ``website`` directory which is the
central directory of the project.  In there you will find files that are used
for the settings of your sites (``settings.py``) and for the url routing
(``views.py``).

The other folders (``sample_app*``) are applications folders and we will speak
about them later on.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Mike Hibbert's excellent tutorials on YouTube: https://www.youtube.com/playlist?list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD
.. _Effective Django: http://effectivedjango.com/index.html
.. _Getting started with Django: http://gettingstartedwithdjango.com/


