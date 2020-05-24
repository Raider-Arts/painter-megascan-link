import importlib
import os
import platform
import subprocess
import sys
from pathlib import Path

import PySide2
from PySide2 import QtCore, QtGui, QtWidgets

import substance_painter.ui as sbsui

from . import dialogs, log, config
from . import utilities as util
from .ui import icon

importlib.reload(icon)
importlib.reload(dialogs)
importlib.reload(log)
importlib.reload(util)
importlib.reload(config)

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
			print("Check installed dependecies")
			import websocket as pd
			log.LoggerLink.Log("Websocket library is installed: {}".format(pd))
			return True
		except ImportError:
			log.LoggerLink.Log("Dependecies error! cannot start plugin", log.logging.ERROR)
			return False

class Data(object):
	"""Dataclass used to store references to items so they dont get garbage collected
	"""    
	toolbar = None

def openSettingsDialog():
	"""Opens the Setings dialog for the user to change the socket port number and other import settings
	"""
	mainWindow = sbsui.get_main_window()
	dialog = dialogs.SettingsDialog(mainWindow)
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
	# Init the logger
	log.LoggerLink.setLoggerName("megascanlink")

	# =================================================
	# Initialize the config file
	config.ConfigSettings.setIniFilePath("megascanlink")
	iniconf = config.configparser.ConfigParser()
	iniconf["Connection"] = {"port": "24981", "timeout": "5"}
	iniconf["General"] = {"outputConsole": "true"}
	config.ConfigSettings.setUpInitialConfig(iniconf)

	if checkDependencies():
		createToolBar()


def close_plugin():
	"""**exit point** of the plugin
	"""    
	mainWindow = sbsui.get_main_window()
	if Data.toolbar:
		sbsui.delete_ui_element(Data.toolbar)
