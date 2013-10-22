.. _django_site_with_no_apps:

How to create a Django site with no Apps
========================================

Prerequisites
-------------

In order to follow this how-to, you will need the following python packages:

.. literalinclude:: /../../source/create_site_with_no_apps/requirements.txt

.. Note:: The finished code for this example can be found at `the github repo`_

Overview
--------

A Django project is really nothing more than a ``settings.py`` module, and
a Django App is really nothing more than a ``models.py`` module. Everything else
is truly optional.

In this howto we are going to show you how to create a simple Django site with no
Apps. As you will see it is rather simple:

#. Create a new Django Website.

#. Add a ``models.py`` to the website directory.

#. add a ``views.py`` to the website directory.

#. add the necessary rules for the url routing (``urls.py``).

In the following example, in order to keep things simple, we are not going to
bother with models at all, but in your projects you are going to use them.  If
you don't then you probably shouldn't be using Django in the first place.
Serving static pages can more easily be done with just html ;)

Implementation
--------------

Create the Django Website
~~~~~~~~~~~~~~~~~~~~~~~~~

The first step, of course, is to create a new Django Website::

    django-admin.py startproject mysite

which means that we are going to end with a directory structure like this one::

    mysite                  # this is the root directory
    ├── manage.py
    └── mysite              # this is the website directory
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

Write the views
~~~~~~~~~~~~~~~

Now we need to create a file named ``views.py`` into our website directory and
write the views functions/classes:

.. literalinclude:: /../../source/create_site_with_no_apps/mysite/mysite/views.py
   :language: python
   :linenos:

Url routing
~~~~~~~~~~~

Finally we have to add the corresponding rule for routing at the ``urls.py``:

.. literalinclude:: /../../source/create_site_with_no_apps/mysite/mysite/urls.py
   :language: python
   :linenos:
   :emphasize-lines: 18

Summing it up
~~~~~~~~~~~~~

At this point, the directory structure looks like this::

    mysite                  # this is the root directory
    ├── manage.py
    └── mysite              # this is the website directory
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── views.py
        └── wsgi.py

In order to test our new site all we have to do is to run::

    python manage.py runserver

and visit the following address::

    http://127.0.0.1:8000/index/

.. Note:: We don't need to run ``python manage.py syncdb`` since we don't use
          a database.

Extending
---------

Of course, in real life, our sites are not going to be so simple :).

We are going to have a lot of views and for each view we are going to need
a template file.  But extending from what we got so far, should be really easy.

For example we probably will want a ``templates`` directory within the website
directory to hold our templates.  Also, if we need a database, then we will add
``models.py`` too. If we have forms then we will add a ``forms.py`` etc.  So,
the directory structure is probably going to look more like the following one::

    root
    └── mysite
       ├── templates
       ├── __init__.py
       ├── forms.py
       ├── models.py
       ├── settings.py
       ├── urls.py
       ├── views.py
       └── wsgi.py

.. _the github repo: https://github.com/pmav99/howto/tree/master/source/create_site_with_no_apps
