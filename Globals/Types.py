'''
Created on Dec 15, 2015

@author: Lucian Apetre
'''

FRAME_REFRESH_RATE = 1.0/50

SCREEN_SIZE_WIDTH = 800
SCREEN_SIZE_HEIGHT = 600

SCREEN_TEXTURE_GRANULARITY = 3
SCREEN_MATRIX_GRANULARITY = 8

ROAD_WIDTH = 100#pixels
NUMBER_OF_TOWERS = 5
NUMBER_OF_VARCOLACS = 5

PROJECTILE_DURATION = 0.2 #seconds that a projectile is shto from tower to target

class Point:
    x = -1
    y = -1
        
    def __init__(self, x, y):
        self.x = x
        self.y = y
    