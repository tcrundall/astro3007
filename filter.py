# -*- coding: utf-8 -*-
"""
Created on Sun May  1 23:05:24 2016

@author: Tim
"""
import matplotlib.pyplot as plt
import math

# reading in file and storing columns into two lists
lines = [line.rstrip('\n').split('\t') for line in open('Filter_transmission.dat.txt')]
xs = []
y1s = []
y2s = []
for line in lines:
    xs.append(float(line[0]))
    y1s.append(float(line[1]))
    y2s.append(float(line[2]))
    
plt.plot(xs, y1s)
plt.plot(xs, y2s, 'r')

plt.xlabel('wavelength')
plt.ylabel('flux')
plt.title('Fliter Transmission')
plt.grid(True)
plt.savefig("ass.png")
plt.show()
