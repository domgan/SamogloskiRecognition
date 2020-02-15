import sounddevice as sd
from tensorflow import keras
import numpy as np
import librosa


class Predict:
    def __init__(self):
        self.fs = 44100  # Sample rate
        self.seconds = 1  # Duration
        self.bits = 16  # Bit depth
        # print('Recording...')
        myrecording = sd.rec(int(self.seconds * self.fs), samplerate=self.fs, channels=1)
        sd.wait()  # Wait until recording is finished
        # print('End of recording')
        myrecording = np.squeeze(myrecording)
        self.data = librosa.resample(myrecording, self.fs, 8000)

    def voice_predicting(self, voice_model_path):
        model = keras.models.load_model(voice_model_path)

        data = self.data[0:8000]
        data = data.astype(np.float64)
        if np.max(data) > 1:
            data = data / (2 ** (self.bits - 1))
        data = librosa.feature.melspectrogram(data, self.fs)
        data = np.expand_dims(data, 0)
        data = np.expand_dims(data, 3)

        predictions_single = model.predict(data)
        predictions = predictions_single[0]
        print(predictions)
        if np.argmax(predictions) == 0:
            voice = True
        else:
            voice = False
        return voice

    def vowel_predicting(self, model_path):
        model = keras.models.load_model(model_path)

        data = self.data[0:8000]
        data = data.astype(np.float64)
        if np.max(data) > 1:
            data = data / (2 ** (self.bits - 1))
        data = librosa.feature.mfcc(data, self.fs)
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
