Plytix Retailers SDK for Python
===============================

The Plytix Retailers SDK for Python is a library designed to simplify the access to the Plytix Retailers API to applications developed in Python. The library gives you an easy way to manage your authentication and to consume the Retailers API services. Thanks to the Plytix Retailers SDK for Python, you can quickly integrate our platform in your site's back end.

You will find the all documentation and examples of how to use it at `the Plytix for developers page <https://plytix.com/developers/>`_.

Plytix Retailers SDK for Python is easy to use
----------------------------------------------

.. code-block:: python

   from plytix.retailers.client import PlytixRetailersClient

   client = PlytixRetailersClient('api-key', 'api-pwd')

Once you have the client, you can start to consume the Plytix Retailers API's services immediately. For example, you get a list of all sites you manage with:

.. code-block:: python

   sites = client.sites.list()
   for site in sites:
       print site.name

Only a few lines are needed to get a list of the sites you manage at Plytix. Quick and easy.


Links
-----

* `Plytix website <https://plytix.com>`_
* `Documentation <https://plytix.com/developers/>`_
* `Development version <https://bitbucket.org/plytixdevs/plytix-sdk-python>`_