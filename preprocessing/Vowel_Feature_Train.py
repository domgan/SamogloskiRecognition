import numpy as np
import librosa
import scipy.io


def mfcc_from_mat(path, fs=8000):
    mat = scipy.io.loadmat(path)
    mat = mat['y']
    mat = mat[1000:8000, :]  # shorten to 1 seconds
    arr = []
    for i in range(mat.shape[1]):
        m = librosa.feature.mfcc(mat[:, i], fs)
        arr.append(m)
    return np.array(arr)


aaa = mfcc_from_mat('data/train/aaa.mat')
eee = mfcc_from_mat('data/train/eee.mat')
iii = mfcc_from_mat('data/train/iii.mat')
ooo = mfcc_from_mat('data/train/ooo.mat')
uuu = mfcc_from_mat('data/train/uuu.mat')
yyy = mfcc_from_mat('data/train/yyy.mat')

aaa1 = mfcc_from_mat('data/train/aaa1.mat')
eee1 = mfcc_from_mat('data/train/eee1.mat')
iii1 = mfcc_from_mat('data/train/iii1.mat')
ooo1 = mfcc_from_mat('data/train/ooo1.mat')
uuu1 = mfcc_from_mat('data/train/uuu1.mat')
yyy1 = mfcc_from_mat('data/train/yyy1.mat')

aaa2 = mfcc_from_mat('data/train/aaa2.mat')
eee2 = mfcc_from_mat('data/train/eee2.mat')
iii2 = mfcc_from_mat('data/train/iii2.mat')
ooo2 = mfcc_from_mat('data/train/ooo2.mat')
uuu2 = mfcc_from_mat('data/train/uuu2.mat')
yyy2 = mfcc_from_mat('data/train/yyy2.mat')

aaa3 = mfcc_from_mat('data/train/aaa3.mat')
eee3 = mfcc_from_mat('data/train/eee3.mat')
iii3 = mfcc_from_mat('data/train/iii3.mat')
ooo3 = mfcc_from_mat('data/train/ooo3.mat')
uuu3 = mfcc_from_mat('data/train/uuu3.mat')
yyy3 = mfcc_from_mat('data/train/yyy3.mat')

aaa4 = mfcc_from_mat('data/train/aaa4.mat')
eee4 = mfcc_from_mat('data/train/eee4.mat')
iii4 = mfcc_from_mat('data/train/iii4.mat')
ooo4 = mfcc_from_mat('data/train/ooo4.mat')
uuu4 = mfcc_from_mat('data/train/uuu4.mat')
yyy4 = mfcc_from_mat('data/train/yyy4.mat')

train_input = np.concatenate((aaa, aaa1, aaa2, aaa3, aaa4,
                              eee, eee1, eee2, eee3, eee4,
                              iii, iii1, iii2, iii3, iii4,
                              ooo, ooo1, ooo2, ooo3, ooo4,
                              uuu, uuu1, uuu2, uuu3, uuu4,
                              yyy, yyy1, yyy2, yyy3, yyy4))
train_input = np.expand_dims(train_input, 3)

col = 5
ta = np.zeros((30 * col, 6))
ta[:, 0] = 1
te = np.zeros((30 * col, 6))
te[:, 1] = 1
ti = np.zeros((30 * col, 6))
ti[:, 2] = 1
to = np.zeros((30 * col, 6))
to[:, 3] = 1
tu = np.zeros((30 * col, 6))
tu[:, 4] = 1
ty = np.zeros((30 * col, 6))
ty[:, 5] = 1
train_labels = np.concatenate((ta, te, ti, to, tu, ty))
