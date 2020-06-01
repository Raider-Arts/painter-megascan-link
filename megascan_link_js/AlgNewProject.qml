
import QtQuick 2.7
import Painter 1.0
import QtWebSockets 1.0
import QtQuick.Controls 2.0
import QtQuick.Dialogs 1.2
import AlgWidgets 2.0
import QtQuick.Layouts 1.12
import "utility.js" as Util 


AlgDialog {
	id: createProjectDialog

	title: "Mesh Assets found in the import data"
	visible: false
	width: 400
	height: 150
	maximumHeight: height
	maximumWidth: width
	minimumHeight: height
	minimumWidth: width

	property var importData: {}

	signal importPressed(var importData)
	signal newProjectPressed(var importData)


	function openWithData(data) {
		createProjectDialog.importData = data
		createProjectDialog.open()
	}

	Rectangle {
		anchors.fill: parent
		color: createProjectDialog.color
		ColumnLayout {
			anchors.fill: parent
			anchors.margins: 10
			AlgLabel  {
				Layout.fillWidth: true
				text: "The Megascan assets imported contain one or more Mesh Assets do you want to create a new project using one of this 3D Asset or just import the textures in the current project? (Note: mesh files will not be imported)"
				wrapMode: Text.Wrap
			}
			Item {
				Layout.fillHeight: true
			}
			RowLayout {
				Item {
					Layout.fillWidth: true
				}
				AlgButton {
					id: importBtn
					text: "Import"
					onClicked: createProjectDialog.importPressed(createProjectDialog.importData)
				}
				AlgButton {
					id: newPrjBtn
					text: "New Project"
					onClicked: createProjectDialog.newProjectPressed(createProjectDialog.importData)
				}
			}
		}
	}
}
