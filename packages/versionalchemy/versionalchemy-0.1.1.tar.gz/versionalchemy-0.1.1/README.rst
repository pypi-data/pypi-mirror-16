VersionAlchemy
==============
A library built on top of the SQLAlchemy ORM for versioning 
row changes to relational SQL tables.

Authors: `Ryan Kirkman <https://www.github.com/ryankirkman/>`_ and
`Akshay Nanavati <https://www.github.com/akshaynanavati/>`_

Build Status
------------
.. image:: https://travis-ci.org/NerdWallet/versionalchemy.svg?branch=master
    :target: https://travis-ci.org/NerdWallet/versionalchemy
    
.. image:: https://readthedocs.org/projects/versionalchemy/badge/?version=latest
    :target: http://versionalchemy.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Useful Links
------------
- `Developer Documentation <http://versionalchemy.readthedocs.io/en/latest/>`_
- `Blog Post <https://www.nerdwallet.com/blog/engineering/versionalchemy-tracking-row-changes/>`_
  with more in depth design decisions

Getting Started
---------------

.. code-block:: bash

  $ pip install versionalchemy
  
TODO - any examples?
  
Contributing
------------
- Make sure you have `pip <https://pypi.python.org/pypi/pip>`_ 
  and `virtualenv <https://virtualenv.pypa.io/en/stable/>`_ on your dev machine
- Fork the repository and make the desired changes
- Run ``make install`` to install all required dependencies
- Run ``make lint tests`` to ensure the code is pep8 compliant and  all tests pass.
  Note that the tests require 100% branch coverage to be considered passing
- Open a pull request with a detailed explaination of the bug or feature
- Respond to any comments. The PR will be merged if the travis CI build passes and 
  the code changes are deemed sufficient by the admin

Style
~~~~~
- Follow PEP8 with a line length of 100 characters
- Prefer parenthesis to ``\`` for line breaks

License
-------
`MIT License <https://github.com/NerdWallet/versionalchemy/blob/master/LICENSE>`_
