'''
Created on Dec 11, 2015

@author: Lucian Apetre
'''
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from Characters.Varcolac import Varcolac
from kivy.clock import Clock

class PlayScreen(Screen):
    
    def on_pre_enter(self, *args):
        self.clear_widgets()
        Screen.on_pre_enter(self, *args)
        
    def on_enter(self, *args):
        varcolac = Varcolac()
        varcolac.pos = (150, 150)
        Clock.schedule_interval(varcolac.move, 1.0 / 60.0)
        
        backButton = Button(text="back")
        backButton.size_hint_x = 0.2
        backButton.size_hint_y = 0.1
        backButton.bind(on_release = self.goBack)   
        
        self.add_widget(varcolac)
        self.add_widget(backButton)
               
        
    def goBack(self, caller):
        self.manager.current = 'menu'
        
    def placeVarcolac(self, varcolac):
        varcolac.velocity = (1, 1)
        