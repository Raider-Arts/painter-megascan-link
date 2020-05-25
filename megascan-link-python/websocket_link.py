from websocket import create_connection
import PySide2
from PySide2 import QtWidgets, QtGui, QtCore
from . import log
import json

class WebsocketLink(QtCore.QObject):
	def __init__(self, parent=None):
		super().__init__(parent=parent)

	def sendDataToJs(self, data: object):
		ws = create_connection("ws://localhost:1212/")
		log.LoggerLink.Log("Sending data to JS plugin")
		ws.send(json.dumps(data))
		ws.close()

