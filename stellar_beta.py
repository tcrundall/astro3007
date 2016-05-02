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

def getMeanSquareDif(pEs, ys, startOfRed):
    total = 0
    for i in range(startOfRed, len(pEs)):
        total = total + (pEs[i] - ys[i])*(pEs[i] - ys[i])

    return total

def generatePlankCurve(temp, xs, startOfRed):
    pEs = []
    for i in range(len(xs)):
        pEs.append(planckEquation(xs[i], temp))

    #normalising values
    pEs_normalising_factor = pEs[startOfRed]

    for i in range(len(xs)):
        pEs[i] = pEs[i]/pEs_normalising_factor

    return pEs

# reading in file and producing plot
lines = [line.rstrip('\n').split('\t') for line in open('star_spec.dat.txt')]

xs = []
ys = []


for line in lines:
    xs.append(float(line[0]))
    ys.append(float(line[1]))
    
#get index of 4500 A
for i in range(len(xs)):
    if xs[i] > 4500:
        startOfRed = i
        break

ys_normal =  ys[startOfRed]

#normalising y values:
for i in range(len(xs)):
    ys[i] = ys[i]/ys_normal

pEs = generatePlankCurve(11000, xs, startOfRed)
print getMeanSquareDif(pEs, ys, startOfRed)


plt.plot(xs, pEs)    
plt.plot(xs, ys)

plt.xlabel('wavelength')
plt.ylabel('intensity')
plt.title('Spectrum of a star')
plt.grid(True)
plt.savefig("ass.png")
plt.show()
