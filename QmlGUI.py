import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

import os
print('Loading Tensorflow...')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # disable console warnings from tensorflow
from backend import Predict


class Person(QObject):
    def __init__(self):
        QObject.__init__(self)

    butLetter = pyqtSignal(str, arguments=["clicked"])

    @pyqtSlot(str)
    def clicked(self):
        data = Predict.recording()
        if Predict.voice_predicting(data, 'voice_model.h5'):
            letter = Predict.vowel_predicting(data, 'vowel_model.h5')
        else:
            letter = '---'
        self.butLetter.emit(letter)


app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

person = Person()
engine.rootContext().setContextProperty('personal', person)

engine.load('backend/view.qml')
engine.quit.connect(app.quit)

sys.exit(app.exec_())
