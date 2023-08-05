mockbcrypt
==========

A mock bcrypt plugin for nosetests that answers the question: *how much time does every test take?*

.. image:: https://travis-ci.org/boneyao/mockbcrypt.png?branch=master
   :target: https://travis-ci.org/boneyao/mockbcrypt


Install
-------

To install the latest release from PyPI::

    pip install mockbcrypt

Or to install the latest development version from Git::

    pip install git+git://github.com/boneyao/mockbcrypt.git

Or to install the latest from source::

    git clone https://github.com/boneyao/mockbcrypt.git
    cd mockbcrypt
    pip install .

You can also make a developer install if you plan on modifying the
source frequently::

    pip install -e .



Usage
-----

Run nosetests with the ``--with-mockbcrypt`` flag, a
License
-------

``nose-mockbcrypt`` is an MIT Licensed library.


Contribute
----------

- Check for open issues or open a fresh issue to start a discussion around a
  feature idea or a bug.
- Fork the repository on GitHub to start making your changes to the master
  branch (or branch off of it).
- Write a test which shows that the bug was fixed or that the feature
  works as expected.
- Send a pull request and bug the maintainer until it gets merged and
  published.
- Make sure to add yourself to the author's file in ``setup.py`` and the
  ``Contributors`` section below :)


Contributors
------------

- `@boneyao <https://github.com/boneyao>`_
