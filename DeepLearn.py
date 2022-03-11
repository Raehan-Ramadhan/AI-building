import numpy as np

#network_shape = (5,3,4,1)
#weights = [np.zeros((a,b)) for a,b in zip(network_shape[1:], network_shape[:-1])]
#biases = [np.zeros((a,1)) for a in network_shape[1:]]

inp = np.arange(1, 6)

res = []
for i in range(3):
    res.append(np.arange(5*i, 5*(i+1)))

res = np.array(res)
nres = np.array([a*3 for a in res])
sres = np.subtract(nres, res)
sres2 = nres - res