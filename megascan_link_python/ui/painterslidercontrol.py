from PySide2 import QtCore, QtGui, QtWidgets
from . import painterslider, painterlineedit

class PainterSliderControl(QtWidgets.QWidget):
    """Compound QWidget simulating the native Substance Painter Slider Control Widget look and feel
    """    
    
    def __init__(self, parent):
        self.currvalue = 0.0
        super().__init__(parent=parent)
        self.slider = painterslider.PainterSlider(self)
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.lineEdit = painterlineedit.PainterLineEdit(self)
        self.lineEdit.setValidator(QtGui.QDoubleValidator())
        self.lineEdit.setFixedWidth(50)
        self.lineEdit.setFixedHeight(16)
        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(self.slider)
        hlayout.addWidget(self.lineEdit)
        self.setLayout(hlayout)
        self.lineEdit.textEdited.connect(self._linkEditValue)
        self.slider.sliderMoved.connect(self._linkSliderValue)

    def _linkSliderValue(self, value: int):
        """Private Method used to link the slider value changes to the Line Edit widget

        :param value: the slide current value is in range from 0 to 100 (int)
        :type value: int
        """
        self.currvalue = float('%.3f' % (max(float(value) / 100.0 + 0.01, 0.0)))
        self.lineEdit.setText(str(self.currvalue))

    def _linkEditValue(self, value: str):
        """Private Method used to link the lineEdit changes to the slider

        :param value: string coming from the LineEdit widget
        :type value: string
        """        
        if (value == ""):
            value = 0.0
        self.currvalue = max(float(value), 0.0)
        self.slider.setValue(int(self.currvalue * 100.0))

    def setValue(self, value: float):
        """Set the control float value, this changes bot the slider and the Line Edit

        :param value: the float value to set
        :type value: float
        """
        self.currvalue = value
        self.lineEdit.setText(str(self.currvalue))
        self.slider.setValue(int(self.currvalue * 100.0))
    
    def setDisabled(self, state: bool):
        """Reinplementing the setDisabled method

        :param state: the state of the widget to set (Enabled(false)/Disabled(true))
        :type state: bool
        """        
        self.lineEdit.setDisabled(state)
        self.slider.setDisabled(state)
