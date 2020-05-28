import QtQuick 2.7
import Painter 1.0
import QtWebSockets 1.0
import QtQuick.Controls 2.0
import QtQuick.Dialogs 1.2
import AlgWidgets 2.0
import QtQuick.Layouts 1.12

PainterPlugin {
	id: megascanlink

	Component.onCompleted: {
		alg.log.info("Megascan-link-JS loaded")
	}

	function importResources(data) {
		// Import the megascan assets textures in the project 
		// it saves them in the Megascan/AssetName path for each asset
		alg.log.info("Importing Megascan Assets in the current project")
		var urls = []
		data.forEach(asset => {
			asset.components.forEach(bitmap => {
				var lenght = urls.push(alg.resources.importProjectResource(bitmap.path,["texture"],"Megascan/"+ asset.name))
				alg.log.info(urls[lenght-1])
			})
		})
		alg.resources.selectResources(urls)
	}

	function createProjectWithResources(asset, imports) {
		// Create a new project using the mesh specified in the data source of the Megascan Asset
		// Data is a single Megascan asset
		if(alg.project.isOpen()){
			alg.log.info("Saving current project")
			alg.project.save("", alg.project.SaveMode.Full)
			alg.project.close()
		}
		alg.log.info("Creating project with resources, using mesh: "+ data.name)
		var bitmaps = []
		asset.components.forEach(bitmap => {
			var lenght = bitmaps.push(alg.fileIO.localFileToUrl(bitmap.path))
			alg.log.info("Loading mesh Texture: "+ bitmaps[lenght-1])
		})
		alg.project.create(alg.fileIO.localFileToUrl(asset.meshList[0].path), bitmaps)

		megascanlink.importResources(imports)
	}

	function checkForMeshAssets(data){
		// Serch in the Megascan import data if there is a Mesh Asset
		var hasMesh = false
		alg.log.info(data[0].type)
		data.forEach(asset => {
			if(asset.type == "3d" || asset.type == "3dplant"){
				hasMesh = true
			}
		})
		return hasMesh
	}

	WebSocketServer {
		// This is the connection from which the python plugin forward the data retriver over socket from bridge to this
		// plugin, here we can use the Substance Painter JS API to import the assets 
		listen: true
		port: 1212

		onClientConnected: {
			alg.log.info("Megascan-link-python plugin connection established");
			// The clientConnected signal is called with a webSocket object in parameter that represents
			// the newly created connection between the server and the client.
			webSocket.onTextMessageReceived.connect(function(message) {
				alg.log.info("receiving data from Megascan-link-python plugin")
				// var date = (new Date()).toLocaleTimeString();
				// alg.log.info("Message received at %1: %2".arg(date).arg(message));
				var data = JSON.parse(message)
				if(checkForMeshAssets(data) && alg.project.isOpen()){
					createProjectDialog.open()
					createProjectDialog.importData = data
				}else if(alg.project.isOpen()){
					importProjectResource(data)
				}else{
					selectMesh.open()
					selectMesh.addAssets(data)
				}
			});
		}
	}

	AlgDialog{
		id: selectMesh
		title: "Select Megascan Asset Mesh for New Project"
		width: 400
		height: 300
		maximumHeight: height
		maximumWidth: width
		minimumHeight: height
		minimumWidth: width
		defaultButtonText: "Select"

		function addAssets(assets){
			alg.log.info(assets)
			assetList.clear()
			assets.forEach(asset => {
				assetList.append({name: asset.name + " (id:"+ asset.id +")"  , image: asset.previewImage, data: asset})
			})
		}

		onAccepted: {
			alg.log.info("Accepted")
			var meshAsset = assetList.get(assetListView.currentIndex).data
			var imports = []
			for (let i = 0; i < assetList.count; i++) {
				const asset = assetList.get(i).data;
				imports.push(asset)
			}
			imports.splice(assetListView.currentIndex,1)
			megascanlink.createProjectWithResources(meshAsset,imports)
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
						alg.log.info(index)
					}
				}
			}
		}
	}

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
						onClicked: {
							megascanlink.importResources(createProjectDialog.importData)
							createProjectDialog.close()
						}
					}
					AlgButton {
						id: newPrjBtn
						text: "New Project"
						onClicked: {
							selectMesh.open()
							selectMesh.addAssets(createProjectDialog.importData)
							createProjectDialog.close()
						}
					}
				}
			}
		}
	}

	onActiveTextureSetChanged: function(stackPath) {
		// Called after the active texture set stack changes, 'activeTextureSetStack' contains the new active stack path.
		// The stack path may be empty if no texture set stack is active. This can happen when closing a project.
		alg.log.info("onActiveTextureSetChanged: " + stackPath)
	}

}