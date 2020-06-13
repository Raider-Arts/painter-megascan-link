# How to Use

## Basic Usage

## Features

## Plugin Settings
Here is the list of settings the plugin exposes

### Connection options
This options are used for the connection with Quixel Bridge make sure that the **Port number** is equal to the Port number in the **Custom Socket Export** option in **Quixel Bridge**

 Option        | Description | Default value
 ------------- |-------------| -------------
 Port Number | This is the port from which the plugin receive the data therefore **it must match they port set in the Custom Socket Export** of Quixel Bridge | 24981
 Timeout (sec) | This is the time the socket remains open and listening for a connection after the times expire the connection it is restarted automatically **NOTE:when you change the port number wait at least this value before trying to export from Quixel Bridge** | 5 seconds

```eval_rst 
.. warning::
    Be sure to insert the same port you have set in the **Export** options of Quixel Bridge
    
    .. image:: _static/port_number_sbs_bridge.jpg
```

### Import options
This options are applied to every import of Megascan Assets

 Option        | Description | Default value
 ------------- |-------------| -------------
 Dont ask to create new project | Option to suppress the dialog that warn the user that he imported a Megascan Asset containing a 3D Mesh and asking him if he want to create a new project with it (NOTE this dialog is only presented if this option is set to FALSE and when importing there is already and open project) | False
 Print Log to console | Option to pring DEBUG messages directly to the painter console (require restart) | False
 Select resouces after import | Automatically select imported resources after import (for easy drag and drop) | True

 ### Bake option
Enabling this option allow the plugin to perform a bake, with the preset values, after a successful import and project creation.

The bake is performed only when creating a new project (**New Project** pressed during the import, if there is an already project open, or when importing a Megascan Asset containing a 3D Mesh when there is no project open).

If the imported Megascan Asset has a High poly mesh the **High Poly (HP)** mesh list is automatically populated with the correct meshes.

 Option        | Description | Default value
 ------------- |-------------| -------------
Enable | Enable the baking process after successful project creation | False

```eval_rst
.. note::
    The options are the same as the ones in the bake window of Substance Painter
    
    .. image:: _static/bake_options_painter.png
```
