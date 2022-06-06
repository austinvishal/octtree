# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 00:14:09 2021

@author: austinvishal
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math

class Point3d:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

class OctNode:
    #here octnode is represented as cube, it can be in any shape in general. in tree terminology the cell/cube is node
    def __init__(self, center, length, width, height): #center is point3d class, length,width, height all are half size
        self.center=center
        self.length=length
        self.width=width
        self.height=height
        self.west=center.x-length
        self.east=center.x + length
        self.north = center.y-width
        self.south = center.y + width
        self.top = center.z - height
        self.bottom= center.z + height
    
    def containsPoint(self,point):
        return (self.west <=point.x < self.east and self.north <=point.y < self.south and self.top <= point.z <self.bottom) #the two edges west and north has equality 
    # because if the point lies on the edge on west/north or the other two sides means other rectangle
    
    #visualize or draw cube outer one
    def draw(self, ax,c='k', lw=1.5, **kwargs):  #linewidth lw ax axis c=color
        x1,y1,z1 =self.west, self.north,self.bottom
        x2,y2,z2=self.east, self.south,self.top
        ax.plot3D([x1,x2,x2,x1,x1],[y1,y1,y2,y2,y1],[z1,z1,z1,z1,z1],c=c, lw=lw,**kwargs)
        ax.plot3D([x1,x2,x2,x1,x1],[y1,y1,y2,y2,y1],[z2,z2,z2,z2,z2],c=c, lw=lw,**kwargs)
        ax.plot3D([x1,x2,x2,x1,x1],[y1,y1,y1,y1,y1],[z1,z1,z2,z2,z1],c=c, lw=lw,**kwargs)
        ax.plot3D([x2,x2,x2,x2,x2],[y1,y2,y2,y1,y1],[z1,z1,z2,z2,z1],c=c, lw=lw,**kwargs)
        
class OctTree:
    #octtree is a octnode/cube here plus a capacity #boundary is a cube
    def __init__(self,boundary,capacity=8):
        self.boundary= boundary
        self.capacity= capacity
        self.points=[] # list to store the points
        self.divided=False
        
    def insert(self,point):
        """
        
       
        Parameters
        ----------
        point : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.
            
        """
        #if the point is in the range of current octtree if not return it
        if not self.boundary.containsPoint(point):
            return False
        if len(self.points) < self.capacity: #another check if quadtree has reached its limit
            self.points.append(point)
            return True  #to know if its inserted into the subtree or not
        #now we reached the capacity of current tree, so we divide/ split. but before we split we need to check if it 
        #is already been split as we can't divided again
        if not self.divided:
                self.divide() #after division set flag to true
                #self.divided= True   #added it inside divide function for encapsulating all divide based things
        #once octtree is divided into 8 subtrees we then insert points
        if self.oct1.insert(point): #here oct1 is a octtree and point is being inserted, recursion
            return True
        elif self.oct2.insert(point):
            return True
        elif self.oct3.insert(point):
            return True
        elif self.oct4.insert(point):
            return True
        elif self.oct5.insert(point): 
            return True
        elif self.oct6.insert(point):
            return True
        elif self.oct7.insert(point):
            return True
        elif self.oct8.insert(point):
            return True
        
        return False #this point might not be reached as it will always insert into subtrees based on capacity
    
    def divide(self):
        center_x=self.boundary.center.x
        center_y=self.boundary.center.y
        center_z=self.boundary.center.z
        new_width=self.boundary.width/2
        new_length=self.boundary.length/2
        new_height=self.boundary.height/2
        #each of subtree initialize the rectangle first
        oct1=OctNode(Point3d(center_x- new_length,center_y-new_width,center_z-new_height),new_length,new_width,new_height) #you need to locate the centerpoint of inner rectangle which is current center - new width
        self.oct1 = OctTree(oct1) #northwest now has new quadtree, the arguments can hae different capacity, here default is 4 as initialized above in the constructor
        
        oct2=OctNode(Point3d(center_x- new_length,center_y-new_width,center_z+new_height),new_length,new_width,new_height) #you need to locate the centerpoint of inner rectangle which is current center - new width
        self.oct2 = OctTree(oct2)
        
        oct3=OctNode(Point3d(center_x- new_length,center_y+new_width,center_z-new_height),new_length,new_width,new_height) #you need to locate the centerpoint of inner rectangle which is current center - new width
        self.oct3 = OctTree(oct3)
        
        oct4=OctNode(Point3d(center_x- new_length,center_y+new_width,center_z+new_height),new_length,new_width,new_height) #you need to locate the centerpoint of inner rectangle which is current center - new width
        self.oct4 = OctTree(oct4)
        
        oct5=OctNode(Point3d(center_x+ new_length,center_y-new_width,center_z-new_height),new_length,new_width,new_height) #you need to locate the centerpoint of inner rectangle which is current center - new width
        self.oct5 = OctTree(oct5) #northwest now has new quadtree, the arguments can hae different capacity, here default is 4 as initialized above in the constructor
        
        oct6=OctNode(Point3d(center_x+ new_length,center_y-new_width,center_z+new_height),new_length,new_width,new_height) #you need to locate the centerpoint of inner rectangle which is current center - new width
        self.oct6 = OctTree(oct6)
        
        oct7=OctNode(Point3d(center_x+ new_length,center_y+new_width,center_z-new_height),new_length,new_width,new_height) #you need to locate the centerpoint of inner rectangle which is current center - new width
        self.oct7 = OctTree(oct7)
        
        oct8=OctNode(Point3d(center_x+ new_length,center_y+new_width,center_z+new_height),new_length,new_width,new_height) #you need to locate the centerpoint of inner rectangle which is current center - new width
        self.oct8 = OctTree(oct8)
        
        self.divided= True  #after division set flag
        
        #visualize octree using helper libraries
        #to calculate total number of points including the recursively divided octrees
    def __len__(self):  #function overriding, the length function
        count = len(self.points)
        if self.divided:
            count += len(self.oct1)+ len(self.oct2)+ len(self.oct3)+ len(self.oct4)+ len(self.oct5)+ len(self.oct6)+ len(self.oct7)+ len(self.oct8)
        #each call will also call its own length function to recursively calculate the total numberof points
        return count
    
    #recursively draw octtrees
    def draw(self,ax):
        self.boundary.draw(ax)
        
        if self.divided:
            self.oct1.draw(ax) #recursive call
            self.oct2.draw(ax)
            self.oct3.draw(ax)
            self.oct4.draw(ax)
            self.oct5.draw(ax)
            self.oct6.draw(ax)
            self.oct7.draw(ax)
            self.oct8.draw(ax)