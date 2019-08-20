# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 16:15:54 2019

The following is the collection of strategies for determining a Humanoid's 
expertise.

@author: Joe
"""

from abc import ABC, abstractmethod

class ExpertiseStratAbstract(ABC):
 
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def expertise(): pass
    
# Strategy for generating the value of a guards expertise in Mencrest
class MencrestExpertiseStrat(ExpertiseStratAbstract):
    def expertise():
        print ("I mostly just sit around all day.")

# Strategy for generating the value of a guards expertise in Karnora
class KarnoraExpertiseStrat(ExpertiseStratAbstract):
    def expertise():
        print ("I am a cunning adversery.")
    
    # Strategy for generating the value of a guards expertise in Aden Valley
class AdenValleyExpertiseStrat(ExpertiseStratAbstract):
    def expertise():
        print ("I am a capable combatant.")
    
    # Strategy for generating the value of a guards expertise in Vo
class VoExpertiseStrat(ExpertiseStratAbstract):
    def expertise():
        print ("I am a master of combat.")