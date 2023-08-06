Getting started
===============

The easiest way to run an ICEkit project is with Docker. It works on OS
X, Linux, and Windows.

If you are not yet familiar with Docker, check out our `Docker Quick
Start <https://github.com/ic-labs/django-icekit/docs/docker-quick-start.md>`__
guide and then come back here.

If you are still not yet ready for Docker, check out our `Manual
Setup <https://github.com/ic-labs/django-icekit/docs/manual-setup-guide.md>`__
guide, which covers all the things that Docker would otherwise take care
of.

Creating a new ICEkit project
=============================

::

    $ bash <(curl -L https://raw.githubusercontent.com/ixc/ixc-project-template/master/startproject.sh) <project_name> [destination_dir]

This script will create a new ICEkit project in a directory named
``<project_name>`` in the current working directory (or
``[destination_dir]``), ready to hack on.

It might need to install ``pip`` and ``virtualenv`` into your global
environment, and will prompt for confirmation if it does.

Running an ICEkit project with Docker
=====================================

::

    $ cd <project_name>
    $ docker-compose up

Some local setup will be performed on first run, which might take a
while, so make yourself a cup of tea. Subsequent runs will skip the
local setup unless the project dependencies have been updated.


