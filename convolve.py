# -*- coding: utf-8 -*-
"""
Created on Sun May  1 23:05:24 2016

@author: Tim
"""
import matplotlib.pyplot as plt
import math


# reading in file and storing columns into two lists
lines = [line.rstrip('\n').split('\t') for line in open('star_spec.dat.txt')]
xs = []
ys = []
for line in lines:
    xs.append(float(line[0]))
    ys.append(float(line[1]))

lines = [line.rstrip('\n').split('\t') for line in open('Filter_transmission.dat.txt')]
xfs = []
y1s = []
y2s = []
for line in lines:
    xfs.append(float(line[0]))
    y1s.append(float(line[1]))
    y2s.append(float(line[2]))

print xfs[0]
print xs[0]

for i in range(len(xs)):
    y1s[i] = y1s[i]*ys[i]
    y2s[i] = y2s[i]*ys[i]

plt.plot(xs, y1s, 'b')
plt.plot(xs, y2s, 'r')

print "Total flux through blue: " + str(sum(y1s))
print "Total flux through red: " + str(sum(y2s))

plt.xlabel('wavelength')
plt.ylabel('intensity')
plt.title('Spectrum of a star')
plt.grid(True)
plt.savefig("ass.png")
plt.show()
