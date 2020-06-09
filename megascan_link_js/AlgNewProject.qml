
import QtQuick 2.7
import Painter 1.0
import QtWebSockets 1.0
import QtQuick.Controls 2.0
import QtQuick.Dialogs 1.2
import AlgWidgets 2.0
import QtQuick.Layouts 1.12
import "utility.js" as Util 

/**
* This dialog is presented to the user when there is a 3D Mesh asset in the import data
* and the config option `askcreateproject` is set to `True`
*
* The dialog asks the user if he want to import the assets bitmaps (since Painter only supports a single mesh per project)
* or wants to create a new project with one of them as the base mesh.
*/
AlgDialog {
	id: createProjectDialog
	/** The tile of the dialog */
	title: "Mesh Assets found in the import data"
	/** Visibility of the dialog - default is false */
	visible: false
	/** width of the dialog -size if fixed to `400x150` */
	width: 400
	/** height of the dialog -size if fixed to `400x150` */
	height: 150
	/** is set to be equal to the `height` variable this blocks the user to resize the dialog*/
	maximumHeight: height
	/** is set to be equal to the `width` variable this blocks the user to resize the dialog*/
	maximumWidth: width
	/** is set to be equal to the `height` variable this blocks the user to resize the dialog*/
	minimumHeight: height
	/** is set to be equal to the `width` variable this blocks the user to resize the dialog*/
	minimumWidth: width

	/** type:Object the JSON data currently being imported */
	property var importData: {}

	/**
	* Emitted when the user press the **Import** button
	* @param importData the JSON data currently being imported 
	*/
	signal importPressed(var importData)
	/**
	* Emitted when the user press the **New Project** button
	* @param importData the JSON data currently being imported 
	*/
	signal newProjectPressed(var importData)

	/**
	* Open the dialog feeding the JSON data coming from Quixel Bridge
	* @param type:Object data the Quixel Bridge JSON data
	*/
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
				/** Dialog Import button - emits the **importPressed** signal */
				AlgButton {
					id: importBtn
					text: "Import"
					onClicked: createProjectDialog.importPressed(createProjectDialog.importData)
				}
				/** Dialog New Projecy button - emits the **newProjectPressed** signal */
				AlgButton {
					id: newPrjBtn
					text: "New Project"
					onClicked: createProjectDialog.newProjectPressed(createProjectDialog.importData)
				}
			}
		}
	}
}
