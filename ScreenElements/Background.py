'''
Created on Jan 5, 2016

@author: Lucian Apetre
'''

from kivy.core.image import Image
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from Globals import Types
import os

class Background(Widget):
    
    def __init__(self):
        super(Background, self).__init__()
        
        with self.canvas:
            ResourcesPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Resources'))
            bckImage = Image(ResourcesPath+'\\grass.png')
            texture = bckImage.texture
            texture.wrap = 'repeat'
            texture.uvsize = ((Types.SCREEN_SIZE_WIDTH/bckImage.width) * Types.SCREEN_TEXTURE_GRANULARITY, (Types.SCREEN_SIZE_HEIGHT/bckImage.height) * Types.SCREEN_TEXTURE_GRANULARITY)
            Rectangle(texture=texture, size=(Types.SCREEN_SIZE_WIDTH, Types.SCREEN_SIZE_HEIGHT), pos=self.pos)