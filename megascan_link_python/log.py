"""This Module contains the logger facilities class 
"""

import logging
import sys

from . import config
from . import utilities as util


class LoggerLink(object):
	"""Class used to log messages to the log file

	see: :meth:`~referencefixer.log.LoggerLink.Log` for know how to use it to print also to the Python editor output
	"""	

	#: Logger name
	_name = ""

	#: Internal reference to the logger
	_logger = None

	#: Internal state of the logger
	_isSetup = False

	@classmethod
	def setLoggerName(cls, name: str):
		"""Set the current session logger name do this before using the logger and once,
		subseguent calls to this methos will have no effect

		:param name: the logger name
		:type name: str
		"""
		if(cls._name == "" and cls._isSetup == False):
			cls._name = name
			cls._logger = logging.getLogger(name)

	@classmethod
	def setUpLogger(cls):
		"""Method used to setup the current logger instance 

		Links the handler to print to the log file (log config path: './referencefixer.log')
		and set up the format to print with
		"""
		if cls._name == "":
			cls.setLoggerName("undefinedlog")
		cls._isSetup = True
		logFormatter = logging.Formatter("%(asctime)s [%(name)s] [%(levelname)s]  %(message)s")
		for handler in cls._logger.handlers:
			cls._logger.handlers.pop()
		filehandler = logging.FileHandler(util.getAbsCurrentPath('{}.log'.format(cls._name)), mode='a')
		filehandler.setFormatter(logFormatter)
		cls._logger.addHandler(filehandler)
		cls._logger.setLevel(logging.DEBUG)

	@classmethod
	def Log(cls, msg: str, logLevel=logging.INFO):
		"""Helper function used to log a massage to a file or if specified in the config file
		with the `outputConsole` propriety also to the Python Editor output of Substance Designer

		:param msg: the message to print
		:type msg: str
		:param logLevel: the log level to print with if it  is lower than the current :attr:`~megascan_link.log.LoggerLink._logger` level it would not be printed, defaults to logging.INFO
		:type logLevel: int, optional
		"""		
		conf = config.ConfigSettings()
		lvl = ""
		if not cls._isSetup:
			cls.setUpLogger()
		if logLevel == logging.INFO:
			lvl = "INFO"
			cls._logger.info(msg)
		if logLevel ==  logging.WARNING:
			lvl = "WARNING"
			cls._logger.warning(msg)
		if logLevel == logging.ERROR:
			lvl = "ERROR"
			cls._logger.error(msg)
		if logLevel == logging.DEBUG:
			lvl = "DEBUG"
			cls._logger.debug(msg)
		if conf.checkIfOptionIsSet("General", "outputConsole"):
			if logLevel >= cls._logger.level:
				print("[{}][{}] {}".format(cls._name,lvl,msg))
