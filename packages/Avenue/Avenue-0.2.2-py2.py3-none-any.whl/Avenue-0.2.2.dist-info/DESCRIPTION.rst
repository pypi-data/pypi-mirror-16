Avenue: Highway routing.
=============================================

.. teaser-begin

Avenue is a very extensible, but lightweight, routing system.

* Free software: MIT license
* Documentation: http://documentation.creeer.io/avenue/
* Source-code: https://github.com/corverdevelopment/avenue/

A quick example:

.. code-block:: python

    from avenue import Avenue

    router = Avenue()

    @router.attach(path='/', method='GET')
    def hello_world():
        return 'Hallo world!'

    route = {
      'path': '/',
      'method': 'GET,
    }

    assert router.solve(**route) == 'Hallo world!'



