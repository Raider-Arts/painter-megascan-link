# How to Install the plugin

## Download the plugin

You can download the plugin in the [realease](https://github.com/Raider-Arts/megascan-link/releases) tab of the github project page

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

## (LINUX) Install Notes

```eval_rst
.. warning::
    Linux users should set the sudo command to execute without password for the python executable of Substance Painter by
    editing the sudoers file (``sudo visudo``) adding this line below ``root ALL=(ALL) ALL``

    ``username ALL=(ALL) NOPASSWD: /opt/Allegorithmic/Substance_Painter/resources/pythonsdk/bin/python3``

    where username is the user that want to install this plugin.
```

I'm not a expert linux user so if are one and want to contribute to make the linux dependencies installation easier and better please take a look
at the [dependencies installation function][dependecies_linux] for the linux platform.

Ideally for linux users would be better to ask for the sudo password and pass it to the dependencies install command using [``subprocess.Popen``][popen_doc] or even better not 
asking at all for a password (but i think that, on linux, this is probably not possible)

## (MacOS) Install notes

```eval_rst
.. warning::
    MacOS users should set the sudo command to execute without password for the python executable of Substance Painter by
    editing the sudoers file (``sudo visudo``) adding this line below ``%admin ALL=(ALL) ALL``

    ``username ALL=(ALL) NOPASSWD: /Applications/Substance\ Painter.app/Contents/Resources/pythonsdk/bin/python3``

    **NOTE the backward slash for escaping the space between Substance and Painter**

    where username is the user that want to install this plugin.
```

And again here like :ref:`(LINUX) Install Notes` if you want to improve the resource installation feel free to do so! head over the [dependencies installation function][dependecies_linux] for the code reference.

## Manual Dependencies Installation
In the case you can't manage to get the automatic dependencies installation working, you can install them yourself

- **Windows installation steps**
    > - open a terminal (`win+r` then write `cmd` and press enter)
    > - navigate to the Substance Painter Python installation folder
    `cd %pathtoSubtancePainter%\resources\pythonsdk`
    > - install the dependencies with the command `python.exe -m pip install websocket-client`
    > - verify the installation with the command `python.exe -m pip freeze`, in the output should be present this line `websocket-client=0.x.x`

- **Linux installation steps**
    > - open a terminal and navigate to `/opt/Allegorithmic/Substance_Painter/resources/pythonsdk/bin`
    > - install the dependencies with the command `sudo python3 -m pip install websocket-client`
    > - verify the installation with the command `sudo python3 -m pip freeze`, in the output should be present this line `websocket-client=0.x.x`

- **MacOS installation steps**
    > - open a terminal and navigate to `/Applications/Substance Painter.app/Contents/Resources/pythonsdk/bin`
    > - install the dependencies with the command `sudo python3 -m pip install websocket-client`
    > - verify the installation with the command `sudo python3 -m pip freeze`, in the output should be present this line `websocket-client=0.x.x`

[quixelbridge]: https://quixel.com/bridge
[sbspainter]: https://www.substance3d.com/products/substance-painter/
[dependecies_linux]: https://github.com/Raider-Arts/painter-megascan-link/blob/master/megascan_link_python/__init__.py#L60
[popen_doc]: https://docs.python.org/3/library/subprocess.html#subprocess.Popen
