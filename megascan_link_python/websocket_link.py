from websocket import create_connection
import PySide2
from PySide2 import QtWidgets, QtGui, QtCore
from . import log, config
import json

class WebsocketLink(QtCore.QObject):
	"""Start up a single use websocket to send data over the JS plugin
	"""	
	def __init__(self, parent=None):
		super().__init__(parent=parent)

	def sendDataToJs(self, data: object):
		"""send the data to the JS plugin using a websocket with port 1212

		:param data: the json data to send
		:type data: object
		"""
		try:
			ws = create_connection("ws://localhost:1212/")
			log.LoggerLink.Log("Sending data to JS plugin")
			jsonData = {"data": data,
						"settings": config.ConfigSettings.getAsDict()}
			ws.send(json.dumps(jsonData))
			ws.close()
		except Exception as e:
			log.LoggerLink.Log("WEBSOCKET ERROR: {}".format(str(e)), log.logging.ERROR)
			log.LoggerLink.Log("CANNOT SEND DATA TO JS", log.logging.ERROR)

