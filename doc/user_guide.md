# How to use the plugin

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

The plugin is divided in two separated packages that work togheter to import the resource from [Quixel Bridge][quixelbridge] to [Substance Painter][sbspainter]

To install them 

## (WINDOWS) Install Notes

## (LINUX) Install Notes

```eval_rst
.. warning::
    Linux users should set the sudo command to execute without password for the python executable of Substance Painter by
    editing the sudoers file (``sudo visudo``) adding this line below ``root ALL=(ALL) ALL``

    ``username ALL=(ALL) NOPASSWD: /opt/Allegorithmic/Substance_Painter/resources/pythonsdk/bin/python3``

    where username is the user that want to install this plugin.
```

I'm not a expert linux user so if are one and want to contribute to make the linux dependencie installation easier and better please head take a look
at the [dependencies installation function][dependecies_linux] for the linux platform.

Ideally for linux users would be to ask for the sudo password and pass it to the command using [``subprocess.Popen``][popen_doc] or even better not asking at
all for a password (but i think that on linux this is probably not possible)

[quixelbridge]: https://quixel.com/bridge
[sbspainter]: https://www.substance3d.com/products/substance-painter/
[dependecies_linux]: https://github.com/Raider-Arts/painter-megascan-link/blob/master/megascan_link_python/__init__.py#L60
[popen_doc]: https://docs.python.org/3/library/subprocess.html#subprocess.Popen
