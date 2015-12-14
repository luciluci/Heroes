'''
Created on Dec 14, 2015

@author: Lucian
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string("""
<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

class SettingsScreen(Screen):
    pass