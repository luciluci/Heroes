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

Builder.load_string("""
<Labirinth>
    canvas:
        Rectangle:
            pos: 30, 300
            size: 300, 20
""")

class Labirinth(Widget):
    pass

class PlayScreen(Screen):
    
    varcolac = None
    labirinth = None
    
    def on_pre_enter(self, *args):
        self.clear_widgets()
        
        self.labirinth = Labirinth()
        self.varcolac = Varcolac()
        
        Screen.on_pre_enter(self, *args)
        
    def on_enter(self, *args):        
        
        self.varcolac.pos = (150, 150)
        self.varcolac.directionUp()
        self.varcolac.setLabirinth(self.labirinth)
        
        Clock.schedule_interval(self.varcolac.move, 1.0 / 60.0)
        
        backButton = Button(text="back")
        backButton.size_hint_x = 0.2
        backButton.size_hint_y = 0.1
        backButton.bind(on_release = self.goBack)   
        
        self.add_widget(self.varcolac)
        self.add_widget(backButton)
        self.add_widget(self.labirinth)
        #test stop varcolac after 5 seconds
        Clock.schedule_once(self.varcolac.stopMovement, 5)
               
    def goBack(self, caller):
        self.manager.current = 'menu'
        
    def placeVarcolac(self, varcolac):
        varcolac.velocity = (1, 1)
        