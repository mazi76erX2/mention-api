Getting Started
===============

Getting your application tokens
+++++++++++++++++++++++++++++++

.. danger::

In order to use the mention-python API client, after you have created a mention account, you first need to acquire a access token. 

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

Take note that the ``account_id`` is is the red outline string of charaters inside the request example seen below: 

.. image:: getting_started_3.png

At this point, you can test out your application using the keys under "Your Application Tokens". The ``twitter.Api()`` object can be created as follows::

    import twitter
    api = twitter.Api(consumer_key=[consumer key],
                      consumer_secret=[consumer secret],
                      access_token_key=[access token],
                      access_token_secret=[access token secret])

Note: Make sure to enclose your keys in quotes (ie, api = twitter.Api(consumer_key='1234567', ...) and so on) or you will receive a NameError.

If you are creating an application for end users/consumers, then you will want them to authorize you application, but that is outside the scope of this document.

And that should be it! If you need a little more help, check out the `examples on Github <https://github.com/bear/python-twitter/tree/master/examples>`_. If you have an open source application using python-twitter, send us a link and we'll add a link to it here.
