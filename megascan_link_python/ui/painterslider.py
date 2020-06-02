from PySide2 import QtCore, QtGui, QtWidgets
import re

class PainterSlider(QtWidgets.QSlider):

    def __init__(self, parent):
        super().__init__(QtCore.Qt.Orientation.Horizontal, parent=parent)
        self.valueChanged.connect(self._drawProgress)
        self.setStyleSheet("""QSlider::groove:horizontal {
                                border: none;
                                height: 2px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */
                                background: #666666;
                                margin: 2px 0;
                            }

                            QSlider::groove:horizontal:disabled {
                                background: #666666;
                            }

                            QSlider::handle:horizontal {
                                background: #cccccc;
                                border: none;
                                width: 10px;
                                margin: -4px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */
                                border-radius: 5px;
                            }

                            QSlider::handle:horizontal:disabled {
                                background: #666666;
                            }""")

    def _drawProgress(self, value):
        styleSheet = self.styleSheet()
        currstop = max(min((value+1)/100.0, 0.99), 0.01)
        lineargradient = f'qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #cccccc, stop:{currstop} #cccccc , stop:{currstop+0.01} #666666, stop:1 #666666);'
        newstylesheet = re.sub(r'(QSlider::groove:horizontal (?:.*?\n*?)*?background:)(.*)((?:.*\s*\n*)*)', f"\\1 {lineargradient} \\3", styleSheet)
        self.setStyleSheet(newstylesheet)


