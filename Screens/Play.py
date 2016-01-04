'''
Created on Dec 11, 2015

@author: Lucian Apetre
'''

from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from Characters.Varcolac import Varcolac
from kivy.clock import Clock
from kivy.uix.widget import Widget
from Globals import Types
from kivy.graphics import Ellipse, Color, Rectangle, Line
from kivy.core.image import Image
from kivy.uix.stacklayout import StackLayout
import math
import os

ROAD = [(0, 150), (420, 150), (420, 300), (200, 300), (200, 400), (700, 400), (700, 600)]

from kivy.lang import Builder

Builder.load_string(
"""
<Controls>
    mScore: score
    mLife: life
    mGelb: gelb
    FloatLayout:
        Widget:
            size_hint: None, None
            size: 730, 100
            pos: 30, 30
            canvas:
                Color:
                    rgba: .5, .1, .1, .5
                Rectangle:
                    pos: self.pos
                    size: self.size
    Score:
        id: score
    Life: 
        id: life
    Gelb:
        id: gelb
<Score>
    size: 150, 50
    pos: 70, 70
    canvas:
        Color:
            rgba: .1, .5, .1, .5
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        pos: 70, 45
        text: "Score:"
    Label:
        pos: 120, 45
        text: str(root.score)
        
<Life>
    size: 150, 50
    pos: 230, 70
    canvas:
        Color:
            rgba: .1, .5, .1, .5
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        pos: 230, 45
        text: "LIFE:"
    Label:
        pos: 260, 45
        text: str(root.val)
        
<Gelb>
    size: 150, 50
    pos: 390, 70
    canvas:
        Color:
            rgba: .1, .5, .1, .5
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        pos: 390, 45
        text: "GELB:"
    Label:
        pos: 430, 45
        text: str(root.amount)
""")

class eDirections():
    DIR_STANDING = 0
    DIR_UP    = 1
    DIR_DOWN  = 2
    DIR_LEFT  = 3
    DIR_RIGHT = 4
    direction = 0
    def __init__(self):
        self.direction = self.DIR_STANDING
        
class eCorner():
    CORNER_NONE       = 10
    CORNER_LEFT_UP    = 31
    CORNER_LEFT_DOWN  = 32
    CORNER_RIGHT_UP   = 41
    CORNER_RIGHT_DOWN = 42
    CORNER_UP_LEFT    = 13
    CORNER_UP_RIGHT   = 14
    CORNER_DOWN_LEFT  = 23
    CORNER_DOWN_RIGHT = 24
    corner = 10
    def __init__(self):
        self.corner = self.CORNER_NONE

class Controls(Widget):
    pass

class Score(Widget):
    score = 1

class Life(Widget):
    val = 100

class Gelb(Widget):
    amount = 1000

class Background(Widget):
    
    def __init__(self):
        super(Background, self).__init__()
        
        with self.canvas:
            ResourcesPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Resources'))
            bckImage = Image(ResourcesPath+'\\grass.png')
            texture = bckImage.texture
            texture.wrap = 'repeat'
            texture.uvsize = ((Types.SCREEN_SIZE_WIDTH/bckImage.width) * Types.SCREEN_TEXTURE_GRANULARITY, (Types.SCREEN_SIZE_HEIGHT/bckImage.height) * Types.SCREEN_TEXTURE_GRANULARITY)
            Rectangle(texture=texture, size=(Types.SCREEN_SIZE_WIDTH, Types.SCREEN_SIZE_HEIGHT), pos=self.pos)
            
