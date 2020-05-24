import QtQuick 2.3
import QtQuick.Window 2.2
import QtQuick.Layouts 1.2

Item {
        width: 24
        height: 24
        objectName: "My plugin UI"
        property alias rectangle: rect

        Rectangle {
                id: rect
                anchors.fill: parent
                color: "red"
                MouseArea {
                        id: mouseArea
                        anchors.fill: parent
                        onClicked: {
                                var ok = alg.mapexport.showExportDialog();
                                if (ok) {
                                        alg.log.info("Export successful!")
                                } else {
                                        alg.log.warn("Export cancelled!")
                                }
                        }
                }
        }
}