
"""Module containing classes for using and retriving icons files
"""
import os
import PySide2
from PySide2 import QtGui, QtCore

def getIcon(name: str) -> str:
    """Return the path to the specified icon
    :param name: icon filename
    :type name: str
    :return: absolute path to the icon
    :rtype: str
    """     
    return os.path.join(os.path.abspath(os.path.split(__file__)[0]), name)


def getIconAsQPixmap(name: str, scale: int = None) -> QtGui.QPixmap:
	"""Retrive a icon image as a QPixmap

	:param name: the icon filename
	:type name: str
	:param scale: the desired size to apply to the icon (squared size), defaults to None
	:type scale: int, optional
	:return: the icon as a QPixmap
	:rtype: QtGui.QPixmap
	"""
	if scale:
		return QtGui.QPixmap(getIcon(name)).scaled(scale,scale,QtCore.Qt.AspectRatioMode.IgnoreAspectRatio,QtCore.Qt.TransformationMode.SmoothTransformation)
	else:
		return QtGui.QPixmap(getIcon(name))