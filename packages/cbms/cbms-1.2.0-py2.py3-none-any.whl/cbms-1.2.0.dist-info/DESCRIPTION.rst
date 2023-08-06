CBMS Api to the Sedona Virtual Machine
=======================

The CBMS API provides read/write capability from Python to the products from `CBMS Studio<http://www.cbmsstudio.com>`_'s `.

The CBMS products can be used as a gateway between a Python application and BACnet or Modbus systems.
For example, a Python program can be written to read/write from KNX and used to expose the values as BACnet objects.

----

The CBMS Studio Server runs on Windows, Linux, Raspberry PI and Blackberry and it exposes a 
REST web service for updating the IO values. These IO values can be exposed as BACnet or Modbus points
or they can be used within a Sedona Wiresheet for control and monitoring.

The CBMS API connects to the REST web service by sending HTTP Post messages to the server for
updating the IO values. The API provides an easy to user interface for sending the HTTP requests on to
the CBMS Server.



