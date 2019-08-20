# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 17:51:00 2019

The following program deomonstrates the Strategy and Factory design patterns
within object-oriented programming. Instances of Humanoids are created using
concrete factories and these instances are assigned specific strategies based
on which factory is used. These strategies are designed in such a way that it 
is very easy to implement a new strategy and not break any code previously
based on the program.

@author: Joe
"""
from abc import ABC

from region_strat import MencrestStrat
from region_strat import KarnoraStrat
from region_strat import AdenValleyStrat
from region_strat import VoStrat

from expertise_strat import MencrestExpertiseStrat
from expertise_strat import KarnoraExpertiseStrat
from expertise_strat import AdenValleyExpertiseStrat
from expertise_strat import VoExpertiseStrat


# Abstract Factory
class Humanoid(ABC):
    
    def __init__(self, regionStrat, expertiseStrat):      
        self._regionStrat = regionStrat
        self._expertiseStrat = expertiseStrat
      
    def wealth(self):
        self._regionStrat.wealth()
     
    def religious(self):
        self._regionStrat.religious()
      
    def expertise(self):
        self._expertiseStrat.expertise()
        
        
# Concrete Factories for Villagers
class MencrestVillager(Humanoid):
    def __init__(self):
        super(MencrestVillager, self).__init__(MencrestStrat, None)
        
class KarnoraVillager(Humanoid):
    def __init__(self):
        super(KarnoraVillager, self).__init__(KarnoraStrat, None)
        
class AdenValleyVillager(Humanoid):
    def __init__(self):
        super(AdenValleyVillager, self).__init__(AdenValleyStrat, None)
        
class VoVillager(Humanoid):
    def __init__(self):
        super(VoVillager, self).__init__(VoStrat, None)


# Concrete Factories for Guards
class MencrestGuard(Humanoid):
    def __init__(self):
        super(MencrestGuard, self).__init__(MencrestStrat, MencrestExpertiseStrat)

class KarnoraGuard(Humanoid):
    def __init__(self):
        super(KarnoraGuard, self).__init__(KarnoraStrat, KarnoraExpertiseStrat)
        
class AdenValleyGuard(Humanoid):
    def __init__(self):
        super(AdenValleyGuard, self).__init__(AdenValleyStrat, AdenValleyExpertiseStrat)
        
class VoGuard(Humanoid):
    def __init__(self):
        super(VoGuard, self).__init__(VoStrat, VoExpertiseStrat)
        
        
# Test Drive
MV = MencrestVillager()
KV = KarnoraVillager()
AVV = AdenValleyVillager()
VV = VoVillager()

MG = MencrestGuard()
KG = KarnoraGuard()
AVG = AdenValleyGuard()
VG = VoGuard()

MV.wealth()
MV.religious()

KG.wealth()
KG.religious()
KG.expertise()