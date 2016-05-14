
from pylab import *
import numpy as np

x = np.random.randn(3000) - 1
y = np.random.randn(3000)*2 + 1

hist, xedges, yedges = np.histogram2d(x,y,bins=40,range=[[-6,4],[-4,6]])
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
imshow(hist.T, extent=extent, interpolation = 'nearest', origin='lower')
colorbar()
show()
