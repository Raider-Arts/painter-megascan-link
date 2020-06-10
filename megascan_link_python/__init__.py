import importlib
import os
import platform
import subprocess
import sys
from pathlib import Path

import PySide2
from PySide2 import QtCore, QtGui, QtWidgets

import substance_painter.ui as sbsui

from . import config, dialogs, log, sockets
from . import utilities as util
from . import websocket_link
from .ui import (icon, painterdropdown, painterlineedit, painterslider,
                 painterslidercontrol)

importlib.reload(icon)
importlib.reload(dialogs)
importlib.reload(log)
importlib.reload(util)
importlib.reload(config)
importlib.reload(sockets)
importlib.reload(painterslider)
importlib.reload(painterslidercontrol)
importlib.reload(painterlineedit)
importlib.reload(painterdropdown)

def checkDependencies() -> bool:
	"""Check if dependencies are installed if not tries to install them

	This function is platform dependent

	.. warning::
		**WARNING FOR LINUX USERS**, they should set the sudo command to execute without password for the python executable of Substance Painter by
		editing the sudoers file (``sudo visudo``) adding this line below ``root ALL=(ALL) ALL``

		``username ALL=(ALL) NOPASSWD: /opt/Allegorithmic/Substance_Painter/resources/pythonsdk/bin/python3``

		where username is the user that want to install this plugin.

		refer to the :ref:`(LINUX) Install Notes` user guide for more details.

	:return: True if dependecies are present or successfully installed, False otherwise
	:rtype: bool
	"""
	try:
		import websocket as pd
		log.LoggerLink.Log("Dependecies already satisfied")
	except ImportError:
		print("Adding dependecies")
		pyInterpreter = None
		target = None
		cmdCall = []
		if platform.system() == "Windows":
			pyInterpreter = Path(os.__file__).parent.parent / "python.exe"
			target = str(pyInterpreter.parent / "lib/site-packages/")
			cmdCall = [str(pyInterpreter)]
		elif platform.system() == "Linux":
			# =================================================
			# WARNING FOR LINUX USERS, they should set the sudo commandd to execute without password for the python executable of Substance Painter
			# editing the visudo file adding this line below root ALL=(ALL) ALL
			# username ALL=(ALL) NOPASSWD: /opt/Allegorithmic/Substance_Painter/resources/pythonsdk/bin/python3
			# where username is the user that want to install this plugin
			pyInterpreter = Path(os.__file__).parent.parent.parent / "bin" / "python3"
			target = str(pyInterpreter.parent.parent / "lib")
			cmdCall = ["sudo", str(pyInterpreter)]
		else:
			log.LoggerLink.Log("Current Platform {} is not supported".format(platform.system()), log.logging.ERROR)
		try:
			cmdCall += ["-m", "pip", "install", "websocket-client"]
			subprocess.check_call(cmdCall)
		except Exception as e:
			log.LoggerLink.Log("Error during pip command: {}".format(e), log.logging.ERROR)
	finally:
		try:
			log.LoggerLink.Log("Check installed dependecies")
			import websocket as pd
			log.LoggerLink.Log("Dependencies are installed correctly")
			return True
		except ImportError:
			log.LoggerLink.Log("Dependecies error! cannot start plugin", log.logging.ERROR)
			return False

class Data(object):
	"""Dataclass used to store references to items so they dont get garbage collected
	"""    
	toolbar = None
	socket = None

def openSettingsDialog():
	"""Opens the Setings dialog for the user to change the socket port number and other import settings
	"""
	mainWindow = sbsui.get_main_window()
	dialog = dialogs.SettingsDialog(Data.socket,mainWindow)
	dialog.show()

def createToolBar():
	"""Creates the toolbar containing the action to open the Settings Dialog
	"""    
	Data.toolbar = sbsui.add_toolbar("Megscan Link", "megascanlink")
	qicon = QtGui.QIcon()
	qicon.addPixmap(icon.getIconAsQPixmap("megascan_logo_idle.png"))
	qicon.addPixmap(icon.getIconAsQPixmap("megascan_logo.png"), QtGui.QIcon.Active)
	action = Data.toolbar.addAction(qicon, None)
	action.triggered.connect(openSettingsDialog)

def start_plugin():
	"""**Entry point** of the plugin.

	Here we set up all the needed fucntionalities like the log the socket thread and we add to the painter toolbar the user interface ation
	"""
	# =================================================
	# Get reference to qt window of substance painter
	mainWindow = sbsui.get_main_window()

	# =================================================
	# Init the logger
	log.LoggerLink.setLoggerName("megascanlink")

	# =================================================
	# Initialize the config file
	config.ConfigSettings.setIniFilePath("settings")
	iniconf = config.configparser.ConfigParser()
	iniconf["Connection"] = {"port": "24981", "timeout": "5"}
	iniconf["General"] = {"outputConsole": "false", "askcreateproject":"true", "selectafterimport": "true"}
	iniconf["Bake"] = {"enabled": 'false', "resolution": '[12,12]', "maxreardistance": '0.5', "maxfrontaldistance": '0.6', 'average': 'true', 'relative': 'true', 'ignorebackface': 'true', 'antialiasing': 'Subsampling 2x2'}
	config.ConfigSettings.setUpInitialConfig(iniconf)

	if checkDependencies():
		createToolBar()
		# =================================================
		# start the socket
		Data.socket = sockets.SocketThread(mainWindow)
		Data.socket.start()
		log.LoggerLink.Log("Megascan Link Python correctly initialized")


def close_plugin():
	"""**Exit point** of the plugin.

	Here we perform the clean up before closing the plugin, stopping the socket thread and removing the toolbar action
	"""
	Data.socket.close()
	mainWindow = sbsui.get_main_window()
	if Data.toolbar:
		sbsui.delete_ui_element(Data.toolbar)
