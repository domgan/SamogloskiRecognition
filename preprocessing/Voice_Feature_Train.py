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

aaa4 = melspec_from_mat('data/aaa4.mat')
eee4 = melspec_from_mat('data/eee4.mat')
iii4 = melspec_from_mat('data/iii4.mat')
ooo4 = melspec_from_mat('data/ooo4.mat')
uuu4 = melspec_from_mat('data/uuu4.mat')
yyy4 = melspec_from_mat('data/yyy4.mat')

n = melspec_from_mat('data/n.mat')
n1 = melspec_from_mat('data/n1.mat')
n2 = melspec_from_mat('data/n2.mat')
n3 = melspec_from_mat('data/n3.mat')
n4 = melspec_from_mat('data/n4.mat')

train_input = np.concatenate((aaa, aaa1, aaa2, aaa4,
                              eee, eee1, eee2, eee4,
                              iii, iii1, iii2, iii4,
                              ooo, ooo1, ooo2, ooo4,
                              uuu, uuu1, uuu2, uuu4,
                              yyy, yyy1, yyy2, yyy4,
                              n, n1, n2, n3, n4))
train_input = np.expand_dims(train_input, 3)

ts = np.ones((30*6*4, 1))
tn = np.zeros((60*5, 1))
train_labels = np.concatenate((ts, tn))
