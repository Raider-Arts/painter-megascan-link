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
        self.tableWidget = QTabWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
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

        self.tableWidget.addTab(self.connTab, "")
        self.importTab = QWidget()
        self.importTab.setObjectName(u"importTab")
        self.verticalLayout_2 = QVBoxLayout(self.importTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.importTab)
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

        self.selectafterimport = QCheckBox(self.groupBox)
        self.selectafterimport.setObjectName(u"selectafterimport")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.selectafterimport)


        self.verticalLayout_5.addLayout(self.formLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.tableWidget.addTab(self.importTab, "")
        self.bakeTab = QWidget()
        self.bakeTab.setObjectName(u"bakeTab")
        self.verticalLayout_7 = QVBoxLayout(self.bakeTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.enableBaking = QCheckBox(self.bakeTab)
        self.enableBaking.setObjectName(u"enableBaking")

        self.verticalLayout_7.addWidget(self.enableBaking)

        self.bakeParameters = QGroupBox(self.bakeTab)
        self.bakeParameters.setObjectName(u"bakeParameters")
        self.formLayout_3 = QFormLayout(self.bakeParameters)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(10)
        self.label_9 = QLabel(self.bakeParameters)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLayoutDirection(Qt.LeftToRight)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.texSize = QPushButton(self.bakeParameters)
        self.texSize.setObjectName(u"texSize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.texSize.sizePolicy().hasHeightForWidth())
        self.texSize.setSizePolicy(sizePolicy1)
        self.texSize.setMinimumSize(QSize(0, 18))
        self.texSize.setMaximumSize(QSize(16777215, 18))
        self.texSize.setBaseSize(QSize(0, 18))
        self.texSize.setLayoutDirection(Qt.LeftToRight)
        self.texSize.setStyleSheet(u"QPushButton {\n"
"	background: #262626;\n"
"	border: 1px solid #4d4d4d;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.texSize)

        self.label_10 = QLabel(self.bakeParameters)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.checkBox = QCheckBox(self.bakeParameters)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.checkBox)

        self.label_11 = QLabel(self.bakeParameters)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.checkBox_2 = QCheckBox(self.bakeParameters)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.checkBox_2)

        self.label_12 = QLabel(self.bakeParameters)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_12)

        self.pushButton_2 = QPushButton(self.bakeParameters)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(0, 18))
        self.pushButton_2.setMaximumSize(QSize(16777215, 18))
        self.pushButton_2.setBaseSize(QSize(0, 18))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background: #262626;\n"
"	border: 1px solid #4d4d4d;\n"
"}")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.pushButton_2)

        self.label_13 = QLabel(self.bakeParameters)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_13)

        self.horizontalSlider = QSlider(self.bakeParameters)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 2px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: #cccccc;\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::groove:horizontal:disabled {\n"
"    background: #666666;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #cccccc;\n"
"    border: none;\n"
"    width: 10px;\n"
"    margin: -4px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"    background: #666666;\n"
"}")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.horizontalSlider)

        self.label_14 = QLabel(self.bakeParameters)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_14)

        self.horizontalSlider_2 = QSlider(self.bakeParameters)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setEnabled(True)
        self.horizontalSlider_2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: none;\n"
"    height: 2px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: #cccccc;\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::groove:horizontal:disabled {\n"
"    background: #666666;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #cccccc;\n"
"    border: none;\n"
"    width: 10px;\n"
"    margin: -4px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"    background: #666666;\n"
"}")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.horizontalSlider_2)


        self.verticalLayout_7.addWidget(self.bakeParameters)

        self.tableWidget.addTab(self.bakeTab, "")
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

        self.tableWidget.addTab(self.About, "")

        self.verticalLayout.addWidget(self.tableWidget)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.helpIcon = QLabel(Dialog)
        self.helpIcon.setObjectName(u"helpIcon")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.helpIcon.sizePolicy().hasHeightForWidth())
        self.helpIcon.setSizePolicy(sizePolicy2)
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

        self.tableWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Megascan Link (Unofficial)", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Port Number:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Timeout (sec)", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Changing port number require a restart of the socket after the current timeout expires (so wait at least the current timeout to use the export on Bridge)", None))
        self.tableWidget.setTabText(self.tableWidget.indexOf(self.connTab), QCoreApplication.translate("Dialog", u"Connection", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"General", None))
#if QT_CONFIG(tooltip)
        self.askforproj.setToolTip(QCoreApplication.translate("Dialog", u"Dont show dialog asking if you want to create a new project when importing Megascan Assets that contain 3D meshes, the meshes are discarded and but the bitmaps are imported in the current opened project", None))
#endif // QT_CONFIG(tooltip)
        self.askforproj.setText(QCoreApplication.translate("Dialog", u"Dont ask to create new project", None))
        self.logtoconsole.setText(QCoreApplication.translate("Dialog", u"Print log to console", None))
        self.selectafterimport.setText(QCoreApplication.translate("Dialog", u"Select resources after import", None))
        self.tableWidget.setTabText(self.tableWidget.indexOf(self.importTab), QCoreApplication.translate("Dialog", u"Import", None))
        self.enableBaking.setText(QCoreApplication.translate("Dialog", u"Enable Bake", None))
        self.bakeParameters.setTitle(QCoreApplication.translate("Dialog", u"Common Parameters", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Texture Size:", None))
        self.texSize.setText(QCoreApplication.translate("Dialog", u"TextureSize", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Relative to Bouding Box", None))
        self.checkBox.setText("")
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Average Normals", None))
        self.checkBox_2.setText("")
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Antialiasing", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Max Frontal Distance", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Max Rear Distance", None))
        self.tableWidget.setTabText(self.tableWidget.indexOf(self.bakeTab), QCoreApplication.translate("Dialog", u"Bake", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Megascan Link Plugin (Unofficial)", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Written by <a href=\"https://github.com/darkimage\" style=\"color: #55aaff\">Luca Faggion</a>", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Want to contribute to the plugin?", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>If you would like to contribute to the development of the plugin you should visit the plugin repository on <a href=\"https://github.com/Raider-Arts/megascan-link\"><span style=\" text-decoration: underline; color:#55aaff;\">Github</span></a>.</p><p>If you need to report a bug or request a feature you can do it in the <a href=\"https://github.com/Raider-Arts/megascan-link/issues\"><span style=\" text-decoration: underline; color:#55aaff;\">issues page</span></a> of the repository or by sending a mail to <a href=\"mailto: luc-af@live.it\"><span style=\" text-decoration: underline; color:#55aaff;\">me</span></a> or to my <a href=\"mailto: team@raiderarts.net\"><span style=\" text-decoration: underline; color:#55aaff;\">team</span></a>.</p><p>I hope this plugin was usefull for you.</p><p>Have a great day!.</p></body></html>", None))
        self.tableWidget.setTabText(self.tableWidget.indexOf(self.About), QCoreApplication.translate("Dialog", u"About", None))
        self.helpIcon.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"todo add url\"><span style=\" text-decoration: underline; color:#55aaff;\">Help</span></a></p></body></html>", None))
        self.saveBtn.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.cancelBtn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

