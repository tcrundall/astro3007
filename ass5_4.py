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

def main3():
    longitude_array = np.zeros((DATA_DIM,DATA_DIM))
    velocity_array = np.zeros((DATA_DIM,DATA_DIM))

    longitude_vals = np.linspace(0, math.pi/2, DATA_DIM)
    r_vals = np.linspace(0, 20, DATA_DIM) # change r_max to higher when working
    
    duplicates_long = []
    duplicates_vels = []

    for i in range(DATA_DIM):
        for j in range(DATA_DIM):
            longitude_array[i,j] = longitude_vals[j]
            velocity_array[i,j], bright = vel3(r_vals[i], longitude_vals[j])
            if bright:
                duplicates_long.append(longitude_vals[j])
                vel, dummy = vel3(r_vals[i], longitude_vals[j])
                duplicates_vels.append(vel)
                 
    #print longitude_array.flatten().tolist().append(duplicates_long)
    print
    #print velocity_array

    plt.hist2d(longitude_array.flatten().tolist() + duplicates_long,
            velocity_array.flatten().tolist() + duplicates_vels,
            200, cmin=1)

    #plt.colorbar()
    plt.savefig("4d.png")


def main2():
    longitude_array = np.zeros((DATA_DIM,DATA_DIM))
    velocity_array = np.zeros((DATA_DIM,DATA_DIM))

    longitude_vals = np.linspace(0, math.pi/2, DATA_DIM)
    r_vals = np.linspace(0, 30, DATA_DIM) # change r_max to higher when working
    
    duplicates_long = []
    duplicates_vels = []

    for i in range(DATA_DIM):
        for j in range(DATA_DIM):
            longitude_array[i,j] = longitude_vals[j]
            velocity_array[i,j], bright = vel2(r_vals[i], longitude_vals[j])
            if bright:
                duplicates_long.append(longitude_vals[j])
                vel, dummy = vel2(r_vals[i], longitude_vals[j])
                duplicates_vels.append(vel)
                 
    #print longitude_array.flatten().tolist().append(duplicates_long)
    print
    #print velocity_array

    plt.hist2d(longitude_array.flatten().tolist() + duplicates_long,
            velocity_array.flatten().tolist() + duplicates_vels,
            200, cmin=1)

    #plt.colorbar()
    plt.savefig("4c.png")


def main():
    longitude_array = np.zeros((DATA_DIM,DATA_DIM))
    velocity_array = np.zeros((DATA_DIM,DATA_DIM))

    longitude_vals = np.linspace(0, math.pi/2, DATA_DIM)
    r_vals = np.linspace(0, 30, DATA_DIM) # change r_max to higher when working
    
    for i in range(DATA_DIM):
        for j in range(DATA_DIM):
            longitude_array[i,j] = longitude_vals[j]
            velocity_array[i,j] = vel(r_vals[i], longitude_vals[j])
    
    #print longitude_array
    #print
    #print velocity_array

    plt.hist2d(longitude_array.flatten().tolist(),
            velocity_array.flatten().tolist(), 200, cmin=1,
            cmap = plt.get_cmap('gray'))

    plt.savefig("4b.png")


DATA_DIM = 500 
main4()
#main2()
#main3()
