.. _use_builtin_auth_system:

How to use Django builtin authentication system
===============================================

Prerequisites
-------------

In order to follow this how-to, you will need the following python packages:

.. literalinclude:: /../../source/use_builtin_auth_system/requirements.txt

.. Note:: The finished code for this example can be found at `the github repo`_

Overview
--------

In this howto we will see how we can use the Django builtin authentication
system. Let's see the involved steps:

#. Create a new Django Website.

#. [Optionally] create a new Django App.

#. Edit the website's ``settings.py`` to enable the relevant applications and
   middleware classes. If you created a separate App then enable it to notify
   Django about it's existence

#. Write the required code that demonstrates the usage of Django's builtin
   ``auth`` system.

#. Add the necessary rules for the url routing at the ``urls.py`` of the website
   directory.

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

.. Note::

    This step is optional. We can write the relevant code both into the Website
    directory or create a new App.  Writing an App is probably the better
    option, since it will allow us to decouple the code from the website and
    make it easier to use it on other websites too.

In order to create our new App, which we will name ``accounts``, we have to
issue the following command::

    python manage.py startapp accounts

This command creates a new folder beside our website directory that has the
following structure::

    accounts
    ├── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py

We are going to use the ``accounts`` App as the App which is responsible for
handling the authentication of our site.

Edit ``settings.py``
~~~~~~~~~~~~~~~~~~~~

First of all, it is very convenient to put at the beginning of ``settings.py``
the following lines of code. They make path handling much much easier:

.. literalinclude:: /../../source/use_builtin_auth_system/mysite/mysite/settings.py
   :language: python
   :linenos:
   :lines: 3-9

This time, since we are going to use Django's builtin ``auth`` we are going to
need a database. So we need to set it up.  To keep things simple we are going to
use sqlite but you should use whatever database you plan on using on your real
Projects.

In order to tell django which database to use we have make the following
changes:

.. literalinclude:: /../../source/use_builtin_auth_system/mysite/mysite/settings.py
   :language: python
   :linenos:
   :lines: 20-30
   :emphasize-lines: 3-4

In order to use the Django builtin authentication system, it is necessary to
enable the ``django.contrib.auth.middleware.AuthenticationMiddleware`` and the
``django.contrib.auth``.  They both are enabled by default.

If we use a separate Django App for the authentication (as we do in this case)
then, we need to enable the App too in the ``INSTALLED_APPS``.  So the
``settings.py`` will look like this:

.. literalinclude:: /../../source/use_builtin_auth_system/mysite/mysite/settings.py
   :language: python
   :linenos:
   :lines: 103-111
   :emphasize-lines: 5

.. literalinclude:: /../../source/use_builtin_auth_system/mysite/mysite/settings.py
   :language: python
   :linenos:
   :lines: 126-138
   :emphasize-lines: 2,3,12


Write the views
~~~~~~~~~~~~~~~

In order to demonstrate Django's auth system we are going to use 7 views:

* ``auth_view`` (in order to avoid any confusion between this view function and
  Django's ``auth`` system in this view we use the suffix ``view``.

* ``login``
* ``loggedin``
* ``logout``
* ``invalid_login``
* ``register_user``
* ``register_success``

Registration Form
+++++++++++++++++

For the registration we are going to use a custom form. So we add a module named
``forms.py`` inside the ``accounts`` App:

.. literalinclude:: /../../source/use_builtin_auth_system/mysite/accounts/forms.py
   :language: python
   :linenos:

Views
+++++

The necessary imports in the ``views.py`` are the following ones:

.. literalinclude:: /../../source/use_builtin_auth_system/mysite/accounts/views.py
   :language: python
   :linenos:
   :lines: 1-7

The ``login`` view shows the form that gathers the username and the password of
the user:

.. literalinclude:: /../../source/use_builtin_auth_system/mysite/accounts/views.py
   :language: python
   :linenos:
   :lines: 10-12

The ``auth_view`` view is the following one:

.. literalinclude:: /../../source/use_builtin_auth_system/mysite/accounts/views.py
   :language: python
   :linenos:
   :lines: 15-24

The ``loggedin`` view is presented to the user after a successful login:

.. literalinclude:: /../../source/use_builtin_auth_system/mysite/accounts/views.py
   :language: python
   :linenos:
   :lines: 27-29

The ``invalid_login`` view is presented to the user after an unsuccessful login
attempt:

.. literalinclude:: /../../source/use_builtin_auth_system/mysite/accounts/views.py
   :language: python
   :linenos:
   :lines: 32-33

The ``logout`` view is presented to the user, after he clicks on the logout
button:

.. literalinclude:: /../../source/use_builtin_auth_system/mysite/accounts/views.py
   :language: python
   :linenos:
   :lines: 36-38

The ``register_user`` view, renders the form that gathers the user information
(username, password, etc) that is going to be stored in the Database:

.. literalinclude:: /../../source/use_builtin_auth_system/mysite/accounts/views.py
   :language: python
   :linenos:
   :lines: 41-53

The ``register_success`` view is presented to the user after a successful
registration:

.. literalinclude:: /../../source/use_builtin_auth_system/mysite/accounts/views.py
   :language: python
   :linenos:
   :lines: 56-57

Templates
+++++++++

If you look at the code in the views, you will see that we reference certain
templates. Well we need to write them too!

There are quite a few ways to handle the templates. In order to make our App
reusable it is quite convenient to add a ``templates`` folder in the root
directory and a separate ``templates`` directory into the ``acounts`` App.
Actually in order to avoid conflicts between the names of the templates of
our App and the names of the other Apps we must put our templates under
``accounts/templates/accounts``.

``mysite.urls``
---------------

.. code-block:: python

    urlpatterns = patterns('account',
        # ...
        url(r'^account/login$', 'mysite.views.login'),
        url(r'^account/auth$', 'mysite.views.auth_view'),
        url(r'^account/logout$', 'mysite.views.logout'),
        url(r'^account/loggedin$', 'mysite.views.loggedin'),
        url(r'^account/invalid$', 'mysite.views.invalid_login'),
        # ...
    )

``mysite.views``
----------------

.. _the github repo: https://github.com/pmav99/howto/tree/master/source/use_builtin_auth_system
