'''
Created on Jan 5, 2016

@author: P3700562
'''

from kivy.graphics import Ellipse, Color
from kivy.uix.widget import Widget
from Globals.Types import Point
#from kivy.lang import Builder
from kivy.properties import NumericProperty

'''Builder.load_string("""
<TowerShadow>:
    size: 30, 30
    canvas.before:
        Color:
            rgba: 1, 1, 0, 1 
    canvas:
        Ellipse:
            pos: self.pos
            size: 30, 30
""")'''

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
        
        
class TowerShadow(Widget):
    red = NumericProperty(0)
    size_max = (30,30)
    
    def __init__(self):
        super(TowerShadow, self).__init__()
        self.size_hint = (None, None)
        
        with self.canvas:
            Color(1., 0, 0)
            d=30.
            self.ellipse = Ellipse(pos=self.pos, size=self.size_max, size_hint=(None, None))
            Color(1, 1, 1)
        
        self.bind(red = self.updateTower, 
                  pos = self.updateTower)
        
    def changePosition(self, newX, newY):
        posX = newX - self.ellipse.size[0] / 2
        posY = newY - self.ellipse.size[1] / 2
        
        if self.pos != (posX, posY):
            self.pos = (posX, posY)
    
    def updateTower(self, *args):
        self.size_hint = (None, None)
        self.canvas.clear()
        self.size = (30, 30)
        with self.canvas:
            Color(self.red, 0, 0)
            d=30.
            self.ellipse = Ellipse(pos=self.pos, size=(30, 30), size_hint=(None, None))
         
    def changeRed(self, red):
        if self.red != red:
            self.red = red        