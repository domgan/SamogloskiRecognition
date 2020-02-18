import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.5

Window {
    id: window
    visible: true
    width: 600
    height: 440
    maximumHeight: 440
    color: "#2e3436"
    title: qsTr("Vowel Recognition")

    Text {
        id: element
        x: 344
        y: 63
        width: 281
        height: 31
        color: "#e3e0e0"
        text: qsTr("Samogłoski Recognition")
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: parent.horizontalCenter
        clip: false
        font.pixelSize: 32
    }

    Text {
        id: element1
        x: 184
        y: 363
        width: 231
        height: 31
        color: "#e3e0e0"
        text: qsTr("A    E    I    O    U    Y      1 second recording")
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        anchors.horizontalCenter: parent.horizontalCenter
        font.weight: Font.Light
        font.pixelSize: 26
    }

    Item {
        id: samogloska
        x: 268
        y: 257
        width: 105
        height: 58
        anchors.horizontalCenter: parent.horizontalCenter

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


    Item {
        id: button
        width: 136
        height: 54
        anchors.horizontalCenter: parent.horizontalCenter
        property alias buttonText: innerText.text;
        property int borderWidth: 1
        property int borderRadius: 2
        scale: state === "Pressed" ? 0.96 : 1.0
        onEnabledChanged: state = ""
        signal clicked
        x: 252
        y: 170

        //define a scale animation
        Behavior on scale {
            NumberAnimation {
                duration: 100
                easing.type: Easing.InOutQuad
            }
        }

        //Rectangle to draw the button
        Rectangle {
            id: rectangleButton
            color: "#c0c4c1"
            radius: 6
            anchors.fill: parent
            border.width: 2
            border.color: "#999999"

            Text {
                id: innerText
                text: "RECORDING"
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.verticalCenter: parent.verticalCenter
                font.pointSize: 16
            }
        }

        //change the color of the button in differen button states
        states: [
            State {
                name: "Hovering"
                PropertyChanges {
                    target: rectangleButton
                    color: "grey"
                }
            },
            State {
                name: "Pressed"
                PropertyChanges {
                    target: rectangleButton
                    color: "red"
                }
            }
        ]

        //define transmission for the states
        transitions: [
            Transition {
                from: ""; to: "Hovering"
                ColorAnimation { duration: 200 }
            },
            Transition {
                from: "*"; to: "Pressed"
                ColorAnimation { duration: 10 }
            }
        ]

        //Mouse area to react on click events
        MouseArea {
            anchors.fill: parent
            hoverEnabled: true
            onEntered: { button.state='Hovering'}
            onExited: { button.state=''}
            onClicked: { personal.clicked(1);}
            onPressed: { button.state="Pressed" }
            onReleased: {
                if (containsMouse)
                  button.state="Hovering";
                else
                  button.state="";
            }
        }
    }


    Connections {
        target: personal
        onButLetter: {
            textEdit.text = clicked
        }
    }

}

/*##^##
Designer {
    D{i:4;anchors_height:47;anchors_width:87}D{i:3;anchors_height:47;anchors_width:87;anchors_x:277;anchors_y:239}
D{i:8;anchors_height:45;anchors_width:47;anchors_x:-66;anchors_y:32}D{i:9;anchors_x:13;anchors_y:-47}
}
##^##*/
