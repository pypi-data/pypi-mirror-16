djdg django OAuth
====================

Djdg Django Oauth provides a simple signature middleware verification between apps

Support
-------
mail to zane.yaung@live.com

Requirements
------------

* Python 2.7
* Django  1.9

Installation
------------

Install with pip::

    pip install djdg-oauth

Add `djdg_oauth` to your `INSTALLED_APPS`

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'djdg_oauth',
    )

run migrate to add tables
.. code-block:: python

    python manage.py migrate djdg_oauth


list, add, del app secret::
.. code-block:: python

    python manage.py python manage.py listoauthapp {app_name}
    python manage.py python manage.py addoauthapp {app_name}
    python manage.py python manage.py deloauthapp {app_name}

add middleware::
.. code-block:: python

    MIDDLEWARE_CLASSES = (
    ...
    'djdg_oauth.middleware.DjdgAuthMiddleware',
)

add settings::
.. code-block:: python

    DJDG_AUTH = {
        "APPS": [
            {"appid": "xxxxxx", "secret": "xxxxxxxxxxxxxxxxxxx", "app": "xxx"},
              ....
        ]

        "FULL_ESCAPE_URL": [....] # full match url to escape auth check,
        "REGEX_ESCAPE_URL": [....] # regex match url to escape auth check
    }
)

Documentation
--------------


License
-------

djdg-oauth is released under the terms of the **BSD license**. Full details in ``LICENSE`` file.

Changelog
---------
