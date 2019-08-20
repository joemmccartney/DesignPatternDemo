# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 17:40:02 2019

The following is the collection of strategies for determining a Humanoid's 
wealth and religious disposition.

@author: Joe
"""
from abc import ABC, abstractmethod

class RegionStratAbstract(ABC):
 
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def wealth(): pass
    
    @abstractmethod
    def religious(): pass

# Strategy for generating values of citizens of the Mencrest region
class MencrestStrat(RegionStratAbstract):
    def wealth():
        print ("I live a modest life.")
    
    def religious():
        print ("I am a God fearing man.")

# Strategy for generating values of citizens of the Karnora region
class KarnoraStrat(RegionStratAbstract):
    def wealth():
        print ("I make enough to support my family.")
    
    def religious():
        print ("I reject God and his plans.")

# Strategy for generating values of citizens of the Aden Valley region     
class AdenValleyStrat(RegionStratAbstract):
    def wealth():
        print ("I live a luxurious life.")
    
    def religious():
        print ("I am more concerned with my own well-being.")

# Strategy for generating values of citizens of the Vo region    
class VoStrat(RegionStratAbstract):
    def wealth():
        print ("I live in the streets.")
    
    def religious():
        print ("I am nothing to God's glorious magnificence.")
     