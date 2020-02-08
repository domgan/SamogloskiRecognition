import numpy as np
import librosa
import scipy.io


def melspec_from_mat(path, fs=8000):
    mat = scipy.io.loadmat(path)
    mat = mat['y']
    mat = mat[0:8000, :]  # shorten to 1 seconds
    arr = []
    for i in range(mat.shape[1]):
        m = librosa.feature.melspectrogram(mat[:, i], fs)
        arr.append(m)
    return np.array(arr)


aaa = melspec_from_mat('data/aaa.mat')
eee = melspec_from_mat('data/eee.mat')
iii = melspec_from_mat('data/iii.mat')
ooo = melspec_from_mat('data/ooo.mat')
uuu = melspec_from_mat('data/uuu.mat')
yyy = melspec_from_mat('data/yyy.mat')

aaa1 = melspec_from_mat('data/aaa1.mat')
eee1 = melspec_from_mat('data/eee1.mat')
iii1 = melspec_from_mat('data/iii1.mat')
ooo1 = melspec_from_mat('data/ooo1.mat')
uuu1 = melspec_from_mat('data/uuu1.mat')
yyy1 = melspec_from_mat('data/yyy1.mat')

aaa2 = melspec_from_mat('data/aaa2.mat')
eee2 = melspec_from_mat('data/eee2.mat')
iii2 = melspec_from_mat('data/iii2.mat')
ooo2 = melspec_from_mat('data/ooo2.mat')
uuu2 = melspec_from_mat('data/uuu2.mat')
yyy2 = melspec_from_mat('data/yyy2.mat')

n = melspec_from_mat('data/n.mat')
n1 = melspec_from_mat('data/n1.mat')

train_input = np.concatenate((aaa, aaa1, aaa2,
                              eee, eee1, eee2,
                              iii, iii1, iii2,
                              ooo, ooo1, ooo2,
                              uuu, uuu1, uuu2,
                              yyy, yyy1, yyy2,
                              n, n1))
train_input = np.expand_dims(train_input, 3)

ts = np.zeros((30*6*3, 2))
ts[:, 0] = 1
tn = np.zeros((60*2, 2))
tn[:, 1] = 1
train_labels = np.concatenate((ts, tn))