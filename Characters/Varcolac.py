'''
Created on Dec 10, 2015

@author: Lucian Apetre
'''
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.vector import Vector
from kivy.lang import Builder
import random


Builder.load_string("""
<Varcolac>:
    size: 30, 30
    canvas:
        Ellipse:
            pos: self.pos
            size: 30, 30
""")

class Varcolac(Widget):
    direction_x = 1
    direction_y = 0
    direction = direction_x, direction_y
    isMoving = True;

    def stopMovement(self, dt):
        self.isMoving = False;
    
    def move(self, dt):
        self.pos = Vector(*self.direction) + self.pos
        print self.pos
        return self.isMoving
    
    def directionUp(self):
        self.direction_x = 0
        self.direction_y = 1
        self.direction = self.direction_x, self.direction_y
        
    def directionDown(self):
        self.direction_x = 0
        self.direction_y = -1
        self.direction = self.direction_x, self.direction_y
        
    def directionLeft(self):
        self.direction_x = -1
        self.direction_y = 0
        self.direction = self.direction_x, self.direction_y
        
    def directionRight(self):
        self.direction_x = 1
        self.direction_y = 0
        self.direction = self.direction_x, self.direction_y