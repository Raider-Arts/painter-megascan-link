Megascan Link Python Package
==============================
This package is the connection between Quixel Bridge and Substance Painter

The role of this package is to receive the JSON data from Bridge and send it over websocket to
the JS counterpart that will use that data to import the needed resources and to store and manage the configuration settings (:ref:`Config Module`).

The plugin has been divided into two plugins :ref:`Megascan Link Python Package` and :ref:`Megascan Link Javascript Package` because of the current
state of the Substance Painter API, what is possible with the JS API in not possible with the Python API and the other way around. Since 
this plugin makes use of some features that are not present in both API I had to split the plugin in half.


Python Subpackages
--------------------

.. toctree::

   megascan_link_python.ui

Python Submodules
-------------------

Plugin Module contents
-----------------------

.. automodule:: megascan_link_python
   :members:
   :undoc-members:
   :show-inheritance:

Config Module
------------------------------------

.. automodule:: megascan_link_python.config
   :members:
   :undoc-members:
   :show-inheritance:

Dialogs Module
-------------------------------------

.. automodule:: megascan_link_python.dialogs
   :members:
   :undoc-members:
   :show-inheritance:

Log Module
---------------------------------

.. automodule:: megascan_link_python.log
   :members:
   :undoc-members:
   :show-inheritance:

Sockets Module
-------------------------------------

.. automodule:: megascan_link_python.sockets
   :members:
   :undoc-members:
   :show-inheritance:

Utilities Module
---------------------------------------

.. automodule:: megascan_link_python.utilities
   :members:
   :undoc-members:
   :show-inheritance:

Websocket Link Module
---------------------------------------------

.. automodule:: megascan_link_python.websocket_link
   :members:
   :undoc-members:
   :show-inheritance:
