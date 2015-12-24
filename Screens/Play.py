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
import os

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

class Background(Widget):
    
    def __init__(self):
        super(Background, self).__init__()
        
        with self.canvas:
            ResourcesPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Resources'))
            texture = Image(ResourcesPath+'\\grass.png').texture
            texture.wrap = 'repeat'
            texture.uvsize = (8,8)
            Rectangle(texture=texture, size=(800, 600), pos=self.pos)
            
class Road(Widget):
        
    def __init__(self, route):
        super(Road, self).__init__()
        
        with self.canvas:
            Color(1, .9, .6)
            Line(points=self._getRoutePoints(route), width=10)
            Color(1, 1, 1)
            
    def _getRoutePoints(self, route):
        retVal = []
        for point in route:
            retVal.extend(list(point))
        return retVal
        
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
        
        self.route.append(Types.SCREEN_ENTRY_POINT)
        self.route.extend([(420, 150), (420, 300), (200, 300), (200, 400), (700, 400)])
        self.route.append(Types.SCREEN_EXIT_POINT)
                
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
            varcolac = Varcolac()
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
        