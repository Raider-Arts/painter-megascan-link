from websocket import create_connection
import PySide2
from PySide2 import QtWidgets, QtGui, QtCore


def sendDataToJs():
	ws = create_connection("ws://localhost:1212/")
	print("Sending 'Hello, World'...")
	ws.send("Hello, World")
	print("Sent")
	ws.close()

