Readme
======

Docs can be found in the `docs <docs/index.md>`__ folder.

App Template
------------

This is a bare-bones skeleton app template, for use with the
``django-admin.py startapp`` command.

You will need ``git``, ``python 2.7+`` and ``pip`` to create a new app
with this template.

Create environment variables for the app and module name (e.g.
``django-foo-bar`` and ``foo_bar``), so we can use them in subsequent
commands:

::

    $ export APP=<app_name>
    $ export MODULE=<module_name>

Install or upgrade Django:

::

    $ pip install -U Django

Create an app from the template:

::

    $ mkdir $APP
    $ django-admin.py startapp -e ini,md,yml -n .coveragerc \
    --template=https://github.com/ixc/ixc-app-template/archive/master.zip \
    $MODULE $APP

Make the ``manage.py`` file executable, for convenience:

::

    $ cd $APP
    $ chmod 755 manage.py

Create a remote repository on `GitHub <https://github.com>`__, then
initialise a local repository and push an initial commit:

::

    $ git init
    $ git add -A
    $ git commit -m 'Initial commit.'
    $ git remote add origin git@github.com:ixc/$APP.git
    $ git push

Now, get to work on your app! You might want to start with:

-  Add a ``LICENSE.txt`` file (e.g.
   `MIT <http://choosealicense.com/licenses/mit/>`__).
-  Read the `contributing <docs/contributing.md>`__ docs.
-  Update the `docs <docs/index.md>`__ (e.g. overview, installation and
   usage).
-  Remove the ``App Template`` section (these instructions) from
   ``README.md`` (this file).


