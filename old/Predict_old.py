import sounddevice as sd
from tensorflow import keras
import numpy as np
import librosa

fs = 8000  # Sample rate
seconds = 3  # Duration
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

    data = data[0:24000]
    data = data.astype(np.float64)
    if np.max(data) > 1:
        data = data / (2 ** (bits - 1))
    data = librosa.feature.mfcc(data, fs)
    data = np.expand_dims(data, 0)

    predictions_single = model.predict(data)
    print(predictions_single[0])
    if np.argmax(predictions_single[0]) == 0:
        letter = 'A'
    elif np.argmax(predictions_single[0]) == 1:
        letter = 'E'
    elif np.argmax(predictions_single[0]) == 2:
        letter = 'I'
    elif np.argmax(predictions_single[0]) == 3:
        letter = 'O'
    elif np.argmax(predictions_single[0]) == 4:
        letter = 'U'
    elif np.argmax(predictions_single[0]) == 5:
        letter = 'Y'
    else:
        letter = 'err'  # prop too many outputs in a model
    return letter
