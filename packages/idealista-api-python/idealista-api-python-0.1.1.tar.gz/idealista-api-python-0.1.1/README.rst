=============
Idealista API
=============

This package upload properties to Idealista using IDEALISTA API.

License
-------

The package is released under the New BSD license.

Example of use
--------------

.. code-block:: python

    from idealista import api

    idealista_api = api.IdealistaAPI('aggregator', 'code')

    result = idealista_api.get_xml({})

    print result
