'''
Created on Jan 5, 2016

@author: Lucian Apetre
14.01.2016 Create TowerFactory
'''

from kivy.graphics import Ellipse, Color
from kivy.uix.widget import Widget
from Globals.Types import Point
from kivy.properties import NumericProperty

class TowerFactory(object):
    _instance = None
    _towers = []
    _maxTowers = 0
    _screenGreed = None
    
    def __init__(self, screenGrid):
        self._screenGreed = screenGrid
        super(TowerFactory, self).__init__()
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TowerFactory, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    
    def setMaxTowers(self, nr):
        self._maxTowers = nr
        for idx in range(0, nr):
            self._towers.append(Tower(self._screenGreed))

    def getTower(self):
        retVal = None
        if self._maxTowers > 0:
            self._maxTowers -= 1
            retVal = self._towers.pop()
        else:
            print "WARNING! no more towers"
        return retVal
    
    def releaseTower(self, tower):
        self._maxTowers += 1
        self._towers.append(tower)
        
    
class Tower(Widget):
    size_x = 30
    size_y = 30
    _screenGrid = None
    
    def __init__(self, screenGrid):
        super(Tower, self).__init__()
        
        self._screenGrid = screenGrid
        #with self.canvas:
        #    Color(1., 0, 0)
        #    Ellipse(pos=(touch.x - self.size_x / 2, touch.y - self.size_y / 2), size=(self.size_x, self.size_y))
        #    Color(1, 1, 1)
        
        #screenGrid.fillArea(Point(touch.x - self.size_x / 2, touch.y - self.size_y / 2), Point(touch.x + self.size_x / 2, touch.y + self.size_y / 2))
        
    def placeAt(self, x, y):
        with self.canvas:
            Color(1., 0, 0)
            Ellipse(pos=(x - self.size_x / 2, y - self.size_y / 2), size=(self.size_x, self.size_y))
            Color(1, 1, 1)
        
        self._screenGrid.fillArea(Point(x - self.size_x / 2, y - self.size_y / 2), Point(x + self.size_x / 2, y + self.size_y / 2))
        
class TowerShadow(Widget):
    red = NumericProperty(0)
    size_max = (30,30)
    
    def __init__(self, position):
        super(TowerShadow, self).__init__()
        self.size_hint = (None, None)
        
        with self.canvas:
            Color(1., 0, 0)
            d=30.
            self.ellipse = Ellipse(pos=position, size=self.size_max, size_hint=(None, None))
            Color(1, 1, 1)
        
        self.bind(red = self.updateTower, 
                  pos = self.updateTower)
        
    def changePosition(self, newX, newY):
        posX = newX - self.ellipse.size[0] / 2
        posY = newY - self.ellipse.size[1] / 2
 
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
        self.red = red        