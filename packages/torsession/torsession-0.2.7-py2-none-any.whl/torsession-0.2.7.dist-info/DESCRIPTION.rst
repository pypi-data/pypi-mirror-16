==========
Torsession
==========

Torsession is an async && sync session backend with Mongodb for Tornado.

Installation
============

.. code-block:: bash

    $ pip install torsession

Example
=======

Async example.

.. code-block:: python

    from torsession.async import SessionManager

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


Sync example.

.. code-block:: python

    from torsession.sync import SessionManager

    # Initialize SessionManager
    sm = SessionManager(pymongo.MotorClient())

    # create a new session or load a session
    session = sm.new_session()
    session = sm.load_session("session id")

    # set a key-value pair
    session.set(key, val)

    # get key
    val = session.get(key)

    # delete a key
    session.delete(key)

    # refresh session id
    session.refresh_id()

    # clear a session
    session.clear()


LICENSE
=======

MIT


