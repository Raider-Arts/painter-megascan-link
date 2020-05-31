# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
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
        Dialog.resize(421, 381)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.impTab = QTabWidget(Dialog)
        self.impTab.setObjectName(u"impTab")
        self.connTab = QWidget()
        self.connTab.setObjectName(u"connTab")
        self.gridLayout_2 = QGridLayout(self.connTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.connTab)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.portNumber = QLineEdit(self.connTab)
        self.portNumber.setObjectName(u"portNumber")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portNumber.sizePolicy().hasHeightForWidth())
        self.portNumber.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.portNumber)

        self.timeoutNumber = QLineEdit(self.connTab)
        self.timeoutNumber.setObjectName(u"timeoutNumber")
        sizePolicy.setHeightForWidth(self.timeoutNumber.sizePolicy().hasHeightForWidth())
        self.timeoutNumber.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.timeoutNumber)

        self.label_2 = QLabel(self.connTab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.connTab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color:rgb(140, 140, 140)\n"
"}")
        self.label_3.setWordWrap(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_3)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)

        self.impTab.addTab(self.connTab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.askforproj = QCheckBox(self.groupBox)
        self.askforproj.setObjectName(u"askforproj")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.askforproj)

        self.logtoconsole = QCheckBox(self.groupBox)
        self.logtoconsole.setObjectName(u"logtoconsole")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.logtoconsole)


        self.verticalLayout_5.addLayout(self.formLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.impTab.addTab(self.tab, "")
        self.About = QWidget()
        self.About.setObjectName(u"About")
        self.gridLayout_6 = QGridLayout(self.About)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.About)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel{\n"
"	color: rgba(255, 255, 255, 100%);\n"
"	font-size: 18px;\n"
"	font-weight: 500;\n"
"}")

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.About)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"	color: rgb(130, 130, 130)\n"
"}\n"
"")
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.About)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
"	color: rgba(255, 255, 255, 100%);\n"
"	font-size: 14px;\n"
"	font-weight: 500;\n"
"}")

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.About)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)
        self.label_7.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.label_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout_6.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.impTab.addTab(self.About, "")

        self.verticalLayout.addWidget(self.impTab)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.helpIcon = QLabel(Dialog)
        self.helpIcon.setObjectName(u"helpIcon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.helpIcon.sizePolicy().hasHeightForWidth())
        self.helpIcon.setSizePolicy(sizePolicy1)
        self.helpIcon.setMinimumSize(QSize(24, 24))
        self.helpIcon.setBaseSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.helpIcon)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.saveBtn = QPushButton(Dialog)
        self.saveBtn.setObjectName(u"saveBtn")

        self.horizontalLayout.addWidget(self.saveBtn)

        self.cancelBtn = QPushButton(Dialog)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.impTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Megascan Link (Unofficial)", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Port Number:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Timeout (sec)", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Changing port number require a restart of the socket after the current timeout expires (so wait at least the current timeout to use the export on Bridge)", None))
        self.impTab.setTabText(self.impTab.indexOf(self.connTab), QCoreApplication.translate("Dialog", u"Connection", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"General", None))
#if QT_CONFIG(tooltip)
        self.askforproj.setToolTip(QCoreApplication.translate("Dialog", u"Dont show dialog asking if you want to create a new project when importing Megascan Assets that contain 3D meshes, the meshes are discarded and but the bitmaps are imported in the current opened project", None))
#endif // QT_CONFIG(tooltip)
        self.askforproj.setText(QCoreApplication.translate("Dialog", u"Dont ask to create new project", None))
        self.logtoconsole.setText(QCoreApplication.translate("Dialog", u"Print log to console", None))
        self.impTab.setTabText(self.impTab.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Import", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Megascan Link Plugin (Unofficial)", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Written by <a href=\"https://github.com/darkimage\" style=\"color: #55aaff\">Luca Faggion</a>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Want to contribute to the plugin?", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>If you would like to contribute to the development of the plugin you should visit the plugin repository on <a href=\"https://github.com/Raider-Arts/megascan-link\"><span style=\" text-decoration: underline; color:#55aaff;\">Github</span></a>.</p><p>If you need to report a bug or request a feature you can do it in the <a href=\"https://github.com/Raider-Arts/megascan-link/issues\"><span style=\" text-decoration: underline; color:#55aaff;\">issues page</span></a> of the repository or by sending a mail to <a href=\"mailto: luc-af@live.it\"><span style=\" text-decoration: underline; color:#55aaff;\">me</span></a> or to my <a href=\"mailto: team@raiderarts.net\"><span style=\" text-decoration: underline; color:#55aaff;\">team</span></a>.</p><p>I hope this plugin was usefull for you.</p><p>Have a great day!.</p></body></html>", None))
        self.impTab.setTabText(self.impTab.indexOf(self.About), QCoreApplication.translate("Dialog", u"About", None))
        self.helpIcon.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"todo add url\"><span style=\" text-decoration: underline; color:#55aaff;\">Help</span></a></p></body></html>", None))
        self.saveBtn.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.cancelBtn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

