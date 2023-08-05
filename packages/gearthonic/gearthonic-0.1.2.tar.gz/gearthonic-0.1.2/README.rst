==========
Gearthonic
==========


A simple client to the XML RPC API of Homegear.

Look at the documentation_ for detailed information.

Quickstart
==========

Install `gearthonic` via pip::

    pip install gearthonic

Initialise the client::

    from gearthonic import GearClient
    gc = GearClient('192.168.1.100', 2001, secure=True)  # 2001 is the default port of the Homegear server

Use the predefined methods to make requests to the XML RPC API::

    gc.device.list_methods()
    gc.device.get_value(1, 4, 'ACTUAL_TEMPERATURE')

Alternatively you can call any method directly via the client::

    gc.getValue(1, 4, 'ACTUAL_TEMPERATURE')

.. _documentation: http://gearthonic.readthedocs.io/en/latest/
