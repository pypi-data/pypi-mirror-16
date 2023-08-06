==========
Gearthonic
==========


A simple client for the API of Homegear.

Look at the documentation_ for detailed information.

Quickstart
==========

Install `gearthonic` via pip::

    pip install gearthonic

Initialise the client::

    from gearthonic import GearClient
    # You only have to provide the host and port of the Homegear server
    gc = GearClient('192.168.1.100', 2001, secure=False, verify=False)

Use the predefined methods to make requests to the API::

    gc.system.list_methods()
    gc.device.get_value(1, 4, 'ACTUAL_TEMPERATURE')

Alternatively you can call any method directly via the client::

    gc.getValue(1, 4, 'ACTUAL_TEMPERATURE')

The default communication protocol is XML-RPC. If you want to use another
protocol like JSON-RPC or a MQTT broker, see the full documentation_.

.. _documentation: http://gearthonic.readthedocs.io/en/latest/
