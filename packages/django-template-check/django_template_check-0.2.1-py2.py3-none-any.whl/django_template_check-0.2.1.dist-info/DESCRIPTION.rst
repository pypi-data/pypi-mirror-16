django-template-check
=====================

This package makes it possible to easily check for basic syntax errors in all loaded Django templates. This can be useful as part of a continuous integration step in a build process, so as not to discover these problems at runtime.

Currently, checking is very minimal, simply relying on the exceptions raised by Django's compile and render template pipeline. Furthermore, only the default Django template backend is tested and supported.

Requirements
------------

This package requires Django version 1.8 or greater, and has been tested with 1.10.

Installation
------------

Simply get the package from ``pip``:

::

    pip install django-template-check

Then make sure to add ``django_template_check`` to your ``INSTALLED_APPS`` in your ``settings.py``.

Usage
-----

After installing this package, simply use it by calling the management command:

::

    python manage.py templatecheck


License
-------

All included code is available under the CC0 1.0 Universal Public Domain Dedication.

django-template-check Changelog
===============================

0.2.1 (2016-08-11)
------------------

- Fix a typo in the install instructions

0.2.0 (2016-08-11)
------------------

- Return 1 when there are errors.

0.1.1 (2016-08-11)
------------------

- Fix packaging to actually include code.

0.1.0 (2016-08-11)
------------------

- Initial working prototype



