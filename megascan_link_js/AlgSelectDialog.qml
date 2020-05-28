import QtQuick 2.7
import Painter 1.0
import QtWebSockets 1.0
import QtQuick.Controls 2.0
import QtQuick.Dialogs 1.2
import AlgWidgets 2.0
import QtQuick.Layouts 1.12
import "utility.js" as Util 


AlgDialog {
	id: selectDialog
	title: "Select Megascan Asset Mesh for New Project"
	width: 400
	height: 300
	maximumHeight: height
	maximumWidth: width
	minimumHeight: height
	minimumWidth: width
	defaultButtonText: "Select"

	property var assets: assetList
	property var currentIndex: assetListView.currentIndex

	function addAssets(assets){
		assetList.clear()
		assets.forEach(asset => {
			assetList.append({name: "{} (id:{})".format(asset.name, asset.id), image: asset.previewImage, data: asset})
		})
	}

	function openWithAssets(assets) {
		selectDialog.addAssets(assets)
		selectDialog.open()
	}

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
	

	ListModel {
		id: assetList
	}

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

	Component {
		id: assetListDelegate
		Item {
			id: rowListLayout
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
