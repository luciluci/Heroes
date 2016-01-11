'''
Created on Jan 5, 2016

@author: P3700562
'''

from kivy.graphics import Ellipse, Color
from kivy.uix.widget import Widget
from Globals.Types import Point

class Tower(Widget):
    
    size_x = 30
    size_y = 30
    
    def __init__(self, touch, screenGrid):
        super(Tower, self).__init__()
        
        with self.canvas:
            Color(1., 0, 0)
            Ellipse(pos=(touch.x - self.size_x / 2, touch.y - self.size_y / 2), size=(self.size_x, self.size_y))
            Color(1, 1, 1)
        
        screenGrid.fillArea(Point(touch.x - self.size_x / 2, touch.y - self.size_y / 2), Point(touch.x + self.size_x / 2, touch.y + self.size_y / 2))