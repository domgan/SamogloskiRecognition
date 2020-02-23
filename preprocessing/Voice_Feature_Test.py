import numpy as np
from preprocessing.Voice_Feature_Train import melspec_from_mat

fs = 8000

aaa = melspec_from_mat('data/test/taaa.mat')
eee = melspec_from_mat('data/test/teee.mat')
iii = melspec_from_mat('data/test/tiii.mat')
ooo = melspec_from_mat('data/test/tooo.mat')
uuu = melspec_from_mat('data/test/tuuu.mat')
yyy = melspec_from_mat('data/test/tyyy.mat')

aaa1 = melspec_from_mat('data/test/taaa1.mat')
eee1 = melspec_from_mat('data/test/teee1.mat')
iii1 = melspec_from_mat('data/test/tiii1.mat')
ooo1 = melspec_from_mat('data/test/tooo1.mat')
uuu1 = melspec_from_mat('data/test/tuuu1.mat')
yyy1 = melspec_from_mat('data/test/tyyy1.mat')

n = melspec_from_mat('data/test/tn.mat')
n1 = melspec_from_mat('data/test/tn1.mat')
n2 = melspec_from_mat('data/test/tn2.mat')
n3 = melspec_from_mat('data/test/tn3.mat')


test_input = np.concatenate((aaa, aaa1,
                            eee, eee1,
                            iii, iii1,
                            ooo, ooo1,
                            uuu, uuu1,
                            yyy, yyy1,
                            n, n1, n2, n3))
test_input = np.expand_dims(test_input, 3)

ts = np.ones((8*6*2, 1))
tn = np.zeros((16*4, 1))
test_labels = np.concatenate((ts, tn))
