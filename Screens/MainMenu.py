'''
Created on Dec 9, 2015

@author: luciluci
'''

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<MenuScreen>:
    FloatLayout:
        Button:
            text: 'Play'
            pos: 200, 450
            size_hint: .5, .1
            on_press: root.manager.current = 'play'
        Button:
            text: 'Settings'
            pos: 200, 390
            size_hint: .5, .1
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Play Online'
            pos: 200, 330
            size_hint: .5, .1
            on_press: root.manager.current = 'playonline'
        Button:
            text: 'Login'
            pos: 200, 270
            size_hint: .5, .1
            on_press: root.manager.current = 'login'
        
""")

# Declare screens
class MenuScreen(Screen):
    pass