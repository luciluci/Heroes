'''
Created on Jan 11, 2016

@author: Lucian Apetre
'''

from Globals import Types

class ScreenGrid:
    maxWidth = 0
    maxHeight = 0
    Matrix = []
    
    def __init__(self):
        self.maxWidth = Types.SCREEN_SIZE_WIDTH / Types.SCREEN_MATRIX_GRANULARITY
        self.maxHeight = Types.SCREEN_SIZE_HEIGHT / Types.SCREEN_MATRIX_GRANULARITY
        self.Matrix = [[0 for x in range(self.maxHeight)] for x in range(self.maxWidth)]
    
    def fillArea(self, fromPoint, toPoint):
        fromX = int(fromPoint.x / Types.SCREEN_MATRIX_GRANULARITY)
        toX = int(toPoint.x / Types.SCREEN_MATRIX_GRANULARITY)
        fromY = int(fromPoint.y / Types.SCREEN_MATRIX_GRANULARITY)
        toY = int(toPoint.y / Types.SCREEN_MATRIX_GRANULARITY)
        for pointX in range(fromX , toX):
            for pointY in range(fromY, toY):
                self.Matrix[pointX][pointY] = 1
        #self.displayScreenMatrix()
    
    def fill(self):
        pass
    
    def getScreenMatrix(self):
        return self.Matrix
    
    def displayScreenMatrix(self):
        f = open('workfile.txt', 'w')
        width = len(self.Matrix)
        #height = len(self.Matrix[0])
        for pointX in range(0, width):
            #print self.Matrix[pointX][:]
            f.write("\n")
            f.write(str(self.Matrix[pointX][:]))
        f.close()
        
    def isColliding(self, fromPoint, toPoint):
        retVal = False
        fromX = int(fromPoint.x / Types.SCREEN_MATRIX_GRANULARITY)
        toX = int(toPoint.x / Types.SCREEN_MATRIX_GRANULARITY)
        fromY = int(fromPoint.y / Types.SCREEN_MATRIX_GRANULARITY)
        toY = int(toPoint.y / Types.SCREEN_MATRIX_GRANULARITY)
        
        if toX > self.maxWidth or fromX < 0:
            #print "WARNING! out of screen bounds"
            return True
        if toY > self.maxHeight or fromY < 0:
            #print "WARNING! out of screen bounds"
            return True
        
        for pointX in range(fromX , toX):
            for pointY in range(fromY, toY):
                if self.Matrix[pointX][pointY] == 1:
                    retVal = True
                    break
                
        return retVal