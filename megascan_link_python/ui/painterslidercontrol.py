from PySide2 import QtCore, QtGui, QtWidgets
from . import painterslider

class PainterSliderControl(QtWidgets.QWidget):
    
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.slider = painterslider.PainterSlider(self)
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setFixedWidth(50)
        self.lineEdit.setFixedHeight(16)
        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(self.slider)
        hlayout.addWidget(self.lineEdit)
        self.setLayout(hlayout)
