import math
import matplotlib.pyplot as plt
import numpy as np

omega = 10
#NH = 5e19

def tau(v):
    Ts = 150
    return 5.49*10e-19*NH/(Ts*math.sqrt(2*math.pi*omega)) \
                *math.exp(-v**2/(2*omega**2))
vs = np.linspace(-100, 100, 100)

NHs = np.linspace(5e19, 5e20, 10)

for NH in NHs:

    ys = [tau(v) for v in vs]

    plt.plot(vs, ys)
plt.show()
