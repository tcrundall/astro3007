# -*- coding: utf-8 -*-
"""
Created on Sun May  1 23:05:24 2016

@author: Tim
"""
import matplotlib.pyplot as plt
import math

def planckEquation(wl, temp):
    h = 6.626e-34 #[Js]
    c = 2.998e8 #[m/s]
    kB = 1.30e-23 #[J/K] 
    
    #turning wl from [angstroms] to [m]
    wl = wl*1e-10
    return (2*h*c*c)/(math.pow(wl,5)) * 1/( math.exp((h*c)/(wl*kB*temp)) - 1)



    
    

# reading in file and producing plot
lines = [line.rstrip('\n').split('\t') for line in open('star_spec.dat.txt')]

xs = []
ys = []

for line in lines:
    xs.append(float(line[0]))
    ys.append(float(line[1]))
    
pEs = []

for i in range(len(xs)):
    pEs.append(planckEquation(xs[i], 1000))



plt.plot(xs, pEs)    
plt.plot(xs, ys)

plt.xlabel('wavelength')
plt.ylabel('intensity')
plt.title('Spectrum of a star')
plt.grid(True)
plt.savefig("ass.png")
plt.show()