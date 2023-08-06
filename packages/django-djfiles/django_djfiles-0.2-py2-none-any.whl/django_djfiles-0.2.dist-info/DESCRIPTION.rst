|Coverage Status| |Build Status| |PyPI version| |licence|

DJFiles
=======

DJFiles is a simple Django app for manage static files of your project
in admin panel. This app is useful for projects where there is a content
manager, which don't have access to server via ssh or don't even know
what it is =)

Using this app you will be able to save static files through admin
panel. Files will be saved in /media/ directory of your project. It's
useful if you are not always have access to server or have a content
manager who responsible for managing such files.

Requirements
~~~~~~~~~~~~

-  Python >= 2.7
-  Django >= 1.8
-  unicode-slugify

Installation
~~~~~~~~~~~~

.. code:: bash

    $ pip install django-djfiles

Add ``djfiles`` to your INSTALLED\_APPS setting like this:

::

    INSTALLED_APPS = [
        ...

        'djfiles',
    ]

Apply ``djfiles`` migrations:

.. code:: bash

    $ ./manage.py migrate djfiles

Add urls to your project urls so you can get image by slug:

.. code:: bash

        urlpatterns += url(r'^djfiles/', include('djfiles.urls'))

.. |Coverage Status| image:: https://coveralls.io/repos/github/luminousmen/djfiles/badge.svg?branch=master
   :target: https://coveralls.io/github/luminousmen/djfiles?branch=master
.. |Build Status| image:: https://travis-ci.org/luminousmen/djfiles.svg?branch=master
   :target: https://travis-ci.org/luminousmen/djfiles
.. |PyPI version| image:: https://badge.fury.io/py/django-djfiles.svg
   :target: https://badge.fury.io/py/django-djfiles
.. |licence| image:: https://camo.githubusercontent.com/bcd5e9b1f7f3f648ca97add1262d43b0e31d25ec/687474703a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4253442d627269676874677265656e2e737667
   :target: https://github.com/luminousmen/djfiles/blob/master/LICENCE


