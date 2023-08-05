Salesforce Oauth Request
========================

A bit of Requests driven utility code to drive the Salesforce.com Oauth2
Web flow. Use this module to login to a Salesforce account using just
the username and password. Good for tests and scripts which need
Salesforce access\_token access.


Installation
------------

.. code-block:: python

   pip install salesforce-oauth-request-yplan


Usage
-----

You need a Connected App defined in Salesforce so that you have all
these pieces of info:

1. ``client ID``
2. ``client secret``
3. ``redirect uri``

Now you can get an ``access_token`` and ``instance_url`` like this:

.. code-block:: python

    import salesforce_oauth_request

    result = salesforce_oauth_request.login(username=username,
                                            password=password,
                                            client_id=client_id,
                                            client_secret=client_secret,
                                            redirect_uri=redirect_uri)

    print "Access token:  {}".format(result['access_token'])
    print "Refresh token: {}".format(result['refresh_token'])
    print "Instance URL:  {}".format(result['instance_url'])

    # Now use access_token, instance_url for REST, SOAP, or BULK API access.


Options
-------

.. code-block:: python

    cache_session=True/False - default False

Pass the option ``cache_session=true`` to save the access token to
``~.sf_oauth`` to save time on repeated runs.

.. code-block:: python

    sandbox=True/False - default False

Pass ``sandbox=True`` to use a sandbox login. ## Testing
