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
	/** type:Object the current Megascan 3D asset used in the project */
	property var meshAsset: {}

	/**
	* Simply indicates that the plugin has been loaded correctly
	*/
	Component.onCompleted: {
		alg.log.info("Megascan-link-JS loaded")
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
	* Set up the baking parameters based on the user config preset parameters and then perform the bake
	* @param type:Object asset the asset to retrive the bake data from
	*/
	function setUpAndBake(asset){
		if((Object.keys(asset).length !== 0)) {
			alg.log.info("Setting up baking parameters and perform textures baking")
			var bakingParams = alg.baking.commonBakingParameters()
			alg.log.info(bakingParams)
			alg.log.info(megascanlink.settings.Bake)
			var bakeSettings = megascanlink.settings.Bake
			bakingParams.commonParameters.Output_Size = JSON.parse(bakeSettings.resolution)
			bakingParams.detailParameters.Average_Normals = Util.checkIfSettingsIsSet(bakeSettings.average)
			bakingParams.detailParameters.Ignore_Backface = Util.checkIfSettingsIsSet(bakeSettings.ignorebackface)
			bakingParams.detailParameters.Relative_to_Bounding_Box = Util.checkIfSettingsIsSet(bakeSettings.relative)
			bakingParams.detailParameters.Max_Rear_Distance = parseFloat(bakeSettings.maxreardistance)
			bakingParams.detailParameters.Max_Frontal_Distance = parseFloat(bakeSettings.maxfrontaldistance)
			bakingParams.detailParameters.Antialiasing = megascanlink.settings.Bake.antialiasing
			bakingParams.detailParameters.High_Definition_Meshes = Util.getHpMeshes(asset)
			alg.baking.setCommonBakingParameters(bakingParams)
			alg.baking.bake(alg.texturesets.getActiveTextureSet())
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
			// set the current project mesh asset 
			megascanlink.meshAsset = asset
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
	* Used to set up the textures set resolution and channel if a new project is being create by this plugin
	* Also set up and started, if requested in the config file, the baking process
	*/
	onActiveTextureSetChanged: function(stackPath) {
		// Called after the active texture set stack changes, 'activeTextureSetStack' contains the new active stack path.
		// The stack path may be empty if no texture set stack is active. This can happen when closing a project.
		if(megascanlink.projectCreated == true) {
			megascanlink.projectCreated = false
			alg.log.info("Changing texture set [{}] resolution to {}".format(stackPath, 4096))
			alg.texturesets.setResolution(stackPath, [12,12])
			if(Util.checkIfSettingsIsSet(megascanlink.settings.Bake.enabled)){
				megascanlink.setUpAndBake(megascanlink.meshAsset)
			}
		}
	}


	/**
	* This is the connection from which the python plugin forward the data retrived over socket from Quixel Bridge to this
	* plugin, here we can use the Substance Painter JS API to to do all the import actions needed
	*/
	WebSocketServer {
		listen: true
		port: 1212

		/**
		* This is the core of this plugin in which we receinve the data from the Python plugin the data we receive is a JSON object
		* containing the Quixel bridge data and the plugin setting retrived from the config file
		* ``` DATA {
			data: QuixelBridge json data
			settings: Config File json data
		}'''
		*/
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

	/**
	* Dialog showed to the user when the plugin can't save the current opened project
	*
	* This happens for example when the users as project opened that has not been saved to disk
	*/
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

	/**
	* Instance of AlgSelectDialog, this dialog is used for starting a new project with the mesh selected by the user from a list of
	* meshes in the megascan data currently being imported, if the are none or only one 3D mesh this dialog is not showed
	*/
	AlgSelectDialog {
		id: selectMesh

		onAccepted: {
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

	/**
	* Instance of AlgNewProject, this dialog is showed to the user if there is a 3D Mesh in the currently imported data.
	*
	* As Substance Painter only supports a single mesh per project we ask the user if he want to create a new project with the
	* the data he is currently importing.
	*
	* This dialog can be suppressed with the config option `askcreateproject` to `False`
	*/
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