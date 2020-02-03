import numpy as np
from Feature_Train_old import mfcc_from_mat

fs = 8000

aaa = mfcc_from_mat('data/taaa.mat', fs)
eee = mfcc_from_mat('data/teee.mat', fs)
iii = mfcc_from_mat('data/tiii.mat', fs)
ooo = mfcc_from_mat('data/tooo.mat', fs)
uuu = mfcc_from_mat('data/tuuu.mat', fs)
yyy = mfcc_from_mat('data/tyyy.mat', fs)

test_input = np.concatenate((aaa, eee, iii, ooo, uuu, yyy))


test_labels = np.zeros(48)
for i in range(8, 16):
    test_labels[i] = 1
for i in range(16, 24):
    test_labels[i] = 2
for i in range(24, 32):
    test_labels[i] = 3
for i in range(32, 40):
    test_labels[i] = 4
for i in range(40, 48):
    test_labels[i] = 5
