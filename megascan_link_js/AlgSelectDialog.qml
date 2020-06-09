import QtQuick 2.7
import Painter 1.0
import QtWebSockets 1.0
import QtQuick.Controls 2.0
import QtQuick.Dialogs 1.2
import AlgWidgets 2.0
import QtQuick.Layouts 1.12
import "utility.js" as Util 

/**
* This dialog is presented to the user if, when creating a new project, there is more than one 3D Mesh asset in the
* import data.
*
* This dialogs allow the user to select a 3D Asset to use a the base mesh for the new project, if there are other 3D Assets only
* their bitmaps are imported.
*/
AlgDialog {
	id: selectDialog
	/** The tile of the dialog */
	title: "Select Megascan Asset Mesh for New Project"
	/** width of the dialog -size if fixed to `400x300` */
	width: 400
	/** height of the dialog -size if fixed to `400x300` */
	height: 300
	/** is set to be equal to the `height` variable this blocks the user to resize the dialog*/
	maximumHeight: height
	/** is set to be equal to the `width` variable this blocks the user to resize the dialog*/
	maximumWidth: width
	/** is set to be equal to the `height` variable this blocks the user to resize the dialog*/
	minimumHeight: height
	/** is set to be equal to the `width` variable this blocks the user to resize the dialog*/
	minimumWidth: width
	/** the accept button text of the dialog - default is `Select` */
	defaultButtonText: "Select"

	/** type:Object the list of 3d assets */
	property var assets: assetList
	/** type:int the current index selected in the list */
	property int currentIndex: assetListView.currentIndex

	/**
	* Add assets to the list widgets of the dialog
	* @param type:List the list of assets to add
	*/
	function addAssets(assets){
		assetList.clear()
		assets.forEach(asset => {
			assetList.append({name: "{} (id:{})".format(asset.name, asset.id), image: asset.previewImage, data: asset})
		})
	}

	/** 
	* Shorthand function to open the dialog and populate the asset list
	* @param type:List the list of assets to add to the dialog list
	*/
	function openWithAssets(assets) {
		selectDialog.addAssets(assets)
		selectDialog.open()
	}

	/** 
	* The List widget (ListView QML)
	*/
	ListView {
		parent: selectMesh.contentItem
		id: assetListView
		anchors.fill: parent
		anchors.margins: 10
		model: assetList
		header: headerList
		delegate: assetListDelegate
		focus: true
		highlight: Rectangle {
			color: 'grey'
		}
		ScrollBar.vertical: AlgScrollBar {}
	}
	
	/** The model of the list, it holds the data needed to populate the widget */
	ListModel {
		id: assetList
	}

	/** The header of the list */
	Component {
		id: headerList
		Rectangle {
			width: parent.width
			height: 24
			color: selectMesh.color
			Rectangle {
				width: parent.width
				height: 18
				color: '#1f1f1f'
				AlgLabel {
					anchors.fill: parent
					anchors.margins: 2
					text: "Select a 3D Megascan Asset:"
				}
			}
		}
	}

	/** This is component instanciated for each entry in the model (*assetList*)*/
	Component {
		id: assetListDelegate
		Item {
			width: parent.width
			height: 72
			RowLayout {
				spacing: 4
				Image {
					Layout.margins: 4
					Layout.preferredWidth: 64
					Layout.preferredHeight: 64
					fillMode: Image.PreserveAspectFit
					smooth: true
					source: "file:/"+image
				}
				AlgLabel {
					text: name
					Layout.leftMargin: 4
				}
			}
			MouseArea {
				anchors.fill: parent
				onClicked: {
					assetListView.currentIndex = index
				}
			}
		}
	}
}
