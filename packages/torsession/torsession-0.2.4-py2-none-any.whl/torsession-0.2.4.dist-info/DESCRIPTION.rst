==========
Torsession
==========

Torsession is an asynchronous session backend with Mongodb for Tornado.

Installation
============

.. code-block:: bash

    $ pip install torsession

Example
=======

.. code-block:: python

    # Initialize SessionManager
    sm = SessionManager(motor.MotorClient())

    # create a new session or load a session
    session = yield sm.new_session()
    session = yield sm.load_session("session id")

    # set a key-value pair
    yield session.set(key, val)

    # get key
    val = yield session.get(key)

    # delete a key
    yield session.delete(key)

    # refresh session id
    yield session.refresh_id()

    # clear a session
    yield session.clear()

LICENSE
=======

MIT


