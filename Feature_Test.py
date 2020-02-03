import numpy as np
from Feature_Train import mfcc_from_mat

fs = 8000

aaa = mfcc_from_mat('data/taaa.mat', fs)
eee = mfcc_from_mat('data/teee.mat', fs)
iii = mfcc_from_mat('data/tiii.mat', fs)
ooo = mfcc_from_mat('data/tooo.mat', fs)
uuu = mfcc_from_mat('data/tuuu.mat', fs)
yyy = mfcc_from_mat('data/tyyy.mat', fs)

test_input = np.concatenate((aaa, eee, iii, ooo, uuu, yyy))
test_input = np.expand_dims(test_input, 3)

ta = np.zeros((8, 6))
ta[:, 0] = 1
te = np.zeros((8, 6))
te[:, 1] = 1
ti = np.zeros((8, 6))
ti[:, 2] = 1
to = np.zeros((8, 6))
to[:, 3] = 1
tu = np.zeros((8, 6))
tu[:, 4] = 1
ty = np.zeros((8, 6))
ty[:, 5] = 1
test_labels = np.concatenate((ta, te, ti, to, tu, ty))