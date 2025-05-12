import numpy as np

def nonlin(x, deriv=False):
    if deriv == True:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

X = np.array([  [0,0,1],
[0,1,1],
[1,0,1],
[1,1,1] ])

y = np.array([[0,1,1,0]]).T

np.random.seed(1)

syn0 = 2 * np.random.random((3,4)) - 1 #weights from range -1 to 1
syn1 = 2 * np.random.random((4,1)) - 1


for iter in range(60000):
    l0 = X
    L1 = nonlin(np.dot(l0, syn0)) # 4 by 1 matrix
    l2 = nonlin(np.dot(L1, syn1)) 
    l2_error = y - l2 # loss matrix
    if (iter % 10000) == 0:
        print ("Error:" + str(np.mean(np.abs(l2_error))))
    l2_delta = l2_error * nonlin(l2,True)
    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(L1,True)
    syn1 += L1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)


    