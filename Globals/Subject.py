'''
Created on Mar 27, 2016

@author: lucian
'''
from Characters.Varcolac import VarcolacEvents

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