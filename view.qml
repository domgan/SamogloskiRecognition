import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.5

Window {
    visible: true
    width: 640
    height: 480
    color: "#2e3436"
    title: qsTr("Samogłoski Recognition")

    Text {
        id: element
        x: 49
        y: 42
        width: 281
        height: 31
        color: "#e3e0e0"
        text: qsTr("Samogłoski Recognition")
        clip: false
        font.pixelSize: 24
    }

    Text {
        id: element1
        x: 99
        y: 79
        width: 231
        height: 42
        color: "#e3e0e0"
        text: qsTr("A    E    I    O    U    Y")
        font.pixelSize: 26
    }

    Item {
        id: samogloska
        x: 268
        y: 236
        width: 105
        height: 58

        Rectangle {
            id: rectangle1
            color: "#2e2d34"
            anchors.fill: parent
            border.width: 2
            border.color: "#dfd3d3"
        }

        TextEdit {
            id: textEdit
            color: "#dcd6d6"
            text: qsTr("-")
            anchors.fill: parent
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            clip: false
            font.pixelSize: 34
        }

    }


    Button {
        id: button1
        x: 249
        y: 161
        width: 143
        height: 46
        text: qsTr("RECORDING")
        layer.enabled: false
        highlighted: false
        flat: false
        autoRepeat: false
        font.bold: false
        font.pointSize: 14

        onClicked: {
            personal.clicked(1)
        }
    }

    Item {
        id: busy
        x: 36
        y: 400
        width: 47
        height: 45

        Rectangle {
            id: rectangle2
            color: "#ded4d4"
            radius: 36.5
            anchors.fill: parent
            border.width: 2
        }

        BusyIndicator {
            id: busyIndicator
            font.pointSize: 12
            running: false
            anchors.fill: parent
        }
    }


    Connections {
        target: personal
        onButLetter: {
            busyIndicator.running = true
            textEdit.text = clicked
            busyIndicator.running = false
        }
    }

}

/*##^##
Designer {
    D{i:4;anchors_height:47;anchors_width:87}D{i:3;anchors_height:47;anchors_width:87;anchors_x:277;anchors_y:239}
D{i:8;anchors_height:45;anchors_width:47;anchors_x:-66;anchors_y:32}D{i:9;anchors_x:13;anchors_y:-47}
}
##^##*/
