'''
Created on Dec 14, 2015

@author: Lucian
'''
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string("""
<LoadingScreen>:
    FloatLayout:
        AsyncImage:
            source: '../examples/widgets/sequenced_images/data/images/button_white_animated.zip'
            size_hint: 1, .5
            pos_hint: {'center_x':.5, 'center_y': .5}
""")

class LoadingScreen(Screen):
    def on_enter(self, *args):
        print("LoadingScreen")
        Screen.on_enter(self, *args)