class Road(Widget):
    
    _route = []
    _resourcesPath = None   
        
    def __init__(self, route):
        super(Road, self).__init__()
        self._route = route
        self._resourcesPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Resources'))
        
        with self.canvas:
            #road data
            self._drawRoad()#works only on 90 degrees angle between points
            #Line(points=self._getRoutePoints(ROAD), width=2)
            self._drawCorners()
            Color(1, 1, 1)
    
    def _drawCorners(self):
        imgCornerLeftUp = Image(self._resourcesPath+'\\grass_road_1.png')
        imgCornerLeftDown = Image(self._resourcesPath+'\\grass_road_1.png')
        imgCornerRightUp = Image(self._resourcesPath+'\\grass_road_1.png')
        imgCornerRightDown = Image(self._resourcesPath+'\\grass_road_1.png')
        imgCornerUpLeft = Image(self._resourcesPath+'\\grass_road_1.png')
        imgCornerUpRight = Image(self._resourcesPath+'\\grass_road_1.png')
        imgCornerDownLeft = Image(self._resourcesPath+'\\grass_road_1.png')
        imgCornerDownRight = Image(self._resourcesPath+'\\grass_road_1.png')
        
        cornerType = eCorner()
        for point in range(0, len(self._route)-2):
            cornerType = self._getCornerType(self._route[point], self._route[point+1], self._route[point+2])
            posX = self._route[point+1][0] - Types.ROAD_WIDTH/2
            posY = self._route[point+1][1] - Types.ROAD_WIDTH/2
            if cornerType == eCorner.CORNER_LEFT_UP:
                imgTexture = imgCornerLeftUp.texture
            elif cornerType == eCorner.CORNER_LEFT_DOWN:
                imgTexture = imgCornerLeftDown.texture
            elif cornerType == eCorner.CORNER_RIGHT_UP:
                imgTexture = imgCornerRightUp.texture
            elif cornerType == eCorner.CORNER_RIGHT_DOWN:
                imgTexture = imgCornerRightDown.texture
            elif cornerType == eCorner.CORNER_UP_LEFT:
                imgTexture = imgCornerUpLeft.texture
            elif cornerType == eCorner.CORNER_UP_RIGHT:
                imgTexture = imgCornerUpRight.texture
            elif cornerType == eCorner.CORNER_DOWN_LEFT:
                imgTexture = imgCornerDownLeft.texture
            elif cornerType == eCorner.CORNER_DOWN_RIGHT:
                imgTexture = imgCornerDownRight.texture
            imgTexture = self._createTexture(imgTexture)
            Rectangle(texture = imgTexture, size=(Types.ROAD_WIDTH, Types.ROAD_WIDTH), pos=(posX, posY))
            
    def _getCornerType(self, point1, point2, point3):
        retVal = eCorner()
        
        direction = self._getDirection(point1, point2)
        retVal.corner = (direction * 10) + self._getDirection(point2, point3)
        
        return retVal.corner
        
    def _drawRoad(self):
        img = Image(self._resourcesPath+'\\grass_road_1.png')
        imgTexture = img.texture
        
        for point in range(0, len(self._route)-1):
                self._drawRoadSegment(self._route[point], self._route[point+1], imgTexture)
        
    def _drawRoadSegment(self, point1, point2, imgTexture):
        rectWidth = Types.ROAD_WIDTH
        rectHeight = Types.ROAD_WIDTH
        
        rectStartPosX = 0
        rectStartPosY = 0
        direction = self._getDirection(point1, point2)
            
        if (direction == eDirections.DIR_LEFT) or (direction == eDirections.DIR_RIGHT):
            rectWidth = math.fabs(point2[0] - point1[0])# + Types.ROAD_WIDTH
            if direction == eDirections.DIR_RIGHT:
                rectStartPosX = point1[0]# - Types.ROAD_WIDTH/2
                rectStartPosY = point1[1] - Types.ROAD_WIDTH/2
            else:
                rectStartPosX = point2[0]
                rectStartPosY = point2[1] - Types.ROAD_WIDTH/2
        elif (direction == eDirections.DIR_DOWN) or (direction == eDirections.DIR_UP):
            rectHeight = math.fabs(point2[1] - point1[1])# + Types.ROAD_WIDTH
            if direction == eDirections.DIR_UP:
                rectStartPosX = point1[0] - Types.ROAD_WIDTH/2
                rectStartPosY = point1[1]# - Types.ROAD_WIDTH/2
            else:
                rectStartPosX = point2[0] - Types.ROAD_WIDTH/2
                rectStartPosY = point2[1]
        else:
            print "WARNING! Computing road direction failed"
        #print "RECTANGLE: size:(width:%d, height:%d) pos=(x:%d, y:%d)" %(rectWidth, rectHeight, rectStartPosX, rectStartPosY)
        texture = self._createTexture(imgTexture, rectWidth, rectHeight)
        Rectangle(texture=texture, size=(rectWidth, rectHeight), pos=(rectStartPosX, rectStartPosY))
    
    def _createTexture(self, imgTexture, width = 100, height = 100):
        #texture = img.texture
        texture = imgTexture
        texture.wrap = 'repeat'
        texture.uvsize = (width/Types.ROAD_WIDTH, height/Types.ROAD_WIDTH)
        return texture
            
    def _getRoutePoints(self, route):
        retVal = []
        for point in route:
            retVal.extend(list(point))
        return retVal
    
    def _getDirection(self, point1, point2):
        retVal = eDirections()
        if point1[0] == point2[0]:
            if point1[1] < point2[1]: 
                retVal.direction = eDirections.DIR_UP
            elif point1[1] > point2[1]:
                retVal.direction = eDirections.DIR_DOWN
            else:
                retVal.direction = eDirections.DIR_STANDING
        if point1[1] == point2[1]:
            if point1[0] < point2[0]: 
                retVal.direction = eDirections.DIR_RIGHT
            elif point1[0] > point2[0]:
                retVal.direction = eDirections.DIR_LEFT
            else:
                retVal.direction = eDirections.DIR_STANDING        
        return retVal.direction
        
