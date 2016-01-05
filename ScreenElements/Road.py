'''
Created on Jan 5, 2016

@author: Apetre Lucian
'''

from kivy.core.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from Globals import Types
import math

import os

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
