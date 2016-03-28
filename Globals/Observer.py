'''
Created on Mar 27, 2016

@author: lucian
'''
from Globals.Subject import Subject
from kivy.uix.widget import WidgetMetaclass
from _pyio import __metaclass__

class ObserverMetaclass(type):
    pass

class MetaclassScreenObserver(WidgetMetaclass, ObserverMetaclass):
    pass

class Observer():
    
    #__metaclass__ = ObserverMetaclass
    _model = Subject
        
    def __init__(self, model):
        self.model = model
        model.attach(self)
        
    def getSubject(self):
        return self._model
        
    def update(self):
        raise NotImplementedError('You need to define a update method!')