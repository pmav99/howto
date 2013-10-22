How to create a Django site with applications
=============================================

If you have already created a django site without applications, the you will
find it very easy to expand your knowledge to sites that use applications.

.. Note:: The finished code for this example can be found at `the github repo`_

Overview
--------

The procedure we have to follow is very similar to the one we followed for the
Django site with no applications. The main difference is that we need first to
create the new Django application and then to notify Django that our new
application is there. Let's see how:

#. create the new application by using the ``manage.py``.

#. open the ``settings.py`` of the website directory and add the name of the new
   application to the ``INSTALLED_APPS`` list.

#. open the ``views.py`` of the new application and write the views
   (functions/classes).

#. add the necessary rules for the url routing at the ``urls.py`` of the website
   directory.

Implementation
--------------

The first step, of course, is to create a new Django project::

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

Now we can proceed with creating our views at the ``views.py`` of our new app:

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

Test
~~~~

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
