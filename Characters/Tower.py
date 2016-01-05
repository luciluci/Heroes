'''
Created on Jan 5, 2016

@author: P3700562
'''

from kivy.graphics import Ellipse, Color
from kivy.uix.widget import Widget

class Tower(Widget):
    
    def __init__(self, touch):
        super(Tower, self).__init__()
        
        with self.canvas:
            Color(1., 0, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            Color(1, 1, 1)