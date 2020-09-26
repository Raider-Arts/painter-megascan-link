# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(622, 275)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(Dialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setStyleSheet(u"QLabel {\n"
"	color: red;	\n"
"	font-size: 24px;\n"
"}")

        self.verticalLayout.addWidget(self.titleLabel)

        self.verticalSpacer_2 = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.descriptionLabel = QLabel(Dialog)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setStyleSheet(u"")
        self.descriptionLabel.setTextFormat(Qt.RichText)
        self.descriptionLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.descriptionLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.dontShowAgain = QCheckBox(Dialog)
        self.dontShowAgain.setObjectName(u"dontShowAgain")

        self.horizontalLayout.addWidget(self.dontShowAgain)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Help)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Megascan Link Error!", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Oops! Megascan link cannot be started!!", None))
        self.descriptionLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>The automatic dependencies installation script failed to install the needed dependency, this is most likely related to a user permission issue</p><p>To make the script work you need to <span style=\" font-weight:600; text-decoration: underline;\">manually install the missing dependency</span></p><p>To do so follow the <a href=\"https://painter-megascan-link.readthedocs.io/en/latest/user_guide_install.html#manual-dependencies-installation\"><span style=\" text-decoration: underline; color:#1e8dda;\">Guide</span></a> for each platform (Windows, Linux, MacOS)</p><p>Plain Link to guide (<a href=\"https://painter-megascan-link.readthedocs.io/en/latest/user_guide_install.html#manual-dependencies-installation\"><span style=\" text-decoration: underline; color:#1e8dda;\">https://painter-megascan-link.readthedocs.io/en/latest/user_guide_install.html#manual-dependencies-installation</span></a>)</p><p>Or press <span style=\" font-weight:600; text-decoration: underline;\">Help</span> to navigate to t"
                        "he documentation website</p></body></html>", None))
        self.dontShowAgain.setText(QCoreApplication.translate("Dialog", u"Don't show again", None))
    # retranslateUi

