# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 02:09:46 2021

@author: austi
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec    
from octtreeimplement import Point3d,OctNode, OctTree

DPI=72

#define the domain
length,width,height = 800,600,600

N=32
xs= np.random.rand(N)*length
ys= np.random.rand(N)*width
zs= np.random.rand(N)*height
points= [Point3d(xs[i],ys[i],zs[i]) for i in range(N)] #we have 500 points

domain = OctNode(Point3d(length/2,width/2,height/2),length/2,width/2,height/2) #domain is the rectangle, center,w,h
otree = OctTree(domain)

for point in points: #insert each of the points
    otree.insert(point)
    
print('Total points inserted:',  len(otree))
#draw the rectangles
fig = plt.figure(figsize=plt.figaspect(0.5))
# fig= plt.figure(figsize=(700/DPI, 500/DPI), dpi=DPI)
ax = fig.add_subplot(1, 2, 1, projection='3d')
# ax=plt.subplot()
ax.set_xlim(0,length)    
ax.set_ylim(0,width)  
ax.set_zlim(0,height)  
otree.draw(ax)
 # draw points

ax.scatter([p.x for p in points], [p.y for p in points],[p.z for p in points],s=4)   
ax.set_xticks([]) 
ax.set_yticks([]) 
ax.set_zticks([]) 



ax.invert_yaxis() #as we define in 4th quad
plt.tight_layout()
#plt.savefig('search-quadtree.png',DPI=72)
plt.show