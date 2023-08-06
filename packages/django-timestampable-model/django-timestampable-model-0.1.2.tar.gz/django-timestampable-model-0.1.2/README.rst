===========================
Django Timestampable Models
===========================

Django Timestampable model is a simple enhancement mixin that enables Django models to have a ``created_at``
and ``updated_at`` field that is always updated.

The main difference between this plugin and the many others out there that do the same, is that
Django Timestampable Models updated the ``updated_at`` field under any circumstance: fixture loading,
bulk updates, etc. whereas traditional Timestampable mixins only provide shorthand for ``auto_add`` and
``auto_add_now`` shortcuts for ``DateTimeField``  s.

Quick start
-----------

1. Add "django_timestampable" to your ``INSTALLED_APPS`` settings like this:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'django_timestampable',
    ]

2. Add ``TimestampableModel`` in your ``Model`` s like so:

.. code-block:: python

    class Stuff(TimestampableModel):

        some_attribute = CharField()

        ...

3. Run `python manage.py makemigrations` then `python manage.py migrate` to add the columns to your models
in your database.

Requirements
------------

No dependencies. Tested on `Django`_ 1.9 with Python 2.7.*

.. _Django: http://www.djangoproject.com/
