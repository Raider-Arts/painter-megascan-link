import re

from PySide2 import QtCore, QtGui, QtWidgets


class PainterLineEdit(QtWidgets.QLineEdit):
	"""QLine Edit widget extension to look an behave like the Substance Painter native one
	"""	

	def __init__(self, text, parent=None):
		super().__init__(text, parent)
		self.setAlignment(QtCore.Qt.AlignRight)
		self.setStyleSheet("""QLineEdit {
								background: #333333;
								border-bottom: 1px solid #333333;
							}

							QLineEdit:hover {
								background: #262626;
							}""" )
		shadow = QtWidgets.QGraphicsDropShadowEffect(self)
		shadow.setXOffset(0.0)
		shadow.setYOffset(1.0)
		shadow.setColor(QtGui.QColor(64,64,64,255))
		self.setGraphicsEffect(shadow)
	
	def focusInEvent(self, focus):
		"""Overridden QtWidget base class focusInEvent to set the background color when the user click (set focus) on this widget
		"""		
		styleSheet = self.styleSheet()
		newStyleSheet = re.sub(r'(QLineEdit\s*{.*?\s*?background\s*?:)(.*?);((?:.*\s*\n*)*)', f'\\1 #262626; \\3', styleSheet)
		self.setStyleSheet(newStyleSheet)
		return super().focusInEvent(focus)

	def focusOutEvent(self, focus):
		"""Overridden QtWidget base class focusInEvent to clear the background color when the user click away (loose focus) from this widget
		"""		
		styleSheet = self.styleSheet()
		newStyleSheet = re.sub(r'(QLineEdit\s*{.*?\s*?background\s*?:)(.*?);((?:.*\s*\n*)*)', f'\\1 #333333; \\3', styleSheet)
		self.setStyleSheet(newStyleSheet)
		return super().focusOutEvent(focus)
