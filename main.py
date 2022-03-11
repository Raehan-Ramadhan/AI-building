#import numpy as np
#network_shape = (5,3,4,1)
#weights = [np.zeros((a,b)) for a,b in zip(network_shape[1:], network_shape[:-1])]
#biases = [np.zeros((a,1)) for a in network_shape[1:]]

import numpy as np

network_shape = (5,3,4,1)
weights = [np.random.rand(a,b) for a,b in zip(network_shape[1:], network_shape[:-1])]
a = np.array([5,3,2,5,6])

print(weights[0], '\n')

weights = [np.random.rand(b,a) for a,b in zip(network_shape[1:], network_shape[:-1])]

print(weights[0], '\n')
print(weights[0])
print(a, type(a), '\n')

