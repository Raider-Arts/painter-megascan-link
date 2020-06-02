from PySide2 import QtCore, QtWidgets, QtGui
from . import icon

class PainterDropDown(QtWidgets.QPushButton):

	def __init__(self, parent=None):
		super().__init__(parent=parent)
		self._menu = QtWidgets.QMenu(self)
		self._menu.setFixedWidth(self.width())
		self._menu.addAction("testttt1")
		self._menu.addAction("testttt2")
		self._menu.addAction("testttt3")
		self._menu.addAction("testttt4")
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
							}""" % (icon.getIcon("dropdown_icon.png").replace('\\', '/')))

	def _setMenuSize(self):
		print(self.width())
		self._menu.setFixedWidth(self.width())