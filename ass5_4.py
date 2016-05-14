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

    if R < 5 and R >= 0:
        V = 50*R #km/s
    elif R >= 5:
        V = 250 #km/s

    return R0*(V / R - V0 / R0)*math.sin(l)

def main2():
    l = math.pi/2
    x = np.linspace(0,20,100)
    y = [vel(r, l) for r in x]
    

    n, bins, patches = plt.hist(y, 30)

    print bins

    plt.show()

def main():
    # generate a list for each l:
    listoflistsr = []
    listoflistsvel = []
    listoflistsl = []
    listofls = np.linspace(1,math.pi/2,1000).flatten().tolist()
    for l in listofls:
        r_list = np.linspace(0,20,1000).flatten().tolist()
        mylist = [vel(r,l) for r in r_list]
        listoflistsl.append(listofls)
        listoflistsvel.append(mylist)
        listoflistsr.append(r_list)


    flat_ls   = [j for i in listoflistsl for j in i]
    flat_vels = [j for i in listoflistsvel for j in i]
    flat_rs = [j for i in listoflistsr for j in i]

    #print flat_vels

    plt.hist2d(flat_ls, flat_vels, 100)
    plt.show()

main()

