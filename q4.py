import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pylab as pl
import matplotlib.cm as cm

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

def vel2(r, l):
    R = math.sqrt(r**2 + R0**2 - 2*r*R0*math.cos(l)) #kpc
    #print "For r: " + str(r) + " and angle: " + str(l) + \
    #       " R is: " + str(R)

    if R < 5 and R >= 0:
        V = 50*R #km/s
    elif R >= 5:
        V = 250 #km/s

    if R > 4 and R < 6:
        bright = True
    else:
        bright = False

    return R0*(V / R - V0 / R0)*math.sin(l), bright


def vel3(r, l):
    R = math.sqrt(r**2 + R0**2 - 2*r*R0*math.cos(l)) #kpc
    #print "For r: " + str(r) + " and angle: " + str(l) + \
    #       " R is: " + str(R)

    if R < 5 and R >= 0:
        V = 50*R #km/s
    elif R >= 5:
        V = 250 #km/s

    if R > 4 and R < 6:
        bright = True
        vel_rad = 50*math.cos( math.asin( math.sin(l)*R/R0 ) )
    else:
        vel_rad = 0
        bright = False

    return R0*(V / R - V0 / R0)*math.sin(l) - vel_rad, bright

def vel4(r, l, R):
    #print "For r: " + str(r) + " and angle: " + str(l) + \
    #       " R is: " + str(R)

    if R < 5 and R >= 0:
        V = 50*R #km/s
    elif R >= 5:
        V = 250 #km/s

    return R0*(V / R - V0 / R0)*math.sin(l)

def vel5(r, l, R):
    #print "For r: " + str(r) + " and angle: " + str(l) + \
    #       " R is: " + str(R)

    if R < 5 and R >= 0:
        V = 50*R #km/s
    elif R >= 5:
        V = 250 #km/s

    if R < 6 and R > 4:
        duplicate = True
    else:
        duplicate = False

    return R0*(V / R - V0 / R0)*math.sin(l), duplicate




def main4():
    xs = np.linspace(0.001,15,400)
    ys = np.linspace(0.001,25,800)

    l_list = []
    vel_list = []

    for i in range(len(xs)):
        for j in range(len(ys)):
            r = math.sqrt( ys[j]**2 + xs[i]**2 )
            l = math.atan( xs[i] / ys[j] )
            R = math.sqrt( (ys[j] - 10)**2 + xs[i]**2)
            if (R < 15):
                l_list.append(l)
                vel_list.append(vel4(r, l, R))

    plt.hist2d(l_list, vel_list, 50, cmin=1)
    plt.show()


def main():
    ls = np.linspace(0.001, math.pi/2, 400)
    rs = np.linspace(0.001, 25, 400)
    
    l_list = []
    vel_list = []

    for i in range(len(ls)):
        for j in range(len(rs)):
            R = math.sqrt(rs[j]**2 + 10**2 - 2 * 10 * rs[j] * math.cos(ls[i]))
            if (R < 15):
                l_list.append(ls[i])
                vel_list.append(vel4(rs[j], ls[i], R))

    plt.hist2d(l_list, vel_list, 50, cmin=1)
    plt.show()
            
main()
