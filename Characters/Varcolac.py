'''
Created on Dec 10, 2015

@author: Lucian Apetre
'''
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.lang import Builder
from Globals import Types
from kivy.graphics import Ellipse, Color

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
    goToX = 0
    goToY = 0
    
    route = []
    routeIndex = 0
    
    def __init__(self, x, y):
        super(Varcolac, self).__init__()
        self.pos = (x, y)
        #set first checkpoint to current position. workaround for not messing up the recursivity in moveTo method
        self.goToX = x
        self.goToY = y

    def stopMovement(self):
        #print "varcolacul s-a oprit"
        self.isMoving = False;
    
    def run(self, dt):
        if self.x < self.goToX:
            self.direction_x = 1
        elif self.x > self.goToX:
            self.direction_x = -1
        else:
            self.direction_x = 0
        if self.y < self.goToY:
            self.direction_y = 1
        elif self.y > self.goToY:
            self.direction_y = -1
        else:
            self.direction_y = 0
        self.direction = self.direction_x, self.direction_y
        
        #print "moveTo %d %d From %d %d" %(self.goToX, self.goToY, self.x, self.y)
        
        if self.direction == (0, 0):
            checkPoint = self._getNextCheckPoint()
            if checkPoint:
                #print "next point %d %d" % (checkPoint[0], checkPoint[1])
                (self.goToX, self.goToY) = checkPoint
                self.run(Types.FRAME_REFRESH_RATE)
        if self.direction == (0, 0):
            self.stopMovement()
        
        return self._move(Types.FRAME_REFRESH_RATE)
    
    def _move(self, dt):
        self.pos = Vector(*self.direction) + self.pos
        self.canvas.ask_update()
        return self.isMoving
    
    def setRoute(self, route):
        self.route = list(route)
        self.route.reverse()
            
    def _getNextCheckPoint(self):
        if len(self.route) <= 0:
            return None
        return self.route.pop()    
        