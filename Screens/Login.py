'''
Created on Dec 14, 2015

@author: Lucian
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string("""
<LoginScreen>:
    FloatLayout:
        cols: 2
        Label:
            text: 'User Name'
            size_hint: .2, .1
            pos: 200, 430
        TextInput:
            size_hint: .3, .1
            pos: 370, 430
        Label:
            text: 'Password'
            password: True
            size_hint: .2, .1
            pos: 200, 370
        TextInput:
            size_hint: .3, .1
            pos: 370, 370
        Button:
            text: 'Sign In'
            size_hint: .22, .1
            pos: 220, 280
            on_press: root.signIn()
        Button:
            text: 'Sign Up'
            size_hint: .22, .1
            pos: 400, 280
            on_press: root.manager.current = 'signup'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
            size_hint: .2, .1
""")

class LoginScreen(Screen):
    def signIn(self):
        print "signing in"
    pass