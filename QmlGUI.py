import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

import os
print('Loading Tensorflow...')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # disable console warnings from tensorflow
from backend.Predict import Predict


class Person(QObject):
    def __init__(self):
        QObject.__init__(self)

    butLetter = pyqtSignal(str, arguments=["clicked"])

    @pyqtSlot(str)
    def clicked(self):
        predict = Predict()
        if predict.voice_predicting('voice_model.h5'):
            letter = predict.vowel_predicting('vowel_model.h5')
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
