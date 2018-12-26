Mention-Python
==============

.. image:: https://img.shields.io/pypi/v/mention.svg
    :target: https://pypi.org/project/mention

.. image:: https://travis-ci.org/mazi76erX2/mention-python.svg?branch=master
    :target: https://travis-ci.org/mazi76erX2/mention-python

.. image:: https://codecov.io/gh/mazi76erX2/mention-python/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/mazi76erX2/mention-python

.. image:: https://readthedocs.org/projects/mention-python/badge/?version=latest
    :target: https://mention-python.readthedocs.org/en/latest

**A Python wrapper around the Mention API.**

.. code-block:: console

    $ python3 -m pip install mention


.. code-block:: python

    >>> from mention import FetchAMentionAPI
    >>> first_mention = FetchAMentionAPI('access_token', 'account_id', 
    ...	'alert_id', 'mention_id')

    >>> first_mention_data = first_mention.query()

    >>> title = first_mention_data['title']
    "Nando's launches their own food ordering app"

Features
--------

**Mention-Python** supports all of the App, Alert and Mention features of the Mention API.

- fetch mention's application data
- create, fetch, update, and delete an alert
- fetch all the alerts of an account
- fetch and curate (update) a mention from an alert
- fetch all mentions for an alert
- fetch all children mentions for a given mention
- mark all of an alert's mentions as read


Table of Contents
-----------------

.. toctree::
   :maxdepth: 3

   installation.rst
   getting_started.rst
   api.rst
   changelog.rst


Introduction
------------
Mention is a social media and web monitoring tool. The media monitoring tool provides real-time alerts for a company's keyword and allows users to monitor millions of sources in real time and in 42 languages.

This library provides a pure Python interface for the `Mention API <https://dev.mention.com/>`_. It works with Python 3.0+

`Mention <http://mention.com>`_. Mention is designed as a REST API with multiple clients: web (the web app, used on computers), iOS, and Android. A client is a program that will consume our API, that will use its endpoints and returned data.

What can this API do for you?

Integrate Mention capabilities into your own website, with your own layout and your own way of managing rights
Use Mention as an intelligent crawler and use its output in your own systems / workflow. You can do pretty much anything the web client can.

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
