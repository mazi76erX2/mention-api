Installation & Testing
------------

Installation
============

To get started, you’ll need to get an account at `Mention.com <http://mention.com>`_. Next, you’ll need to obtain your access token so you can make API requests:

Getting your application tokens
+++++++++++++++++++++++++++++++

In order to use the mention-python API client you first need to acquire a access token. 

Create your app
________________

Create a new `Mention App <https://dev.mention.com/apps/create>`_. Login using your mention details, click the "Create a new application" button and fill out the fields on the next page.


.. image:: getting_started_1.png

On the next screen, you'll see the applications that you've created. Click the "Edit" button to see the application that you created and some information about it:

Your app
_________

Once your app is created, you'll be directed to a new page showing you some information about it.

.. image:: getting_started_2.png
.. image:: getting_started_3.png

Your Keys
_________

Take note that the ``account_id`` is the string of charaters outlined in red inside the request example seen below: 

.. image:: getting_started_3.png

Lastly, install Python >= 3.6. Now you’re ready to install Mention-Python.

**From PyPI**

.. code-block:: console

    $ pip install mention-python

**From source**

Install the dependencies:

- `Requests <http://docs.python-requests.org/en/latest/>`_
- `Requests-oauth2 <https://github.com/maraujop/requests-oauth2/>`_

Alternatively use `pip`

.. code-block:: console

    $ pip install -r requirements.txt

Download the latest `mention-python` library from: https://github.com/mazi76erx2/mention-python/

Extract the source distribution and run

.. code-block:: console

    $ python setup.py build
    $ python setup.py install


Testing
=======

The following requires ``pip install pytest-cov``. Run

.. code-block:: console

    $ make test

If you would like to see coverage information

.. code-block:: console

    $ make coverage


Getting the code
================

The code is hosted at `Github <https://github.com/mazi76erX2/mention-python>`_.

Check out the latest development version anonymously with

.. code-block:: console

$ git clone git://github.com/mazi76erX2/mention-python.git
$ cd mention-python

At this point, you can test out your application using the key under "Access Token". The ``mention.FetchAnAlerAPI()`` object can be created as follows::

    import twitter
    alert = mention.FetchAnAlerAPI(access_token='access_token',
    							   account_id='account_id',
    							   alert_id='alert_id')