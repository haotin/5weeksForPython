# -*- coding: utf-8 -*-
#616566709@qq.com _author_haotin
#2016-01-26

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import sqlalchemy as sa
import tushare as ts
from math import sqrt
pd.set_option('display.width', 350)



# New figure with white background
fig = plt.figure(figsize=(6,6), facecolor='white')

# New axis over the whole figure, no frame and a 1:1 aspect ratio
ax = fig.add_axes([0,0,1,1], frameon=False, aspect=1)

# Number of ring
n = 50
size_min = 50
size_max = 50*50

# Ring position
P = np.random.uniform(0,1,(n,2))

# Ring colors
C = np.ones((n,4)) * (0,0,0,1)
# Alpha color channel goes from 0 (transparent) to 1 (opaque)
C[:,3] = np.linspace(0,1,n)

# Ring sizes
S = np.linspace(size_min, size_max, n)

# Scatter plot
scat = ax.scatter(P[:,0], P[:,1], s=S, lw = 0.5,
                  edgecolors = C, facecolors='None')

# Ensure limits are [0,1] and remove ticks
ax.set_xlim(0,1), ax.set_xticks([])
ax.set_ylim(0,1), ax.set_yticks([])

def update(frame):
    global P, C, S

    # Every ring is made more transparent
    C[:,3] = np.maximum(0, C[:,3] - 1.0/n)

    # Each ring is made larger
    S += (size_max - size_min) / n

    # Reset ring specific ring (relative to frame number)
    i = frame % 50
    P[i] = np.random.uniform(0,1,2)
    S[i] = size_min
    C[i,3] = 1

    # Update scatter object
    scat.set_edgecolors(C)
    scat.set_sizes(S)
    scat.set_offsets(P)

    # Return the modified object
    return scat,
animation = animation .FuncAnimation(fig, update, interval=10, blit=True, frames=200)
# animation.save('rain.gif', writer='imagemagick', fps=30, dpi=40)
plt.show()
# =======================================================================================
# import urllib
# from mpl_toolkits.basemap import Basemap
#
# # -> http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php
# feed = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"
#
# # Significant earthquakes in the last 30 days
# # url = urllib.request.urlopen(feed + "significant_month.csv")
#
# # Magnitude > 4.5
# url = urllib.request.urlopen(feed + "4.5_month.csv")
#
# # Magnitude > 2.5
# # url = urllib.request.urlopen(feed + "2.5_month.csv")
#
# # Magnitude > 1.0
# # url = urllib.request.urlopen(feed + "1.0_month.csv")
#
# # Reading and storage of data
# data = url.read()
# data = data.split(b'\n')[+1:-1]
# E = np.zeros(len(data), dtype=[('position',  float, 2),
#                                ('magnitude', float, 1)])
#
# for i in range(len(data)):
#     row = data[i].split(',')
#     E['position'][i] = float(row[2]),float(row[1])
#     E['magnitude'][i] = float(row[4])
#
# fig = plt.figure(figsize=(14,10))
# ax = plt.subplot(1,1,1)
#
# earth = Basemap(projection='mill')
# # Next, we request to draw coastline and fill continents:
#
# earth.drawcoastlines(color='0.50', linewidth=0.25)
# earth.fillcontinents(color='0.95')
#
# P = np.zeros(50, dtype=[('position', float, 2),
#                          ('size',     float, 1),
#                          ('growth',   float, 1),
#                          ('color',    float, 4)])
# scat = ax.scatter(P['position'][:,0], P['position'][:,1], P['size'], lw=0.5,
#                   edgecolors = P['color'], facecolors='None', zorder=10)
#
# def update(frame):
#     current = frame % len(E)
#     i = frame % len(P)
#
#     P['color'][:,3] = np.maximum(0, P['color'][:,3] - 1.0/len(P))
#     P['size'] += P['growth']
#
#     magnitude = E['magnitude'][current]
#     P['position'][i] = earth(*E['position'][current])
#     P['size'][i] = 5
#     P['growth'][i]= np.exp(magnitude) * 0.1
#
#     if magnitude < 6:
#         P['color'][i]    = 0,0,1,1
#     else:
#         P['color'][i]    = 1,0,0,1
#     scat.set_edgecolors(P['color'])
#     scat.set_facecolors(P['color']*(1,1,1,0.25))
#     scat.set_sizes(P['size'])
#     scat.set_offsets(P['position'])
#     return scat,
#
#
# animation = animation.FuncAnimation(fig, update, interval=10)
# plt.show()
#=============================================================
# Scatter Plots
import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

plt.scatter(X,Y)
plt.show()

# ==========================================================
# Bar Plots


import numpy as np
import matplotlib.pyplot as plt

n = 12
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x,y in zip(X,Y1):
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

plt.ylim(-1.25,+1.25)
plt.show()

# =========================================================

# Contour Plots
import numpy as np
import matplotlib.pyplot as plt

def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap='jet')
C = plt.contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)
plt.show()


# =========================================================

# Multi Plots
import numpy as np
import matplotlib.pyplot as plt

plt.subplot(2,2,1)
plt.subplot(2,2,3)
plt.subplot(2,2,4)

plt.show()

# =========================================================

# 3D Plots
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')

plt.show()