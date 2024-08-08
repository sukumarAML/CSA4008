from qutip import *
import numpy as np
import matplotlib.pyplot as plt

print(Qobj())

print(Qobj([[1],[2]]))

r = np.random.rand(4, 4)
print(Qobj(r))
print(basis(5,3))
print(coherent(5,0.5-0.5j))
