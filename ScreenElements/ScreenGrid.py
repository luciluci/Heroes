'''
Created on Jan 11, 2016

@author: Lucian Apetre
'''

from Globals import Types

class ScreenGrid:
    granularity = 0#screen greed granularity
    maxWidth = 0
    maxHeight = 0
    Matrix = []
    
    def __init__(self):
        self.granularity = 8#screen greed granularity
        self.maxWidth = Types.SCREEN_SIZE_WIDTH / self.granularity
        self.maxHeight = Types.SCREEN_SIZE_HEIGHT / self.granularity
        self.Matrix = [[0 for x in range(self.maxHeight)] for x in range(self.maxWidth)]
    
    def fillArea(self, fromPoint, toPoint):
        fromX = int(fromPoint.x / self.granularity)
        toX = int(toPoint.x / self.granularity)
        fromY = int(fromPoint.y / self.granularity)
        toY = int(toPoint.y / self.granularity)
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
        fromX = int(fromPoint.x / self.granularity)
        toX = int(toPoint.x / self.granularity)
        fromY = int(fromPoint.y / self.granularity)
        toY = int(toPoint.y / self.granularity)
        
        if toX > self.maxWidth or fromX < 0:
            print "WARNING! out of screen bounds"
            return True
        if toY > self.maxHeight or fromY < 0:
            print "WARNING! out of screen bounds"
            return True
        
        for pointX in range(fromX , toX):
            for pointY in range(fromY, toY):
                if self.Matrix[pointX][pointY] == 1:
                    retVal = True
                    break
                
        return retVal