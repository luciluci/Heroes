'''
Created on Dec 11, 2015

@author: Lucian Apetre
'''

from Characters.Tower import Tower, TowerShadow, TowerFactory
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from Characters.Varcolac import Varcolac
from kivy.clock import Clock
from Globals import Types
from Globals.Types import Point
from kivy.uix.stacklayout import StackLayout
from ScreenElements.Background import Background
from ScreenElements.Road import Road
from ScreenElements.ScreenGrid import ScreenGrid
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.core.window import Window
from functools import partial

ROAD = [(0, 150), (420, 150), (420, 300), (200, 300), (200, 400), (700, 400), (700, 600)]

class GameControls():
    #holder element
    layout = None
    
    #elements
    backButton = None
    lblScore = None
    lblScoreValue = None
    lblLife = None
    lblLifeValue = None
    lblResources = None
    lblResourcesValue = None
    createTower = None
    
    screenGrid = None
    
    def __init__(self, screenGrid):
        self.screenGrid = screenGrid
        
        self.layout = StackLayout(size=(Types.SCREEN_SIZE_WIDTH, 80), orientation="lr-bt", size_hint=(None, None))
        self.backButton = Button(text='Back', size_hint=(.1, .4), pos_hint={'x':.01, 'y':.01})
        
        self.lblScore = Label(text='SCORE:', size_hint=(.1, .4))
        self.lblScoreValue = Label(text='0', size_hint=(.1, .4))
        self.lblLife = Label(text='LIFE:', size_hint=(.1, .4))
        self.lblLifeValue = Label(text='100', size_hint=(.1, .4))
        self.lblResources = Label(text='RESOURCES:', size_hint=(.1, .4))
        self.lblResourcesValue = Label(text='100', size_hint=(.1, .4))
        
        self.createTower = Button(text='Tower', size_hint=(.1, .4), pos_hint={'x':.01, 'y':.01})
        
        self.layout.canvas.add(Color(.8, .7, .1, .7))
        self.layout.canvas.add(Rectangle(size=self.layout.size))
        
        self.layout.add_widget(self.backButton)
        self.layout.add_widget(self.lblScore)
        self.layout.add_widget(self.lblScoreValue)
        self.layout.add_widget(self.lblLife)
        self.layout.add_widget(self.lblLifeValue)
        self.layout.add_widget(self.lblResources)
        self.layout.add_widget(self.lblResourcesValue)
        self.layout.add_widget(self.createTower)
        
        self.fill()
        
    def fill(self):
        self.screenGrid.fillArea(Point(0,0), Point(Types.SCREEN_SIZE_WIDTH, 80))
        

