import numpy as np
import librosa
import scipy.io


def mfcc_from_mat(path, fs=8000):
    mat = scipy.io.loadmat(path)
    mat = mat['y']
    mat = mat[4000:8000, :]  # shorten to 1 seconds
    arr = []
    for i in range(mat.shape[1]):
        m = librosa.feature.mfcc(mat[:, i], fs)
        arr.append(m)
    return np.array(arr)


aaa = mfcc_from_mat('data/aaa.mat')
eee = mfcc_from_mat('data/eee.mat')
iii = mfcc_from_mat('data/iii.mat')
ooo = mfcc_from_mat('data/ooo.mat')
uuu = mfcc_from_mat('data/uuu.mat')
yyy = mfcc_from_mat('data/yyy.mat')

aaa1 = mfcc_from_mat('data/aaa1.mat')
eee1 = mfcc_from_mat('data/eee1.mat')
iii1 = mfcc_from_mat('data/iii1.mat')
ooo1 = mfcc_from_mat('data/ooo1.mat')
uuu1 = mfcc_from_mat('data/uuu1.mat')
yyy1 = mfcc_from_mat('data/yyy1.mat')

aaa2 = mfcc_from_mat('data/aaa2.mat')
eee2 = mfcc_from_mat('data/eee2.mat')
iii2 = mfcc_from_mat('data/iii2.mat')
ooo2 = mfcc_from_mat('data/ooo2.mat')
uuu2 = mfcc_from_mat('data/uuu2.mat')
yyy2 = mfcc_from_mat('data/yyy2.mat')

train_input = np.concatenate((aaa, aaa1, aaa2,
                              eee, eee1, eee2,
                              iii, iii1, iii2,
                              ooo, ooo1, ooo2,
                              uuu, uuu1, uuu2,
                              yyy, yyy1, yyy2))
train_input = np.expand_dims(train_input, 3)

ta = np.zeros((90, 6))
ta[:, 0] = 1
te = np.zeros((90, 6))
te[:, 1] = 1
ti = np.zeros((90, 6))
ti[:, 2] = 1
to = np.zeros((90, 6))
to[:, 3] = 1
tu = np.zeros((90, 6))
tu[:, 4] = 1
ty = np.zeros((90, 6))
ty[:, 5] = 1
train_labels = np.concatenate((ta, te, ti, to, tu, ty))
