=========
ekomi API
=========

This package connect to EKOMI API.

License
-------

The package is released under the New BSD license.

Example of use
--------------

.. code-block:: python

    from ekomi import api

    ekomi_api = api.EkomiAPI('id', 'pw')

    result = ekomi_api.put_order('order_id', date)

    print result['link']
    print result['hash']