class PlayScreen(Screen):

    labirinth = None
    route = []
    varcolaci = []
    screenAlive = False
    
    #test
    layout = None
    
    lblScore = None
    lblScoreValue = None
    lblLife = None
    lblLifeValue = None
    lblResources = None
    lblResourcesValue = None
    
    controls = None
    screenGrid = None
    
    #TowerShadow
    towerShadow = None
    bTowerShadowOn = False
    _towerFactory = None
    
    
    def __init__(self, name):
        super(PlayScreen, self).__init__()
        
        self.screenGrid = ScreenGrid()
        self._towerFactory = TowerFactory(self.screenGrid)
        self._towerFactory.setMaxTowers(Types.NUMBER_OF_TOWERS)
        self.name = name
        
        self.clear_widgets()
        self.route.extend(ROAD)
                
        self.background = Background()
        
        self.road = Road(self.route, self.screenGrid)
        self.controls = GameControls(self.screenGrid)
        
        self.controls.backButton.bind(on_release = self.goBack)
        self.controls.createTower.bind(on_release = self.createTowerShadowClick)
        
    def on_pre_enter(self, *args):
        Screen.on_pre_enter(self, *args)
        self.clear_widgets()
        
    def on_enter(self, *args):
        self.screenAlive = True
        
        self.add_widget(self.background)
        self.add_widget(self.road)
        self.add_widget(self.controls.layout)

        #throw first varcolac in the game
        Clock.schedule_once(self.addVarcolac, 0)
        
    def clearMenuBar(self):
        #self.menuBar.remove_widget(self.backButton)
        print "todo"
               
    def goBack(self, caller):
        self.clearMenuBar()
        self.screenAlive = False
        self.screenGrid.displayScreenMatrix()
        while len(self.varcolaci) > 0:
            varcolac = self.varcolaci.pop()
            varcolac.stopMovement()
            self.remove_widget(varcolac)
        self.manager.current = 'menu'
        self.clear_widgets()
        
    def addVarcolac(self, dt):
        if(self._isScreenAlive() and len(self.varcolaci) < 5):
            varcolac = Varcolac(self.route)
            varcolac.setRoute(self.route)
            
            self.add_widget(varcolac)
            self.varcolaci.append(varcolac)
            Clock.schedule_interval(varcolac.run, Types.FRAME_REFRESH_RATE)
            #throw another varcolac in the game
            Clock.schedule_once(self.addVarcolac, 1)
    
    def addTower(self, touch):
        
        #tower = Tower(touch, self.screenGrid)
        tower = self._towerFactory.getTower()
        if tower:
            tower.placeAt(touch.x, touch.y)
            self.add_widget(tower)
        self.bTowerShadowOn = False               
        
    def on_touch_down(self, touch):
        bCanAddTower = True
        
        towerGridStartPoint = Point(self._correctPosition(touch.x)-Tower.size_x/2, self._correctPosition(touch.y)-Tower.size_y/2)
        towerGridEndPoint   = Point(self._correctPosition(touch.x)+Tower.size_x/2, self._correctPosition(touch.y)+Tower.size_y/2)
        
        if self.screenGrid.isColliding(towerGridStartPoint, towerGridEndPoint):
            #print "WARNING! cannot built tower on other widgets"
            bCanAddTower = False

        if bCanAddTower == True:
            towerPosX = self._correctPosition(touch.x)
            towerPosY = self._correctPosition(touch.y)
            
            self.addTower(Point(towerPosX, towerPosY))
            self.remove_widget(self.towerShadow)
            del self.towerShadow
        return Screen.on_touch_down(self, touch)
    
    def _isScreenAlive(self):
        return self.screenAlive
        
    def createTowerShadowClick(self, caller):
        self.towerShadow = TowerShadow((Window.mouse_pos[0], Window.mouse_pos[1]))
        self.add_widget(self.towerShadow)
        self.bTowerShadowOn = True
        Clock.schedule_interval(partial(self.moveTower, self.towerShadow), 0.05)
        
    def moveTower(self, shadow, dt):
        if self._isScreenAlive() == False or self.bTowerShadowOn == False:
            return False
        
        towerShadowPosX = self._correctPosition(Window.mouse_pos[0])
        towerShadowPosY = self._correctPosition(Window.mouse_pos[1])
        
        shadow.changePosition(towerShadowPosX, towerShadowPosY)
        
        if self.screenGrid.isColliding(Point(towerShadowPosX-shadow.width/2, towerShadowPosY-shadow.height/2), Point(towerShadowPosX+shadow.width/2, towerShadowPosY+shadow.height/2)):
            shadow.changeRed(0.2)
            #print "WARNING! position unavailable"
        else:
            shadow.changeRed(1)
        
        return True
    
    #used to detect nearest grid point
    def _correctPosition(self, pos):
        correctedPos = 0
        if pos % Types.SCREEN_MATRIX_GRANULARITY <= Types.SCREEN_MATRIX_GRANULARITY / 2:
            correctedPos = int(pos / Types.SCREEN_MATRIX_GRANULARITY) * Types.SCREEN_MATRIX_GRANULARITY
        else:
            correctedPos = int(pos / Types.SCREEN_MATRIX_GRANULARITY) * Types.SCREEN_MATRIX_GRANULARITY + 1
        return correctedPos