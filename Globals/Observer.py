'''
Created on Mar 27, 2016

@author: lucian
'''
from Globals.Subject import Subject

class Observer:
    model = Subject
    
    def __init__(self, model):
        self.model = model
        model.attach(self)
        
    def update(self):
        raise NotImplementedError('You need to define a update method!')