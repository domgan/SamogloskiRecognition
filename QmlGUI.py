import Predict
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

class Person(QObject):

    def __init__(self):
        QObject.__init__(self)

    butLetter = pyqtSignal(str, arguments=["clicked"])

    @pyqtSlot(str)
    def clicked(self):
        data = Predict.recording()
        letter = Predict.predicting(data, 'model.h5')
        self.butLetter.emit(letter)


app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

person = Person()
engine.rootContext().setContextProperty('personal', person)

engine.load('view.qml')
engine.quit.connect(app.quit)

sys.exit(app.exec_())

#    letter = 'hhhhhhhhhh'
#    helper.send_file(letter)
#    sys.exit(app.exec_())