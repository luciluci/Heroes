'''
Created on Mar 27, 2016

@author: lucian
'''
from Globals.Types import VarcolacEvents

#Watchdog used to track dead Varcolacs

class Subject:
    _views = []
    _event = VarcolacEvents.NoEvent
    
    def attach(self, observer):
        self._views.append(observer)
        
    def setEvent(self, evt):
        self._event = evt
        self.notify()
        
    def notify(self):
        for view in self._views: 
            view.update()
            
class Watchdog(object):
    _instance = None
    
    _observers = []
    _event = VarcolacEvents.NoEvent
    _id = -1
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Watchdog, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    
    def attach(self, observer):
        self._observers.append(observer)
        
    def setEvent(self, evt):
        self._event = evt
        self.notify()
        
    def setVarcolacId(self, id):
        self._id = id
        
    def notify(self):
        for view in self._observers: 
            view.update(self._id)
            
gWatchdog = Watchdog()