'''
Created on Dec 14, 2015

@author: Lucian
'''

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from Screens.Play import PlayScreen
from Screens.Signup import SignupScreen
from Screens.Login import LoginScreen
from Screens.Loading import LoadingScreen
from Screens.PlayOnline import PlayOnlineScreen
from Screens.Settings import SettingsScreen
from Screens.MainMenu import MenuScreen

# Create the screen manager
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(PlayScreen(name='play'))
sm.add_widget(PlayOnlineScreen(name='playonline'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(LoadingScreen(name='loadingScreen'))
sm.add_widget(SignupScreen(name='signup'))
sm.current = 'menu'

class Game(App):
    def build(self):
        return sm

if __name__ == '__main__':
    Game().run()