# -*- coding: utf-8 -*-
"""
Created on Sun May  1 23:05:24 2016

@author: Tim
"""
import matplotlib.pyplot as plt
import math

# reading in file and storing columns into two lists
lines = [line.rstrip('\n').split() \
        for line in open('Values.xls')]

xs = []
ys = []
mean_background = 5581.817
for i, line in enumerate(lines):
    if i != 0:
        xs.append(float(line[0]))
        ys.append(float(line[1]) - mean_background)
    

plt.plot(xs, ys)

plt.xlabel('Radial distance')
plt.ylabel('Normalised Integrated Intensity')
plt.title('Radial Profile Plot')
plt.grid(True)
plt.savefig("radial_profile_plot.png")
plt.show()
