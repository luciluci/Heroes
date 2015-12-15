'''
Created on Dec 11, 2015

@author: Lucian Apetre
'''
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from Characters.Varcolac import Varcolac
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.widget import Widget
from Globals import Types

Builder.load_string("""
<Labirinth>
    canvas:
        Rectangle:
            pos: 0, 60
            size: self.width, 8
""")

class Labirinth(Widget):
    pass

class PlayScreen(Screen):

    labirinth = None
    route = []
    varcolaci = []
    
    def on_pre_enter(self, *args):
        self.clear_widgets()
        
        self.route = [(420, 150), (420, 300), (200, 300), (200, 400), (700, 400), (700, 600)]        
        self.labirinth = Labirinth()
        
        Screen.on_pre_enter(self, *args)
        
    def on_enter(self, *args):        
        
        backButton = Button(text="back")
        backButton.size_hint_x = 0.2
        backButton.size_hint_y = 0.1
        backButton.bind(on_release = self.goBack)
        
        self.add_widget(backButton)
        self.add_widget(self.labirinth)

        for num in range(0,5):
            Clock.schedule_once(self.addVarcolac, num)
               
    def goBack(self, caller):
        for varcolac in self.varcolaci:
            varcolac.stopMovement()
        self.manager.current = 'menu'
        
    def addVarcolac(self, dt):
        varcolac = Varcolac(150, 150)
        varcolac.setRoute(self.route)
        
        self.add_widget(varcolac)
        self.varcolaci.append(varcolac)
        Clock.schedule_interval(varcolac.run, Types.FRAME_REFRESH_RATE)       
        
        