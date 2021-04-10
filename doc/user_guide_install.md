# How to Install

## Download the plugin

You can download the plugin in the [realease](https://github.com/Raider-Arts/painter-megascan-link/releases) tab of the github project page

##### Build types

- Development Build
    > This build is always updated as soon a commit is pushed on the master branch
    ```eval_rst
    .. warning::
        This builds can be very unstable or not working at all!
        So when use them expect them to not work or not behaving correctly
    ```

- Tagged Builds
    > The tagged builds are stable usable builds

## Install the Plugin

The plugin is divided in two separated packages that work togheter to import the resources from [Quixel Bridge][quixelbridge] to [Substance Painter][sbspainter]

To install them unzip the archive in the Substance Painter Document directory that is located in:

```eval_rst
.. note::
    **For Windows 10**
    ``%userprofile%\Documents\Allegorithmic\Substance Painter``
    or 
    ``%userprofile%\OneDrive\Documents\Allegorithmic\Substance Painter``

.. note::
    **For Linux**
    ``~/Documents/Allegorithmic/Substance Painter``

.. note::
    **For MacOS**
    ``/Users/%username%/Documents/Allegorithmic/Substance Painter``
```

If you want to install it by hand simply place respectively:

- the `megascan_link_python` folder to `%substance painter documents path%\python\plugins\` folder
- the `megascan_link_js` folder to `%substance painter documents path%\plugins\` folder

```eval_rst
.. note::
    if you had Substance Painter opened during the installation you should not be able to see the plugins listed to fix it 
    simply click ``Reload Plugin Folder`` for both the Python plugin and the Javascript plugin
```

```eval_rst
.. warning::
    **The plugins packages work together so both plugins should be enabled on Substance Painter!**
```
