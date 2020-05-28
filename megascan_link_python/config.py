"""Module containing classes for managing the config settings files or related
"""
import configparser
import os
from pathlib import Path
from typing import List

from . import utilities as util


class ConfigSettings(object):
	"""Class that manages a config file
	"""    
	#: Contains the path to the ini config file (root dir of module) needs to be initialized
	path = None
	#: Config parser class instance
	config = configparser.ConfigParser()
	#: Current state of the config file
	opened = False

	@classmethod
	def setIniFilePath(cls, name: str):
		"""Set the filepath of the ini file

		:param name: the name of the config ini file (without extension)
		:type name: str
		"""
		cls.path = Path(util.getAbsCurrentPath(name + ".ini"))

	@classmethod
	def getConfigSettingAsList(cls, cat: str, prop: str, separator=",") -> List[str]:
		"""Helper function to retrive a config option as a list 

		:param cat:  Category name string
		:type cat: str
		:param prop: Propriety of the category to retrive as list
		:type prop: str
		:param separator: the saparator character used to split values in the config string value, defaults to ","
		:type separator: str, optional
		:return: the config settings as a List
		:rtype: List[str]
		"""        
		res = cls.getConfigSetting(cat, prop)
		if res == "":
			return list()
		return res.split(separator)

	@classmethod
	def removeConfigSettings(cls, cat: str, prop: str, flush=True) -> bool:
		"""Helper function used to clear an option entry of a Section

		:param cat: Category name string
		:type cat: str
		:param prop: Propriety of the category to remove
		:type prop: str
		:param flush: If true it will immediatly update the file on disk, defaults to True
		:type flush: bool, optional
		:return: return True if successfully delete False otherwise
		:rtype: bool
		"""
		cls.checkConfigState()
		res = cls.config.remove_option(cat,prop)
		if flush:
			with open(cls.path, 'w') as configFile:
				cls.config.write(configFile)
		return res

	@classmethod
	def updateConfigSetting(cls, cat: str, prop: str, value: str, flush=True):
		"""Helper function used to update a config propriety.

		:param cat: Category name string
		:type cat: str
		:param prop: Propriety of the category to update
		:type prop: str
		:param value: Value to associate to the propriety
		:type value: str
		:param flush: If true it will immediatly update the file on disk, defaults to True
		:type flush: bool, optional
		"""
		cls.checkConfigState()
		if not cls.config.has_section(cat):
			cls.config.add_section(cat)
		cls.config[cat][prop] = str(value)
		if flush:
			with open(cls.path, 'w') as configFile:
				cls.config.write(configFile)

	@classmethod
	def getConfigSetting(cls, cat: str, prop: str) -> str:
		"""Helper function to retrive a config propriety value.

		:param cat: Category name string
		:type cat: str
		:param prop: Propriety of the category to retrive
		:type prop: str
		:return: the propriety value
		:rtype: str
		"""
		cls.checkConfigState()
		# return cls.config[cat][prop]
		return cls.config.get(cat, prop, fallback="")
	
	@classmethod
	def getConfigCategory(cls, cat: str) -> dict:
		"""Helper function to retrive an entire category of the ini file

		:param cat: Category name string
		:type cat: str
		:return: the dictionary containing the proprities with their corrispective values, if the category does not exist and empty dictionary is returned
		:rtype: str
		"""
		cls.checkConfigState()
		if cls.config.has_section(cat):
			return cls.config[cat]
		else:
			return dict()
	
	@classmethod
	def checkConfigState(cls):
		"""Check if the current config file is opened if not and the file exist
		reads and load the content of it to the config parser
		"""        
		if not cls.opened and cls.path.exists():
			cls.config.read(cls.path)
			cls.opened = True


	@classmethod
	def setUpInitialConfig(cls, config: configparser.ConfigParser):
		"""Function to use a config parser instance to initialize the config file
		This will initialize the config file only if it does not exist

		:param config: The config instance to use for populating the initial value of the config
		:type config: configparser.ConfigParser
		"""        
		if not cls.path.exists():
			with open(cls.path, 'w') as configFile:
				config.write(configFile)

	@classmethod
	def checkIfOptionIsSet(cls, cat: str, prop: str) -> bool:
		"""Helper function that will check if a propriety of a section is set or not by confronting
		it with the following values ["true", "yes", "y", "ok"]

		:param cat: Category name string
		:type cat: str
		:param prop: Propriety of the category to check agains
		:type prop: str
		:return: if the propriety is set returns True, False otherwise
		:rtype: bool
		"""        
		if cls.getConfigSetting(cat, prop).lower() in ["true", "yes", "y", "ok"]:
			return True
		return False

	@classmethod
	def flush(cls):
		"""Helper function used to write the content to file
		"""	
		with open(cls.path, 'w') as configFile:
			cls.config.write(configFile)
		cls.config.read(cls.path)
		cls.opened = True
