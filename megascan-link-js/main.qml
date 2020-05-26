import QtQuick 2.7
import Painter 1.0
import QtWebSockets 1.0
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2
import AlgWidgets 2.0
import QtQuick.Layouts 1.12

PainterPlugin {

	Component.onCompleted: {
		alg.log.info("Megascan-link-JS loaded")
	}

	WebSocketServer {
		listen: true
		port: 1212

		onClientConnected: {
			alg.log.info("Megascan-link-python plugin connection established");
			// The clientConnected signal is called with a webSocket object in parameter that represents
			// the newly created connection between the server and the client.
			// When we receive a message from a connected client, display it, then send back a message.
			webSocket.onTextMessageReceived.connect(function(message) {
				alg.log.info("receiving data from Megascan-link-python plugin")
				// var date = (new Date()).toLocaleTimeString();
				// alg.log.info("Message received at %1: %2".arg(date).arg(message));
				var data = JSON.parse(message)
				var urls = []
				alg.log.info(data[0].type)
				data.forEach(asset => {
					asset.components.forEach(bitmap => {
						var lenght = urls.push(alg.resources.importProjectResource(bitmap.path,["texture"],"megacan/"+ asset.name))
						alg.log.info(urls[lenght-1])
					})
				})
				alg.resources.selectResources(urls)
			});
		}
	}

	AlgDialog {
		id: createProjectDialog
		title: "Choose a date"
		visible: false
		width: 400
		height: 150
		maximumHeight: height
		maximumWidth: width
		minimumHeight: height
		minimumWidth: width
		Rectangle {
			anchors.fill: parent
			color: createProjectDialog.color
			ColumnLayout {
				anchors.fill: parent
				anchors.margins: 10
				AlgLabel  {
					Layout.fillWidth: true
					text: "The Megascan assets imported contain a Mesh Asset do you want to create a new project using this asset or import them in the current project? (Note that the mesh file will not be imported)"
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
							alg.log.warn("clicked")
						}
					}
					AlgButton {
						id: newPrjBtn
						text: "New Project"
						onClicked: {
							alg.log.warn("clicked")
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