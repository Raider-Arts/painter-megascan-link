import AlgWidgets 2.0
import QtQuick 2.7
import QtQuick.Layouts 1.3
import QtQuick.Window 2.12
import Painter 1.0

AlgToolBarButton {

	function openSettingsDialog() {
		var component = Qt.createComponent("SettingsDialog.qml");
		var window = component.createObject("control");
		window.show()
	}

	id: control
	tooltip: "Open Megascan Link settings"
	iconName: control.hovered && !control.loading ? "ui/megascan_logo.png" : "ui/megascan_logo_idle.png"

	onClicked: openSettingsDialog()
}
