CUser, make email the USERNAME\_FIELD
=====================================

CUser makes it easy to use email address as your identification token
instead of a username.

CUser is a custom Django User model (extends ``AbstractBaseUser``) so it
takes a tiny amount of effort to use.

The only difference between CUser and the vanilla Django User is email
address is the ``USERNAME_FIELD`` (and username does not exist).

Why use CUser?
--------------

Because you still want everything in ``django.contrib.auth``, but you
also want users to **log in with email addresses**. And you don't want
to create your own custom User model or authentication backend.

Install & Set up
----------------

0. If you previously used Django's default User model,
   ``django.contrib.auth.User``, jump to **Notes** first (then come
   back). Otherwise, continue onward!

1. Install with ``pip install django-username-email``

2. Add ``cuser`` to your ``INSTALLED_APPS`` setting:

   .. code-block:: python

       INSTALLED_APPS = [
           ...
           'cuser',
       ]

3. Specify the custom model as the default user model for your project
   using the ``AUTH_USER_MODEL`` setting in your settings.py:

   .. code-block:: python

       AUTH_USER_MODEL = 'cuser.CUser'

4. Instead of referring to User directly, you should reference the user
   model using ``django.contrib.auth.get_user_model()``

5. Make migrations and migrate them to create CUser's models.

   .. code-block:: shell

       python manage.py makemigrations cuser
       python manage.py migrate



Notes
-----

If you have tables referencing Django's User model, you will have to
delete those table and migrations, then re-migrate. This will ensure
everything is set up correctly from the beginning.

When you define a foreign key or many-to-many relations to the User
model, you should specify the custom model using the ``AUTH_USER_MODEL``
setting.

For example:

.. code-block:: python

    from django.conf import settings
    from django.db import models

    class Profile(models.Model):
        user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
    )

License
-------

Released under the MIT license. See LICENSE for details.

Questions, comments, or anything else?
--------------------------------------

-  Open an issue
-  `Twitter <https://twitter.com/tomfme>`__
-  tom@meagher.co