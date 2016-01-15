'''
Created on Jan 5, 2016

@author: Lucian Apetre
14.01.2016 Create TowerFactory
'''

from kivy.graphics import Ellipse, Color
from kivy.uix.widget import Widget
from Globals.Types import Point
from Globals import Types
from kivy.properties import NumericProperty

class TowerFactory(object):
    _instance = None
    _towers = []
    _towersMax = 0
    _towersCount = 0
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
        self._towersMax = nr
        for idx in range(0, nr):
            self._towers.append(Tower(self._screenGreed))

    def getTower(self):
        retVal = None
        if self._towersCount < self._towersMax:
            self._towersCount += 1
            retVal = self._towers.pop()
        else:
            print "WARNING! no more towers"
        return retVal
    
    def releaseTower(self, tower):
        self._towersCount -= 1
        self._towers.append(tower)
        
    def getBuildedTowers(self):
        return self._towersCount
        
    
class Tower(Widget):
    size_x = 30
    size_y = 30
    _screenGrid = None
    _posX = 0
    _posY = 0
    _maxPosX = 0
    _maxPosY = 0
    
    def __init__(self, screenGrid):
        super(Tower, self).__init__()
        self._screenGrid = screenGrid
        
    def placeAt(self, x, y):
        self._posX = x - self.size_x / 2
        self._posY = y - self.size_y / 2
        self._maxPosX = x + self.size_x / 2
        self._maxPosY = y + self.size_y / 2
        
        with self.canvas:
            Color(1., 0, 0)
            Ellipse(pos=(self._posX, self._posY), size=(self.size_x, self.size_y))
            Color(1, 1, 1)
        
        self._screenGrid.fillArea(Point(self._posX, self._posY), Point(self._maxPosX, self._maxPosY))

    def remove(self):
        self.canvas.clear()
        self._screenGrid.unfillArea(Point(self._posX, self._posY), Point(self._maxPosX, self._maxPosY))
        
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