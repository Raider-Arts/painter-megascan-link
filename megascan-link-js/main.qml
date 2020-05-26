import QtQuick 2.7
import Painter 1.0
import QtWebSockets 1.0
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2
import AlgWidgets 2.0
import QtQuick.Layouts 1.12

PainterPlugin {
	id: megascanlink

	Component.onCompleted: {
		alg.log.info("Megascan-link-JS loaded")
	}

	function importResources(data) {
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

	function importMeshResources(data){
		alg.log.info("Importing Megascan Assets in the current project")

	}

	function createProjectWithResources(data) {
		alg.log.info("Creating project with resources")
		var urls = []
		data.forEach(asset => {
			asset.components.forEach(bitmap => {
				var lenght = urls.push(alg.fileIO.localFileToUrl(bitmap.path))
				alg.log.info(urls[lenght-1])
			})
		})
		alg.project.create(alg.fileIO.localFileToUrl(data[0].meshList[0].path), urls)
	}

	function checkForMeshAssets(data){
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
					createProjectWithResources(data)
				}
			});
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
							megascanlink.createProjectWithResources(createProjectDialog.importData)
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