# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:12:47 2022

@author: stefa
"""
import os
import IPython
from pyhamilton import (HamiltonInterface,  LayoutManager, 
 Plate96, Tip96, initialize, tip_pick_up, tip_eject, move_sequence,
 aspirate, dispense,  oemerr, resource_list_with_prefix, normal_logging)

liq_class = 'StandardVolumeFilter_Water_DispenseJet_Empty'



lmgr = LayoutManager('deck.lay')
plates = resource_list_with_prefix(lmgr, 'plate_', Plate96, 5)
tips = resource_list_with_prefix(lmgr, 'tips_', Tip96, 1)
liq_class = 'StandardVolumeFilter_Water_DispenseJet_Empty'

aspiration_poss = [(plates[0], x) for x in range(8)]
dispense_poss = [(plates[0], x) for x in range(8,16)]
vols_list = [100]*8


tips_poss = [(tips[0], x) for x in range(8)]

def enter_pyhamilton_repl():
    IPython.embed()

if __name__ == '__main__': 
    with HamiltonInterface(simulate=True) as ham_int:
        normal_logging(ham_int, os.getcwd())
        initialize(ham_int)
        enter_pyhamilton_repl()

# move_sequence(ham_int, 'plate_1', 0,0,1)