import math
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pylab as pl
import matplotlib.cm as cm

# Constants:
R0 = 10 #kpc # distance from sun to galactic centre in parsecs (approx)
V0 = 250

def vel4(r, l, R):
    #print "For r: " + str(r) + " and angle: " + str(l) + \
    #       " R is: " + str(R)

    if R < 5 and R >= 0:
        V = 50*R #km/s
    elif R >= 5:
        V = 250 #km/s

    return R0*(V / R - V0 / R0)*math.sin(l)

def partB():
    ls = np.linspace(0.001, math.pi/2, DATA_DIM)
    rs = np.linspace(0.001, 25, DATA_DIM)
    
    l_list = []
    vel_list = []

    for i in range(len(ls)):
        for j in range(len(rs)):
            R = math.sqrt(rs[j]**2 + 10**2 - 2 * 10 * rs[j] * math.cos(ls[i]))
            if (R < 15):
                l_list.append(ls[i])
                vel_list.append(vel4(rs[j], ls[i], R))

    plt.hist2d(l_list, vel_list, PLOT_DIM, cmin=1)
    plt.savefig("partb.png")
            
def partC():
    ls = np.linspace(0.001, math.pi/2, DATA_DIM)
    rs = np.linspace(0.001, 25, DATA_DIM)
    
    l_list = []
    vel_list = []

    for i in range(len(ls)):
        for j in range(len(rs)):
            R = math.sqrt(rs[j]**2 + 10**2 - 2 * 10 * rs[j] * math.cos(ls[i]))
            if (R < 15):
                l_list.append(ls[i])
                vel_list.append(vel4(rs[j], ls[i], R))
                if (R > 4 and R < 6):
                    l_list.append(ls[i])
                    vel_list.append(vel4(rs[j], ls[i], R))

    plt.hist2d(l_list, vel_list, PLOT_DIM, cmin=1)
    plt.savefig("partc.png")

def partD():
    ls = np.linspace(-math.pi/2, math.pi/2, DATA_DIM*2)
    rs = np.linspace(0.001, 25, DATA_DIM)
    
    l_list = []
    vel_list = []

    for i in range(len(ls)):
        for j in range(len(rs)):
            R = math.sqrt(rs[j]**2 + 10**2 - 2 * 10 * rs[j] * math.cos(ls[i]))
            if (R < 15):
                if (R > 4 and R < 6):
                    vel_add = 50*math.cos( math.asin( 10*(math.sin(abs(ls[i]))/R )) )
                    #vel_add = 0 #subbing out radial expansion
                    vel = vel4(rs[j], ls[i], R) - vel_add*(ls[i]/abs(ls[i]))
                    l_list.append(ls[i])
                    l_list.append(ls[i])
                    vel_list.append(vel)
                    vel_list.append(vel)
                else:
                    l_list.append(ls[i])
                    vel_list.append(vel4(rs[j], ls[i], R))

    plt.hist2d(l_list, vel_list, PLOT_DIM, cmin=1)
    plt.savefig("partd.png")
 
DATA_DIM = 500
PLOT_DIM = 300
#partB()
#partC()
partD()
