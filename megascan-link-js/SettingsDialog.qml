import AlgWidgets 2.0
import QtQuick 2.7
import QtQuick.Layouts 1.3
import QtQuick.Window 2.12
import Painter 1.0

AlgWindow {
	id: settingsdialog
    minimumWidth: 400
    minimumHeight: 300
    title: "Megascan Link settings"
    flags: Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowTitleHint | Qt.WindowSystemMenuHint


	WebSocketServer {
		listen: true
		port: 1212

		onClientConnected: {
			alg.log.info("Python setting websocket found");
			webSocket.sendTextMessage("HELLO PYTHON")
		}
	}

	Component.onCompleted:{
		portnumber.text = alg.project.settings.value("portnumber")
	}

	ColumnLayout {
		AlgTabBar {
			id: root
			AlgTabButton {
				text: "Socket"
			}
			AlgTabButton {
				text: "Import"
			}
			AlgTabButton {
				text: "About"
			}
		}
		
		StackLayout {
			width: parent.width
			currentIndex: root.currentIndex
			Item {
				anchors.leftMargin: 5
				GridLayout {
					columns: 2
					rowSpacing: 1
					anchors.fill: parent
					anchors.leftMargin: 20
					anchors.topMargin: 10
					AlgLabel { text: "Port number:"}
					AlgTextInput {
						id: portnumber
						Layout.preferredWidth: 100
						onTextChanged: {
							alg.log.warn("edited: " + text)
							alg.project.settings.setValue("portnumber", text)
						}
					}
				}
			}
			Item {
				anchors.leftMargin: 5
			}
			Item {
				anchors.leftMargin: 5
			}
		}
	}
}