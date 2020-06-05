import importlib
import os
import platform
import subprocess
import sys
from pathlib import Path

import PySide2
from PySide2 import QtCore, QtGui, QtWidgets
from websocket import create_connection

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
	"""Check if dependencies are installed if not tries to install them (it is platform dependent??)

	:return: True if dependecies are present or successfully isntalled, False otherwise
	:rtype: bool
	"""
	try:
		import websocket as pd
		log.LoggerLink.Log("Dependecies already satisfied")
	except ImportError:
		pyInterpreter = None
		target = None
		if platform.system() == "Windows":
			pyInterpreter = Path(os.__file__).parent.parent / "python.exe"
			target = str(pyInterpreter.parent / "lib/site-packages/")
		else:
			log.LoggerLink.Log("Current Platform {} is not supported".format(platform.system()), log.logging.ERROR)
		subprocess.check_call([str(pyInterpreter), "-m", "pip", "install", "--target={}".format(target), "websocket-client"])
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
	"""**Entry point** of the plugin
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
		# start the sockets
		Data.socket = sockets.SocketThread(mainWindow)
		Data.socket.start()
		log.LoggerLink.Log("Megascan Link Python correctly initialized")


def close_plugin():
	"""**exit point** of the plugin
	"""
	Data.socket.close()
	mainWindow = sbsui.get_main_window()
	if Data.toolbar:
		sbsui.delete_ui_element(Data.toolbar)
