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


class Background(Widget):
    
    def __init__(self):
        super(Background, self).__init__()
        
        with self.canvas:
            ResourcesPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Resources'))
            texture = Image(ResourcesPath+'\\grass.png').texture
            texture.wrap = 'repeat'
            texture.uvsize = (8,8)
            Rectangle(texture=texture, size=(800, 600), pos=self.pos)
        
class Tower(Widget):
    
    def __init__(self, touch):
        super(Tower, self).__init__()
        
        with self.canvas:
            Color(1., 0, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            Color(1, 1, 1)
            
class GameControls(Widget):
    
    def __init__(self):
        super(GameControls, self).__init__()
        
        with self.canvas:
            Color(.1, .1, 1, .9)
            Line(width = 2., rectangle=(self.x, self.y, self.width, self.height))
            Color(1, 1, 1)

class PlayScreen(Screen):

    labirinth = None
    route = []
    varcolaci = []
    backButton = None
    screenAlive = False
    menuBar = None
    controls = None
    
    
    def __init__(self, name):
        super(PlayScreen, self).__init__()
        self.name = name
        
        self.clear_widgets()
        
        self.route = [(420, 150), (420, 300), (200, 300), (200, 400), (700, 400), (700, 600)]        
        self.background = Background()
        
        self.backButton = Button(text="back")
        self.backButton.size_hint_x = 0.2
        self.backButton.size_hint_y = 0.1
        self.backButton.bind(on_release = self.goBack)
        
        self.controls = GameControls()
        
        
    def on_pre_enter(self, *args):
        Screen.on_pre_enter(self, *args)
        self.clear_widgets()
        
    def on_enter(self, *args):
        self.screenAlive = True

        self.menuBar = StackLayout(spacing=10)
        self.menuBar.add_widget(self.backButton)
        self.menuBar.add_widget(self.controls)
        
        self.add_widget(self.background)
        self.add_widget(self.menuBar)

        #throw first varcolac in the game
        Clock.schedule_once(self.addVarcolac, 0)
        
    def clearMenuBar(self):
        self.menuBar.remove_widget(self.backButton)
        self.menuBar.remove_widget(self.controls)
               
    def goBack(self, caller):
        self.clearMenuBar()
        self.screenAlive = False
        while len(self.varcolaci) > 0:
            varcolac = self.varcolaci.pop()
            varcolac.stopMovement()
            self.remove_widget(varcolac)
        self.manager.current = 'menu'
        
    def addVarcolac(self, dt):
        if(self._isScreenAlive() and len(self.varcolaci) < 5):
            varcolac = Varcolac(150, 150)
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
        