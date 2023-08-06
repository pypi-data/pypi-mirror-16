Kyōkai (境界)
-------------

Kyōkai is a fast asynchronous Python server-side web framework. It is
built upon `asyncio <https://docs.python.org/3/library/asyncio.html>`__
and ``libuv`` for an extremely fast web server.

Setting up a Kyōkai app is incredibly simple. Here's a simple server
that echoes your client's headers:

.. code:: python

    import json
    from kyokai import Kyokai, Request, Response

    kyk = Kyokai("example_app")

    @kyk.route("/")
    async def index(request: Request):
        return json.dumps(request.headers), 200, {"Content-Type": "application/json"}
        
    kyk.run()

For more information, see the docs at https://mirai.veriny.tf.
