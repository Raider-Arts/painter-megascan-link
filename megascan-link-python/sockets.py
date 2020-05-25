"""Module containing classes for managing the comunincation with the socket thread 
and the main thread (in which we can use the SDAPI)
"""
import io
import json
import socket
import sys
import time
from logging import DEBUG, INFO, WARNING
from PySide2 import QtCore
from . import config, log, websocket_link


class SocketThread(QtCore.QThread):
	"""Core plugin class that manages a socket process for receiving TCP packets from
	Quixel Bridge
	"""
	#: Signal that is fired whenever a packet is retrived over the socket
	#:
	#: :type: QtCore.Signal
	#: :param object: json dictionary containing the data
	#: :type ojbect: dict
	onDataReceived = QtCore.Signal(object)
	#: flag that indicates that the socket should stop in the next timeout frame
	#:
	#: see :meth:`~megascan_link.sockets.SocketThread.stop`
	#: 
	#: .. warning::
	#:      dont use this flag directly use instead the :meth:`~megascan_link.sockets.SocketThread.stop` methods
	shouldClose = False
	#: flag that indicates that a restart is been requested, the restart is processed in the next timeout frame,
	#: it is cleared (False) when the restart happen
	#:
	#: used for example if you want to change the listening port or the timeout duration
	#:
	#: see :meth:`~megascan_link.sockets.SocketThread.restart`
	#:
	#: .. warning::
	#:      dont use this flag directly use instead the :meth:`~megascan_link.sockets.SocketThread.restart` method instead
	shouldRestart = False
	#: variables that idicates if the socket has been started
	#:
	#: but it is not guarantee that it is listening 
	started = False

	def run(self):
		"""This is the method that manages the socket lifetime process

		To interact with the socket use the :meth:`~megascan_link.sockets.SocketThread.stop` and :meth:`~megascan_link.sockets.SocketThread.restart` method instead

		While this method is running the associated thread is kept alive **closing** the socket without requesting a **restart** will make this thread close too

		The socket is listening on the port specified on the config file and it is restarted every time the timeout duration expires (also setted from the config file)
		"""

		logger = log.LoggerLink()
		# get config settings
		conf = config.ConfigSettings()
		# get the port number
		port = int(conf.getConfigSetting("Connection", "port"))
		timeout = int(conf.getConfigSetting("Connection", "timeout"))

		# Create a TCP/IP socket
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.settimeout(timeout)
		#bind to an address and port
		server_address = ('localhost', port)
		logger.Log('trying to start up socket on {} with port {} and timeout {}'.format(server_address[0], server_address[1], timeout), INFO)
		while not self.started:
			try:
				sock.bind(server_address)
				self.started = True
			except Exception:
				logger.Log("Failed to start up socket .... retrying",INFO)
				time.sleep(1)

		if not self.started:
			return
		# Listen for incoming connections
		sock.listen(1)
		while True:
			if self._tryCloseSocket(sock):
				break
			# Wait for a connection
			try:
				logger.Log('waiting for a connection',DEBUG)
				self._receivedData = io.StringIO()
				self._connection, client_address = sock.accept()
				logger.Log('connection from {}'.format(client_address), DEBUG)
				# Receive the data in small chunks and gather it until there is no more
				while True:
					if self._tryCloseSocket(sock):
						break
					data =  self._connection.recv(16)
					if data:
						self._receivedData.write(data.decode("utf-8"))
					else:
						logger.Log('no more data from {}'.format(client_address), DEBUG)
						break
			except socket.timeout:
				logger.Log("socket timeout", DEBUG)
			else:
				# Clean up the connection
				data = self._receivedData.getvalue()
				if data:
					jsonObj = json.loads(data)
					self.onDataReceived.emit(jsonObj)
					websocket = websocket_link.WebsocketLink()
					websocket.sendDataToJs(data)
			finally:
				if hasattr(self, '_connection'):
					self._connection.close()
				self._receivedData.close()
		self.shouldClose = False
		if self.shouldRestart:
			logger.Log("Restarting socket", INFO)
			self.shouldRestart = False
			self.started = False
			self.run()
		self.started = False

	def _tryCloseSocket(self, sock) -> bool:
		"""Internal method used for testing if the socket should be closed
		based on the :attr:`~megascan_link.sockets.SocketThread.shouldClose` flag
		
		if it possible the socket is closed

		:param sock: socked to close
		:type sock: sock.Socket
		:return: True if the socket is being closed, False otherwise
		:rtype: bool
		"""
		if self.shouldClose:
			logger = log.LoggerLink()
			logger.Log("closing socket",INFO)
			sock.close()
			return True
		else:
			return False

	def restart(self):
		"""Set the needed flags to perform a socket restart

		.. note::
			The restart is performed only after the timeout duration
		"""        
		self.shouldClose = True
		self.shouldRestart = True

	def close(self):
		"""Set the needed flags to close the socket

		.. note::
			The close operatiob is performed only after the timeout duration
		"""       
		self.shouldClose = True