class Tower(Widget):
    
    def __init__(self, touch):
        super(Tower, self).__init__()
        
        with self.canvas:
            Color(1., 0, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            Color(1, 1, 1)

class PlayScreen(Screen):

    labirinth = None
    route = []
    varcolaci = []
    backButton = None
    screenAlive = False
    menuBar = None
    
    def __init__(self, name):
        super(PlayScreen, self).__init__()
        self.name = name
        
        self.clear_widgets()
        self.route.extend(ROAD)
                
        self.background = Background()
        self.road = Road(self.route)
        
        self.backButton = Button(text="back")
        self.backButton.size_hint_x = 0.2
        self.backButton.size_hint_y = 0.1
        self.backButton.bind(on_release = self.goBack)
        
    def on_pre_enter(self, *args):
        Screen.on_pre_enter(self, *args)
        self.clear_widgets()
        
    def on_enter(self, *args):
        self.screenAlive = True

        self.menuBar = StackLayout(spacing=10)
        self.menuBar.add_widget(self.backButton)
        
        self.add_widget(self.background)
        self.add_widget(self.road)
        self.add_widget(self.menuBar)
        self.add_widget(Controls())

        #throw first varcolac in the game
        Clock.schedule_once(self.addVarcolac, 0)
        
    def clearMenuBar(self):
        self.menuBar.remove_widget(self.backButton)
               
    def goBack(self, caller):
        self.clearMenuBar()
        self.screenAlive = False
        while len(self.varcolaci) > 0:
            varcolac = self.varcolaci.pop()
            varcolac.stopMovement()
            self.remove_widget(varcolac)
        self.manager.current = 'menu'
        self.clear_widgets()
        
    def addVarcolac(self, dt):
        if(self._isScreenAlive() and len(self.varcolaci) < 5):
            print "one more"
            varcolac = Varcolac(self.route)
            varcolac.setRoute(self.route)
            
            self.add_widget(varcolac)
            self.varcolaci.append(varcolac)
            Clock.schedule_interval(varcolac.run, Types.FRAME_REFRESH_RATE)
            #throw another varcolac in the game
            Clock.schedule_once(self.addVarcolac, 1)
    
    def addTower(self, touch):
        tower = Tower(touch)
        self.add_widget(tower)               
        
    def on_touch_down(self, touch):
        self.addTower(touch)
        return Screen.on_touch_down(self, touch)
    
    def _isScreenAlive(self):
        return self.screenAlive
        