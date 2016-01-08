'''
Created on Dec 11, 2015

@author: Lucian Apetre
'''

from Characters.Tower import Tower
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from Characters.Varcolac import Varcolac
from kivy.clock import Clock
from kivy.uix.widget import Widget
from Globals import Types
from kivy.uix.stacklayout import StackLayout
from ScreenElements.Background import Background
from ScreenElements.Road import Road
from kivy.graphics import Ellipse, Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

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


class Controls(Widget):
    pass

class Score(Widget):
    score = 1

class Life(Widget):
    val = 100

class Gelb(Widget):
    amount = 1000
    
class bck(Widget):
    def __init__(self):
        super(bck, self).__init__()
        
        with self.canvas:
            Color(1., 0, 0)
            d = 30.
            Ellipse(pos=(50,50), size=(d, d))
            Color(1, 1, 1)

class Point:
    x = -1
    y = -1
        
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class ScreenGrid:
    Matrix = [[0 for x in range(Types.SCREEN_SIZE_HEIGHT+1)] for x in range(Types.SCREEN_SIZE_WIDTH+1)]
    granularity = 1 #currenlty not used, will be used to speed up the game computations.
    
    def fillArea(self, fromPoint, toPoint):
        for pointX in range(fromPoint.x, toPoint.x+1):
            for pointY in range(fromPoint.y, toPoint.y+1):
                self.Matrix[pointX][pointY] = 1
    
    def fill(self):
        pass
    
    def getScreenMatrix(self):
        return self.Matrix

class GameControls(ScreenGrid):
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
    
    def __init__(self):
        #super(GameControls, self).__init__()
        
        self.layout = StackLayout(size=(Types.SCREEN_SIZE_WIDTH, 100), orientation="lr-bt", size_hint=(None, None))
        self.backButton = Button(text='Back', size_hint=(.2, .1), pos_hint={'x':.01, 'y':.01})
        #self.backButton.bind(on_release = self.goBack)
        
        self.lblScore = Label(text='SCORE:', size_hint=(.1, .1))
        self.lblScoreValue = Label(text='0', size_hint=(.1, .1))
        self.lblLife = Label(text='LIFE:', size_hint=(.1, .1))
        self.lblLifeValue = Label(text='100', size_hint=(.1, .1))
        self.lblResources = Label(text='RESOURCES:', size_hint=(.1, .1))
        self.lblResourcesValue = Label(text='100', size_hint=(.1, .1))
        
        
        self.layout.canvas.add(Color(.8, .7, .1, .7))
        self.layout.canvas.add(Rectangle(size=self.layout.size))
        
        self.layout.add_widget(self.backButton)
        
        self.layout.add_widget(self.lblScore)
        self.layout.add_widget(self.lblScoreValue)
        self.layout.add_widget(self.lblLife)
        self.layout.add_widget(self.lblLifeValue)
        self.layout.add_widget(self.lblResources)
        self.layout.add_widget(self.lblResourcesValue)
        
        self.fill()
        
    def fill(self):
        self.fillArea(Point(0,0), Point(Types.SCREEN_SIZE_WIDTH, 100))
        

class PlayScreen(Screen):

    labirinth = None
    route = []
    varcolaci = []
    backButton = None
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
    
    
    def __init__(self, name):
        super(PlayScreen, self).__init__()
        self.name = name
        
        self.clear_widgets()
        self.route.extend(ROAD)
                
        self.background = Background()
        self.road = Road(self.route)
        self.controls = GameControls()
        self.controls.backButton.bind(on_release = self.goBack)
        
        print "ds"
        
    def on_pre_enter(self, *args):
        Screen.on_pre_enter(self, *args)
        self.clear_widgets()
        
    def on_enter(self, *args):
        self.screenAlive = True

        #self.menuBar = StackLayout(spacing=[10, 10])
        #self.menuBar.add_widget(self.backButton)
        
        self.add_widget(self.background)
        self.add_widget(self.road)
        #self.add_widget(self.menuBar)
        self.add_widget(self.controls.layout)
        #self.add_widget(self.layout)

        #throw first varcolac in the game
        Clock.schedule_once(self.addVarcolac, 0)
        
    def clearMenuBar(self):
        #self.menuBar.remove_widget(self.backButton)
        print "todo"
               
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
        bCanAddTower = True
        if self.controls.layout.collide_point(touch.x, touch.y) == True:
            print "colision with menu"
            bCanAddTower = False
        
        if self.road.collide_point(touch.x, touch.y) == True:
            print "colision with road"
            bCanAddTower = False
                
        if bCanAddTower == True:
            self.addTower(touch)
        return Screen.on_touch_down(self, touch)
    
    def _isScreenAlive(self):
        return self.screenAlive
        