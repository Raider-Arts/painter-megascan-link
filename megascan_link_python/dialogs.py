"""Module which contains all the dialogs used by the plugin

The dialogs are generated using QtDesigner and are located under /ui/uiDesign
and then converted to python code using the buildDialogs.py script
"""

import importlib

import PySide2
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import Qt

from .ui import settings_dialog, icon, painterslider
from . import config, log, sockets

importlib.reload(settings_dialog)
importlib.reload(painterslider)

class SettingsDialog(QtWidgets.QDialog, settings_dialog.Ui_Dialog):
	"""Dialog displayed to the user for editing the plugin settings
	"""    

	def __init__(self, socket: sockets.SocketThread, parent=None):
		super().__init__(parent=parent)
		self.setupUi(self)
		self._socketRef = socket
		self.needRestart = False
		self.helpIcon.setPixmap(icon.getIconAsQPixmap("help_icon.png",24))
		self.portNumber.setText(config.ConfigSettings.getConfigSetting("Connection", "port"))
		self.portNumber.setValidator(QtGui.QIntValidator(self))
		self.timeoutNumber.setText(config.ConfigSettings.getConfigSetting("Connection", "timeout"))
		self.timeoutNumber.setValidator(QtGui.QIntValidator(0, 60, self))
		self.portNumber.textChanged.connect(self._setNeedRestart)
		self.timeoutNumber.textChanged.connect(self._setNeedRestart)
		self.saveBtn.pressed.connect(self._saveSettings)
		self.cancelBtn.pressed.connect(lambda: self.close())
		self.askforproj.setCheckState(Qt.CheckState.Unchecked if config.ConfigSettings.checkIfOptionIsSet("General", "askcreateproject") else Qt.CheckState.Checked)
		self.logtoconsole.setCheckState(Qt.CheckState.Checked if config.ConfigSettings.checkIfOptionIsSet("General", "outputConsole") else Qt.CheckState.Unchecked)
		self.selectafterimport.setCheckState(Qt.CheckState.Checked if config.ConfigSettings.checkIfOptionIsSet("General", "selectafterimport") else Qt.CheckState.Unchecked)
		self.texSize.setOptions([['128','[7,7]'],['256','[8,8]'],['512','[9,9]'],['1024','[10,10]'],['2048','[11,11]'],['4096','[12,12]'],['8192','[13,13]']])
		self._setControlsStateOfWidget(self.bakeParametersGroup, True)

	def _setControlsStateOfWidget(self, widget: QtCore.QObject, state: bool):
		"""Set the state (Enabled/Disabled) of all the children of the input widget

		:param widget: the parent widget
		:type widget: QtCore.QObject
		:param state: the state to set to all the children
		:type state: bool
		"""		
		paramControls = widget.findChildren(QtWidgets.QWidget)
		for paramControl in paramControls:
				paramControl.setDisabled(not state)

	def _setNeedRestart(self, changeStr):
		"""Internal method used to set the needRestart variable used to restart the socket if the 
		port number or timeout values are changed by the user
		"""		
		self.needRestart = True
		log.LoggerLink.Log("Changed Port number or Timeout socket need to restart", log.logging.DEBUG)

	def _saveSettings(self):
		"""Save the changed settings to file then inform the socket thread if it need to restart himself
		"""
		config.ConfigSettings.updateConfigSetting("Connection", "port", self.portNumber.text(), False)
		config.ConfigSettings.updateConfigSetting("Connection", "timeout", self.timeoutNumber.text(), False)
		logtoconsoleState = True if self.askforproj.checkState() == Qt.CheckState.Checked else False
		config.ConfigSettings.updateConfigSetting("General", "outputConsole", logtoconsoleState, False)
		askcreateprojectState = False if self.askforproj.checkState() == Qt.CheckState.Checked else True
		config.ConfigSettings.updateConfigSetting("General", "askcreateproject", askcreateprojectState, False)
		selectafterimportState = True if self.selectafterimport.checkState() == Qt.CheckState.Checked else False
		config.ConfigSettings.updateConfigSetting("General", "selectafterimport", selectafterimportState, False)
		config.ConfigSettings.flush()
		if self.needRestart:
			self._socketRef.restart()
		self.close()

