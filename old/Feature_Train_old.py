import numpy as np
import librosa
import scipy.io

fs = 8000


def mfcc_from_mat(path, fs):
    mat = scipy.io.loadmat(path)
    mat = mat['y']
    mat = mat[0:16000, :]  # shorten to 2 seconds
    arr = []
    for i in range(mat.shape[1]):
        m = librosa.feature.mfcc(mat[:, i], fs)
        arr.append(m)
    return np.array(arr)


aaa = mfcc_from_mat('data/aaa.mat', fs)
eee = mfcc_from_mat('data/eee.mat', fs)
iii = mfcc_from_mat('data/iii.mat', fs)
ooo = mfcc_from_mat('data/ooo.mat', fs)
uuu = mfcc_from_mat('data/uuu.mat', fs)
yyy = mfcc_from_mat('data/yyy.mat', fs)

train_input = np.concatenate((aaa, eee, iii, ooo, uuu, yyy))


train_labels = np.zeros(180)
for i in range(30, 60):
    train_labels[i] = 1
for i in range(60, 90):
    train_labels[i] = 2
for i in range(90, 120):
    train_labels[i] = 3
for i in range(120, 150):
    train_labels[i] = 4
for i in range(150, 180):
    train_labels[i] = 5
