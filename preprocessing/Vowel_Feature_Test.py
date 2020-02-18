import numpy as np
from preprocessing.Vowel_Feature_Train import mfcc_from_mat

fs = 8000

aaa = mfcc_from_mat('data/taaa.mat', fs)
eee = mfcc_from_mat('data/teee.mat', fs)
iii = mfcc_from_mat('data/tiii.mat', fs)
ooo = mfcc_from_mat('data/tooo.mat', fs)
uuu = mfcc_from_mat('data/tuuu.mat', fs)
yyy = mfcc_from_mat('data/tyyy.mat', fs)

aaa1 = mfcc_from_mat('data/taaa1.mat', fs)
eee1 = mfcc_from_mat('data/teee1.mat', fs)
iii1 = mfcc_from_mat('data/tiii1.mat', fs)
ooo1 = mfcc_from_mat('data/tooo1.mat', fs)
uuu1 = mfcc_from_mat('data/tuuu1.mat', fs)
yyy1 = mfcc_from_mat('data/tyyy1.mat', fs)

test_input = np.concatenate((aaa, aaa1,
                             eee, eee1,
                             iii, iii1,
                             ooo, ooo1,
                             uuu, uuu1,
                             yyy, yyy1))
test_input = np.expand_dims(test_input, 3)

ta = np.zeros((16, 6))
ta[:, 0] = 1
te = np.zeros((16, 6))
te[:, 1] = 1
ti = np.zeros((16, 6))
ti[:, 2] = 1
to = np.zeros((16, 6))
to[:, 3] = 1
tu = np.zeros((16, 6))
tu[:, 4] = 1
ty = np.zeros((16, 6))
ty[:, 5] = 1
test_labels = np.concatenate((ta, te, ti, to, tu, ty))
