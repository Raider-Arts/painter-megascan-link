
# Substance Painter Megascan Link Plugin ![painterversion](https://img.shields.io/badge/painter%20version-2020.1.2%20(6.1.2)-green) ![Tag Release](https://github.com/Raider-Arts/painter-megascan-link/workflows/Tag%20Release/badge.svg) ![pre-release](https://github.com/Raider-Arts/painter-megascan-link/workflows/pre-release/badge.svg)
This plugin enable the import of Megascan Assets using the export feature of [Quixel Bridge](https://quixel.com/bridge)

## Quick start guide

For a complete guide on all the options of the plugin refere to the [How to use documentation](https://painter-megascan-link.readthedocs.io/en/latest/?badge=latest).

 - Download the plugin from the [Release Page](https://github.com/Raider-Arts/painter-megascan-link/releases) or you can [build it yourself](todoaddlink.todo)

 - Install it in Substance Painter by exctracting the zip file in the documents folder:

	- **For Windows 10** ``%userprofile%\Documents\Allegorithmic\Substance Painter``
	- **For Linux** ``~/Documents/Allegorithmic/Substance Painter``
	- **For MacOS** ``/Users/%username%/Documents/Allegorithmic/Substance Painter``

> :information_source: After you have extracted the archive open up Substance Painter and enable both plugins python 
> ![enable plugins](doc/_static/enable_plugins.jpg)

 - Select a Megascan Asset you want to export then setup Quixel Bridge to the correct export option and then click Export (Default plugin port is **24981**)

    ![bridge export](doc/_static/bridge_setup.gif)

 - Import the currently exporting Megascan Asset to the current opened Substance Painter project:

    ![painter import](doc/_static/simple_import.gif)

 - Be sure to change the normal map **Color Space** to **Open Gl**

 	![color space](doc/_static/color_space.gif)

## Import assets into project example
In this short video you can see how to import Megascan Assets from Quixel Bridge to a Substance Painter project using the Plugin

![painter import](doc/_static/simple_import.gif)

## Create project importing assets
In this other video you can see how to you can automatically create a project importing some Megascan Assets from Quixel Bridge to Substance Painter

![create project](doc/_static/project_creation.gif)

## Want to contribute?
If you are willing to contribute you should start by [reading the dev docs](https://megascan-link.readthedocs.io/en/latest/).

**Done it?** all right it's time to clone this repository and start coding !!

After you made your changes don't forget to test them!! 

And please i'm trying to keep this plugin without any external dependencies for the ease of usage for everyone! so try to rely on what the already build-in python installation of Substance Designer has to offer

I hope this plugin helped you. 
