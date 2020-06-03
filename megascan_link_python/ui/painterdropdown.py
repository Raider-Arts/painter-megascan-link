from PySide2 import QtCore, QtWidgets, QtGui
from . import icon
import os

class PainterDropDown(QtWidgets.QPushButton):
	"""Custom QPushButton widget that emulates the look and feel of Substance Painter native Drop Down Widget
	"""	

	def __init__(self, parent=None):
		super().__init__(parent=parent)
		self._currvalue = None
		self._options = []
		self._menu = QtWidgets.QMenu(self)
		self._menu.setFixedWidth(self.width())
		self._menu.setStyleSheet("""QMenu::item { height: 12px; margin: -2px; border: 3px solid #4d4d4d; }""")
		self._menu.aboutToShow.connect(self._setMenuSize)
		self.setMenu(self._menu)
		self.clearFocus()
		self.setStyleSheet("""QPushButton {
								background: #262626;
								height: 12px;
								border: 1px solid #4d4d4d;
							}
							QPushButton:hover {
								background: #1a1a1a;
							}
							QPushButton::menu-indicator {
								image: url(%s);
								subcontrol-position: right center;
								subcontrol-origin: padding;
								left: -2px;
							}""" % (icon.getIcon("dropdown_icon.png").replace(os.sep, '/')))

	def getValue(self):
		"""Get the current selected value

		:return: the current value selected
		:rtype: QVariant
		"""		
		return self._currvalue

	def setSelectedByData(self, data):
		"""Set programmatically the selected value of the Drop Down

		:param data: select the appropriate action in the QMenu by its action data
		:type data: QVariant
		"""		
		for i in range(len(self._options)):
			action = self._menu.actionAt(i)
			if action.data() == data:
				action.activate()

	def setSelectedByText(self, text):
		"""Set programmatically the selected value of the Drop Down

		:param data: select the appropriate action in the QMenu by its text
		:type data: str
		"""		
		for i in range(len(self._options)):
			action = self._menu.actionAt(i)
			if action.text() == text:
				action.activate()

	def _onMenuActionTrigger(self):
		"""Slot used to change the current value and the displayed text of the QPushButton when an option is selected
		"""		
		action = self.sender()
		self.setText(action.text())
		self._currvalue = action.data()

	def setOptions(self, options):
		"""Set the Action displayed by the Drop Down 

		:param options: the options to set, must be a list of tuple or nested array like ('display text', data) or ['display text', data]
		:type options: List|Tuple
		"""		
		self._options = options
		self._menu.clear()
		for opt in options:
			action = QtWidgets.QAction(opt[0], parent=self)
			action.setData(opt[1])
			action.triggered.connect(self._onMenuActionTrigger)
			self._menu.addAction(action)

	def _setMenuSize(self):
		"""Slot used to set the width of the QMenu exactly wide as the QPushButton before shwoing it
		"""		
		self._menu.setFixedWidth(self.width())