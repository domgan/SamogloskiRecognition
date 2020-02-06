import sounddevice as sd
from tensorflow import keras
import numpy as np
import librosa

fs = 8000  # Sample rate
seconds = 1  # Duration
bits = 16  # Bit depth


def recording():
    print('Recording...')
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    print('End of recording')
    myrecording = np.squeeze(myrecording)
    return myrecording


def predicting(data, model_path):
    model = keras.models.load_model(model_path)

    data = data[0:8000]
    data = data.astype(np.float64)
    if np.max(data) > 1:
        data = data / (2 ** (bits - 1))
    data = librosa.feature.mfcc(data, fs)
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
