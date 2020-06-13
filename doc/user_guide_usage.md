# How to Use

## Basic Usage

## Features

## Plugin Settings
Here is the list of settings the plugin exposes
### Connection options
this options are used for the connection with Quixel Bridge make sure that the **Port number** is equal to the Port number in the **Custom Socket Export** option in **Quixel Bridge**

 Option        | Description | Default value
 ------------- |-------------| -------------
 Port Number | This is the port from which the plugin receive the data therefore **it must match they port set in the Custom Socket Export** of Quixel Bridge | 24981
 Timeout (sec) | This is the time the socket remains open and listening for a connection after the times expire the connection it is restarted automatically **NOTE:when you change the port number wait at least this value before trying to export from Quixel Bridge** | 5 seconds

```eval_rst 
.. warning::
    Be sure to insert the same port you have set in the **Export** options of Quixel Bridge
    
    .. image:: _static/port_number_sbs_bridge.jpg
```
