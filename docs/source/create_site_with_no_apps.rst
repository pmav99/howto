How to create a Django site with no applications
================================================

Actually it is rather simple to create a django site with no applications.

The first step, of course, is to create a new django application::

    django-admin.py startproject mysite

which means that we are going to end with a directory structure like this one::

    mysite                  # this is the root directory
    ├── manage.py
    └── mysite              # this is the website directory
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

Now, all we have to do is to add a ``views.py`` to the website directory and to
add their corresponding templates.  Probably, we will want to place the
templates into a separate ``templates`` directory.  So the procedure is rather
straight-forward:

#. We write the views (``views.py``).
#. We write the templates (``mysite/templates/*.html``).
#. We add the necessary rules for the url routing (``urls.py``).

For example, the views.py could have the following 

Finally, the directory structure is going to look like this::

    root
    └── mysite
       ├── templates
       ├── __init__.py
       ├── settings.py
       ├── urls.py
       ├── views.py
       └── wsgi.py


Extending from here should be easy.  If you have forms then you can add
a ``forms.py`` within the ``mysite`` directory etc.
