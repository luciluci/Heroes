'''
Created on Dec 9, 2015

@author: luciluci
'''

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

Builder.load_string("""
<LoadingScreen>:
    FloatLayout:
        AsyncImage:
            source: '../examples/widgets/sequenced_images/data/images/button_white_animated.zip'
            size_hint: 1, .5
            pos_hint: {'center_x':.5, 'center_y': .5}
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
<PlayScreen>:
    FloatLayout:
        Label:
            text: 'PLAY'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
<PlayOnline>:
    FloatLayout:
        Label:
            text: 'Play Online'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

# Declare screens
class MenuScreen(Screen):
    pass

class LoginScreen(Screen):
    def signIn(self):
        print "signing in"
    pass

class PlayScreen(Screen):
    pass

class PlayOnline(Screen):
    pass

class SettingsScreen(Screen):
    pass

class SignupScreen(Screen):
    def register(self):
        print "registering"
        box = BoxLayout()
        box.add_widget(Label(text='Hello world'))
        box.add_widget(TextInput(text='Hi'))
        
        popup = Popup(title='Registration',
                      content=box,
                      size_hint=(.5, .5))
        popup.open()
    pass

class LoadingScreen(Screen):
    def on_enter(self, *args):
        print("LoadingScreen")
        Screen.on_enter(self, *args)
    
# Create the screen manager
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(PlayScreen(name='play'))
sm.add_widget(PlayOnline(name='playonline'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(LoadingScreen(name='loadingScreen'))
sm.add_widget(SignupScreen(name='signup'))
sm.current = 'menu'

class TestApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()