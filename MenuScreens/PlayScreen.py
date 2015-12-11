'''
Created on Dec 11, 2015

@author: Lucian Apetre
'''
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from Characters.Varcolac import Varcolac
from kivy.clock import Clock

class PlayScreen(Screen):
    
    varcolac2 = None
    
    def on_pre_enter(self, *args):
        self.clear_widgets()
        Screen.on_pre_enter(self, *args)
        
    def on_enter(self, *args):
        self.varcolac2 = Varcolac()
        self.varcolac2.pos = (150, 300)
        
        varcolac = Varcolac()
        varcolac.pos = (150, 150)
        Clock.schedule_interval(varcolac.move, 1.0 / 60.0)
        
        backButton = Button(text="back")
        backButton.size_hint_x = 0.2
        backButton.size_hint_y = 0.1
        backButton.bind(on_release = self.goBack)   
        
        self.add_widget(varcolac)
        self.add_widget(self.varcolac2)
        self.add_widget(backButton)
        #test stop varcolac after 5 seconds
        Clock.schedule_once(varcolac.stopMovement, 5)
               
    def goBack(self, caller):
        self.manager.current = 'menu'
        
    def placeVarcolac(self, varcolac):
        varcolac.velocity = (1, 1)
        