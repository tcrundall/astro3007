import math
import matplotlib.pyplot as plt
import numpy as np

omega = 10
#NH = 5e19

def tau(v):
    Ts = 150
    return 5.49*10e-19*NH/(Ts*math.sqrt(2*math.pi*omega)) \
                *math.exp(-v**2/(2*omega**2))

def Tb(v):
    Ts = 150
    return Ts*(1 - math.exp(-tau(v)))

def gaus(x):
    norm = 1/(omega_prime*math.sqrt(2*math.pi))

    return norm*math.exp(-x**2/(2*omega_prime**2))

vs = np.linspace(-5* omega,5* omega, 500)

NHs = np.linspace(5e19, 5e20, 10)

for NH in NHs:

    ys = [Tb(v) for v in vs]
    peak = max(ys)

    i = 0
    while (ys[i] < 0.5*peak):
        i += 1
    FWHM = -2*vs[i]

    omega_prime = FWHM/2.355

    zs = [gaus(x) for x in vs]
    gaus_peak = max(zs)
    #print gaus_peak

    zs = [z*peak/gaus_peak for z in zs]

    difference = 0
    total = 0
    for i in range(len(vs)):
        difference = difference + abs(zs[i] - ys[i])
        total = total + (ys[i])

    print difference/total * 100
    


    plt.plot(vs, ys)
    plt.plot(vs, zs, '--')

    

plt.savefig("q3.png")
