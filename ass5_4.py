import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pylab as pl

# Constants:
R0 = 10 #kpc # distance from sun to galactic centre in parsecs (approx)
V0 = 250

def vel(r, l):
    R = math.sqrt(r**2 + R0**2 - 2*r*R0*math.cos(l)) #kpc
    #print "For r: " + str(r) + " and angle: " + str(l) + \
    #       " R is: " + str(R)

    if R < 5 and R > 0:
        V = 50*R #km/s
    elif R >= 5:
        V = 250 #km/s

    return R0*(V / R - V0 / R0)*math.sin(l)

def main():
    l = math.pi/2
    x = np.linspace(0,20,100)
    y = [vel(r, l) for r in x]
    

    n, bins, patches = plt.hist(y, 30)

    print bins

    plt.show()

main()

