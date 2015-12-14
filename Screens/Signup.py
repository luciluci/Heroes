'''
Created on Dec 14, 2015

@author: Lucian Apetre
'''

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder

Builder.load_string("""
<SignupScreen>:
    FloatLayout:
        cols: 2
        Label:
            text: 'Name'
            size_hint: .2, .1
            pos: 200, 430
        TextInput:
            size_hint: .3, .1
            pos: 370, 430
        Label:
            text: 'email'
            size_hint: .2, .1
            pos: 200, 370
        TextInput:
            size_hint: .3, .1
            pos: 370, 370
        Label:
            text: 'User Name'
            size_hint: .2, .1
            pos: 200, 310
        TextInput:
            size_hint: .3, .1
            pos: 370, 310
        Label:
            text: 'Password'
            password: True
            size_hint: .2, .1
            pos: 200, 250
        TextInput:
            size_hint: .3, .1
            pos: 370, 250
        Button:
            text: 'Create account'
            size_hint: .22, .1
            pos: 220, 190
            on_press: root.register()
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
            size_hint: .2, .1
""")

class SignupScreen(Screen):
    def register(self):
        print "registering"
        box = BoxLayout()
        box.add_widget(Label(text='Registration successful'))
        
        popup = Popup(title='Registration',
                      content=box,
                      size_hint=(.5, .5))
        popup.open()
    pass