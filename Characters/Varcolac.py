'''
Created on Dec 10, 2015

@author: Lucian Apetre
'''
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.lang import Builder
from Globals import Types
import datetime
from kivy.core.image import Image
import os


Builder.load_string("""
<Varcolac>:
    size: 30, 30
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1 
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
    speed = 2
    
    route = []
    routeIndex = 0
    
   # image = Image((os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Resources')))+"robot_right.gif")
    
    def __init__(self):
        super(Varcolac, self).__init__()
        #self.pos = (x, y)
        self.pos = Types.SCREEN_ENTRY_POINT
        #set first checkpoint to current position. workaround for not messing up the recursivity in moveTo method
        self.goToX = Types.SCREEN_ENTRY_POINT[0]
        self.goToY = Types.SCREEN_ENTRY_POINT[1]
        
        #ResourcesPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Resources'))
        #self.image = Image(ResourcesPath+"\\robot_right.gif")

    def stopMovement(self):
        #print "varcolacul s-a oprit"
        self.isMoving = False;
    
    def run(self, dt):
        if self.x < self.goToX:
            self.direction_x = self.speed
        elif self.x > self.goToX:
            self.direction_x = -1 * self.speed
        else:
            self.direction_x = 0
        if self.y < self.goToY:
            self.direction_y = self.speed
        elif self.y > self.goToY:
            self.direction_y = -1 * self.speed
        else:
            self.direction_y = 0
        self.direction = self.direction_x, self.direction_y
        
        #print "TIME:" + str(datetime.datetime.now().time())
        
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
        