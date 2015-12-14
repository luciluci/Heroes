'''
Created on Dec 14, 2015

@author: Lucian
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string("""
<PlayOnlineScreen>:
    FloatLayout:
        Label:
            text: 'Play Online'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

class PlayOnlineScreen(Screen):
    pass