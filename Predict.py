import sounddevice as sd
from tensorflow.keras import models
import numpy as np
from librosa.feature import melspectrogram, mfcc


class Predict:
    def __init__(self):
        self.fs = 8000  # Sample rate
        self.seconds = 1  # Duration
        self.bits = 16  # Bit depth
        self.recording()
        if np.max(self.data) > 1:
            self.data = self.data / (2 ** (self.bits - 1))

    def recording(self):
        print('Recording...')
        myrecording = sd.rec(int(self.seconds * self.fs), self.fs, 1)
        sd.wait()  # Wait until recording is finished
        print('End of recording')
        myrecording = np.squeeze(myrecording)
        self.data = myrecording
        self.data = self.data[1000:8000].astype(np.float64)

    def voice_predicting(self, voice_model_path):
        model = models.load_model(voice_model_path)

        data = self.data
        data = melspectrogram(data, self.fs)
        data = np.expand_dims(data, 0)
        data = np.expand_dims(data, 3)

        predictions_single = model.predict(data)
        predictions = predictions_single[0]
        print(predictions)
        if predictions >= 0.5:
            voice = True
        else:
            voice = False
        return voice

    def vowel_predicting(self, model_path):
        model = models.load_model(model_path)

        data = self.data
        data = mfcc(data, self.fs)
        data = np.expand_dims(data, 0)
        data = np.expand_dims(data, 3)

        predictions_single = model.predict(data)
        predictions = predictions_single[0]
        print(predictions)
        t = 0.5
        if predictions[0] > t:
            letter = 'A'
        elif predictions[1] > t:
            letter = 'E'
        elif predictions[2] > t:
            letter = 'I'
        elif predictions[3] > t:
            letter = 'O'
        elif predictions[4] > t:
            letter = 'U'
        elif predictions[5] > t:
            letter = 'Y'
        else:
            letter = '----'
        return letter
