"""Contain Helper Functions used in common tasks
"""

import PySide2
from pathlib import Path
from PySide2 import QtWidgets

def getAbsCurrentPath(append: str) -> str:
	"""Simple function to get the current script path

	:param append: path or filename to add
	:type append: str
	:return: the full path plus the append param
	:rtype: str
	"""	
	return str((Path(__file__).parent / append).absolute())