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

    def create(self):
        posx = random.randint(100, 480)
        posy = random.randint(100, 480)
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(posx, posy), size=(d, d))
        print "create varcolac"
    
    def move(self, dt):
        self.pos = Vector(*self.direction) + self.pos
        print self.pos
        print "move varcolac"
        
    def on_touch_move(self, touch):
        print "on_touch_move"