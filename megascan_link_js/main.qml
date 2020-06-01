import QtQuick 2.7
import Painter 1.0
import QtWebSockets 1.0
import QtQuick.Controls 2.0
import QtQuick.Dialogs 1.2
import AlgWidgets 2.0
import QtQuick.Layouts 1.12
import "utility.js" as Util 


PainterPlugin {
	id: megascanlink
	/** type:bool global flag that indicates that a project has been created */
	property bool projectCreated: false
	/** type:Object the settings values of the user config file */
	property var settings: {}

	/**
	* Simply indicates that the plugin has been loaded correctly
	*/
	Component.onCompleted: {
		alg.log.info("Megascan-link-JS loaded")
	}

	onActiveTextureSetChanged: function(stackPath) {
		// Called after the active texture set stack changes, 'activeTextureSetStack' contains the new active stack path.
		// The stack path may be empty if no texture set stack is active. This can happen when closing a project.
		if(megascanlink.projectCreated == true) {
			megascanlink.projectCreated = false
			alg.log.info("Changing texture set [{}] resolution to {}".format(stackPath, 4096))
			alg.texturesets.setResolution(stackPath, [12,12])
		}
	}

	/**
	* Import the Megascan Assets textures in the project and put them in the Megascan/{AssetName} path for each asset
	* @param type:Object data Quixel Bridge Json data
	*/
	function importResources(data) {
		// Import the megascan assets textures in the project 
		// it saves them in the Megascan/AssetName path for each asset
		alg.log.info("Importing Megascan Assets in the current project")
		var urls = []
		data.forEach(asset => {
			asset.components.forEach(bitmap => {
				var lenght = urls.push(alg.resources.importProjectResource(bitmap.path,["texture"],"Megascan/{}".format(asset.name)))
				alg.log.info(urls[lenght-1])
			})
		})
		// select the assets in the browser if the user want it
		if(Util.checkIfSettingsIsSet(megascanlink.settings.General.selectafterimport)){
			alg.resources.selectResources(urls)
		}
	}

	/**
	* Create a new project using the defined asset as the Mesh Asset
	* @param type:Object asset Json data of the Mesh asset (Quixel Bridge)
	* @param type:Array imports Array of Json data of additonal resources to import in the newly created project
	*/
	function createProjectWithResources(asset, imports) {
		// Create a new project using the mesh specified in the data source of the Megascan Asset
		// Data is a single Megascan asset
		var err = false
		if(alg.project.isOpen()){
			alg.log.info("Saving current project")
			try {
				alg.project.save("", alg.project.SaveMode.Full)
				alg.project.close()
			} catch (error) {
				alg.log.error("Failed to create new project could not save current opened project")
				err = true
				saveError.open()
			}
		}
		if(!err) {
			alg.log.info("Creating project with resources, using mesh: {}".format(asset.name))
			var bitmaps = []
			asset.components.forEach(bitmap => {
				var lenght = bitmaps.push(alg.fileIO.localFileToUrl(bitmap.path))
				alg.log.info("Loading mesh Texture: {}".format(bitmaps[lenght-1]))
			})
			alg.project.create(alg.fileIO.localFileToUrl(asset.meshList[0].path), bitmaps)

			//Import additional resources if they are present
			if(Object.keys(imports).length !== 0){
				megascanlink.importResources(imports)
			}
			// set the global `projectCreated` variable informing other actions that we have created a new project
			megascanlink.projectCreated = true
		}
	}

	/**
	* Check if in the Bridge json data are present some Assets that have associated a Mesh Asset
	* @param type:Object data Quixel Bridge Json data to check
	* @return type:boolean returns True if there is an 3D Asset, False otherwise
	*/
	function checkForMeshAssets(data){
		// Serch in the Megascan import data if there is a Mesh Asset
		var hasMesh = false
		var count = 0
		var mesh = {}
		data.forEach(asset => {
			if(asset.type == "3d" || asset.type == "3dplant"){
				hasMesh = true
				count += 1
				mesh = asset
			}
		})
		return { hasMeshes: hasMesh, count: count, lastMesh: mesh, data: data}
	}

	/**
	* This is the connection from which the python plugin forward the data retrived over socket from Quixel Bridge to this
	* plugin, here we can use the Substance Painter JS API to to do all the import actions needed
	*/
	WebSocketServer {
		listen: true
		port: 1212

		onClientConnected: {
			alg.log.info("Megascan-link-python plugin connection established");
			// The clientConnected signal is called with a webSocket object in parameter that represents
			// the newly created connection between the server and the client.
			webSocket.onTextMessageReceived.connect(function(message) {
				alg.log.info("Receiving data from Megascan-link-python plugin")
				var pythondata = JSON.parse(message)
				var data = pythondata.data
				megascanlink.settings = pythondata.settings
				var meshCheck = checkForMeshAssets(data)
				if(meshCheck.hasMeshes && alg.project.isOpen() && Util.checkIfSettingsIsSet(megascanlink.settings.General.askcreateproject)){
					createProject.openWithData(meshCheck)
				}else if(alg.project.isOpen()){
					megascanlink.importResources(data)
				}else{
					if(meshCheck.count > 1){
						selectMesh.openWithAssets(data)
					}else {
						megascanlink.createProjectWithResources(meshCheck.lastMesh, Util.removeFromAssets(meshCheck.lastMesh, data))
					}
				}
			});
		}
	}

	AlgDialog {
		id: saveError
		title: "ERROR Could not save current project"
		defaultButtonText: "Ok"
		visible: false
		width: 400
		height: 100
		maximumHeight: height
		maximumWidth: width
		minimumHeight: height
		minimumWidth: width
		ColumnLayout {
			anchors.fill: parent
			anchors.margins: 10
			AlgLabel  {
				Layout.fillWidth: true
				text: "Could not save the project, please save or close the current project before trying to import Megascan Assets"
				wrapMode: Text.Wrap
			}
			Item {
				// spacer item
				Layout.fillWidth: true
				Layout.fillHeight: true
			}
		}

		onAccepted: saveError.close()
	}

	AlgSelectDialog {
		id: selectMesh

		onAccepted: {
			alg.log.info("Accepted")
			var meshAsset = assets.get(currentIndex).data
			var imports = []
			for (let i = 0; i < assets.count; i++) {
				const asset = assets.get(i).data;
				imports.push(asset)
			}
			imports.splice(currentIndex,1)
			megascanlink.createProjectWithResources(meshAsset,imports)
		}

	}

	AlgNewProject {
		id: createProject

		onImportPressed: {
			megascanlink.importResources(importData.data)
			createProject.close()
		}

		onNewProjectPressed : {
			if(importData.count > 1){
				selectMesh.open()
				selectMesh.addAssets(importData.data)
			}else{
				megascanlink.createProjectWithResources(importData.lastMesh, Util.removeFromAssets(importData.lastMesh, importData.data))
			}
			createProject.close()
		}
	}
}