'''
Created on 30/04/2011

@author: dave
'''

class Fragment():
        
    def __init__(self, text='', tones=None, moods=None, subject=None):
        self.text = text
        self.tones = [] if tones == None else tones
        self.moods = [] if moods == None else moods
        self.subject = '' if subject == None else subject
        
    def __str__(self):
        return self.text