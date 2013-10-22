.. _django_site_with_apps:

How to create a Django site with Apps
=====================================

Prerequisites
-------------

In order to follow this how-to, you will need the following python packages:

.. literalinclude:: /../../source/create_site_with_apps/requirements.txt

.. Note:: The finished code for this example can be found at `the github repo`_

Overview
--------

The procedure we have to follow is very similar to the one we followed on
":ref:`django_site_with_no_apps`". The main difference is that we need first to
create the new Django App and then to notify Django that our new App is there.
Let's see the involved steps in detail:

#. Create a new Django Website.

#. Create the new Django App using the ``manage.py``.

#. Edit ``settings.py`` of the website directory and add the name of the new
   application to the ``INSTALLED_APPS`` list.

#. Edit ``views.py`` of the new Django App and write the views
   (functions/classes).

#. Add the necessary rules for the url routing at the ``urls.py`` of the website
   directory.

In this example, in order to keep things simple, we are not going to bother with
models at all, but in your projects you are going to use them.  If you don't
then you probably shouldn't be using Django in the first place.  Serving static
pages can more easily be done with just html ;)

Implementation
--------------

Create the Django Website
~~~~~~~~~~~~~~~~~~~~~~~~~

The first step, of course, is to create a new Django Website::

    django-admin.py startproject mysite

After that command we are going to get the following directory structure::

    mysite                  # this is the root directory
    ├── manage.py
    └── mysite              # this is the website directory
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

Create the Django App
~~~~~~~~~~~~~~~~~~~~~

Now, we need to create our new application. We can do that by running the
following command::

    python manage.py startapp sample_app

This command creates a new folder beside our website directory that has the
following structure::

    sample_app
    ├── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py

As we can see, a django application is nothing more than an ordinary python
package.

Notify Django about the existence of the new App.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit the ``settings.py`` file and add a line with the name of the App to the
``INSTALLED_APPS`` tuple.

.. literalinclude:: /../../source/create_site_with_apps/mysite/mysite/settings.py
   :language: python
   :linenos:
   :lines: 116-128
   :emphasize-lines: 12

Write the views
~~~~~~~~~~~~~~~

Now we can proceed with creating our views at the ``views.py`` of our new App:

.. literalinclude:: /../../source/create_site_with_apps/mysite/sample_app/views.py
   :language: python
   :linenos:

Url routing
~~~~~~~~~~~

Finally we add the corresponding rule for routing at the ``urls.py`` of the
website directory:

.. literalinclude:: /../../source/create_site_with_no_apps/mysite/mysite/urls.py
   :language: python
   :linenos:
   :emphasize-lines: 18

Summing it up
~~~~~~~~~~~~~

At this point, the directory structure looks like this::

    mysite                  # this is the root directory
    ├── manage.py
    ├── mysite              # website directory
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── sample_app         # app directory
        ├── templates
        ├── __init__.py
        ├── models.py
        ├── tests.py
        └── views.py

In order to test our new site all we have to do is to run::

    python manage.py runserver

and visit the following address::

    http://127.0.0.1:8000/index/

.. Note:: We don't need to run ``python manage.py syncdb`` since we don't use
          a database.

Extending
---------

Of course, in real life, our sites are not going to be so simple :).

We are going to have many applications and each application is going to have
lots of views and for each view we are going to need a template file.  But
extending from what we got so far, should be really easy.

For example we probably will want a ``templates`` directory to hold our
templates.  Also, if we need a database, then we will add ``models.py`` too.  If
we have forms then we will add a ``forms.py`` etc.

So, the directory structure is going to look similar to this one::

    mysite                  # root directory
    ├── manage.py
    ├── mysite              # website directory
    │   ├── templates
    │   ├── __init__.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── views.py
    │   └── wsgi.py
    ├── sample_app1         # app1 directory
    │   ├── templates
    │   ├── __init__.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── sample_app2         # app2 directory
        ├── templates
        ├── __init__.py
        ├── forms.py
        ├── models.py
        ├── tests.py
        └── views.py

.. _the github repo: https://github.com/pmav99/howto/tree/master/source/create_site_with_apps
