Megascan Link Javascript Package
================================
This package is responsible to utilize the Substance Painter API to import the Megascan Assets into the current opened project.

It receives the data over websocket from the :ref:`Megascan Link Python Package`.

Utility
----------

	.. js:autofunction:: checkIfSettingsIsSet

	.. js:autofunction:: getHpMeshes

	.. js:autofunction:: removeFromAssets


String Extensions
-----------------

	.. js:autoattribute:: String#format

QML Modules
-----------
	.. autodoxygenfile:: main.qml

	.. autodoxygenfile:: AlgNewProject.qml

	.. autodoxygenfile:: AlgSelectDialog.qml