'''
Created on Jan 5, 2016

@author: Lucian Apetre
14.01.2016 Create TowerFactory
'''

from kivy.graphics import Ellipse, Color, Rectangle
from kivy.uix.widget import Widget
from Globals.Types import Point
from kivy.properties import NumericProperty, BooleanProperty
from kivy.animation import Animation
from kivy.clock import Clock
from functools import partial
import os

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
    

class Projectile(Widget):
    
    def __init__(self, pos, size):
        super(Projectile, self).__init__(pos=pos, size=size)
        with self.canvas:
            self.ellipse = Ellipse(pos=pos, size=size)
            
        self.bind(pos = self.updateTower)
        
    def updateTower(self, *args):
        self.ellipse.pos = self.pos
        
    def erase(self):
        self.canvas.clear()
    
class Tower(Widget):
    size_x = 63
    size_y = 100
    _screenGrid = None
    posX = 0
    posY = 0
    _maxPosX = 0
    _maxPosY = 0
    ResourcesPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Resources'))
    #projectile 
    _projectile_x = 20
    _projectile_y = 70
    
    _attackRadius = 200
    
    _bShooting = BooleanProperty(False)
    _varcolac = None
    
        
    def __init__(self, screenGrid):
        super(Tower, self).__init__()
        self._screenGrid = screenGrid
        self.bind(_bShooting = self._shoot)
        
    def setIsShooting(self, bShooting):
        self._bShooting = bShooting
        
    def setShootToPosition(self, position):
        self._shootToPosition = position
        
    def getShootToPosition(self):
        return self._shootToPosition
        
    def placeAt(self, x, y):
        self.posX = x - self.size_x / 2
        self.posY = y - self.size_y / 2
        self._maxPosX = x + self.size_x / 2
        self._maxPosY = y + self.size_y / 2
        
        with self.canvas:
            Rectangle(pos=(self.posX, self.posY), size=(self.size_x, self.size_y), source=self.ResourcesPath+"\\Tower_63x100.png")
            Color(1, 1, 1)
        
        self._screenGrid.fillArea(Point(self.posX, self.posY), Point(self._maxPosX, self._maxPosY))
        
    def remove(self):
        self.canvas.clear()
        self._screenGrid.unfillArea(Point(self.posX, self.posY), Point(self._maxPosX, self._maxPosY))
        
    def _shoot(self, *args):
        if self._bShooting == True:
            self._startShooting()
            
    def _stopShooting(self):
        self._bShooting = False
    
    def _startShooting(self):
        Clock.schedule_interval(self._shootProjectile, 1)
        
    def _shootProjectile(self, dt):
        position = self.getShootToPosition()
        proj = Projectile(pos=(self.posX + self._projectile_x, self.posY + self._projectile_y), size = (10, 10))
        self.add_widget(proj)
        self._animateProjectile(proj, position)
        #flag Varcolag for draining life when the projectile hits it
        #self._varcolac.flagStartShooting()
        #TO DO
        return self._bShooting
        
    #create projectile and start "shooting"
    def _animateProjectile(self, instance, toPosition):
        animation = Animation(pos=toPosition)
        animation.start(instance)
        animation.bind(on_complete = self._dezanimateProjectile)

    #clears the projectile that was just shot
    def _dezanimateProjectile(self, *args):
        projectile = args[1]
        self.remove_widget(projectile)
        projectile.erase()
        del projectile
        self._varcolac.drainLife()
        #drain life from the flaged Varcolac
        
    def getAttackRadius(self):
        return self._attackRadius
    
    def setCurrentVarcolac(self, varcolac):
        if self._varcolac != varcolac:
            print "change focused varcolac"
            self._varcolac = varcolac
    
    def _drainLife(self, varcolac):
        varcolac.drainLife()
        print "TO DO"
            
class TowerShadow(Widget):
    red = NumericProperty(0)
    size_max = (63,100)
    ResourcesPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Resources'))
    
    def __init__(self, position):
        super(TowerShadow, self).__init__()
        self.size_hint = (None, None)
        
        with self.canvas:
            Color(0, 1., 0)
            self.tower = Rectangle(pos=position, size=self.size_max, source=self.ResourcesPath+"\\Tower_63x100.png")
            Color(1, 1, 1)
        
        self.bind(red = self.updateTower, 
                  pos = self.updateTower)
        
    def changePosition(self, newX, newY):
        posX = newX - self.tower.size[0] / 2
        posY = newY - self.tower.size[1] / 2
 
        self.pos = (posX, posY)
    
    def updateTower(self, *args):
        self.size_hint = (None, None)
        self.canvas.clear()
        self.size = self.size_max
        with self.canvas:
            Color(self.red, 1., 0)
            self.tower = Rectangle(pos=self.pos, size=self.size_max, source=self.ResourcesPath+"\\Tower_63x100.png")
         
    def changeRed(self, red):
        self.red = red