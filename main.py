import math as mt
from matplotlib import pyplot as plt
import numpy as np

from info_file import * 
from efficiency_simulation import *
from hist2D_and_values import *
from flux import *

#RPC Parameters
Lx = 15/100 #cm
Ly = 19/100 #cm
H = 203/100 #cm
dt = 6484.156421 #s
A = Lx*Ly*64 #cm^2

data_file_name = 'result.txt' 

Npad_top, Npad_bot, line_top, col_top, line_bot, col_bot = getINFO(data_file_name)

v_max = 3000                                        # max value for the color range
hist2D_save_path = 'example.png'     # relative path for saving the 2D histogram for that file
title = '2D map 71k'

N_obs_top = hist2D_and_values(col_top,line_top, v_max, hist2D_save_path, title)
eff_nEvents_2M = True

if eff_nEvents_2M:
    efficiency = {1: 0.0519965, 2: 0.055161, 3: 0.057214, 4: 0.0584345, 5: 0.058457, 6: 0.0568765, 7: 0.0551395, 8: 0.052138, 9: 0.0542435, 10: 0.0572075, 11: 0.0597515, 12: 0.0607005, 13: 0.0602005, 14: 0.059475, 15: 0.0571135, 16: 0.0542635, 17: 0.055503, 18: 0.058525, 19: 0.061044, 20: 0.0621335, 21: 0.062147, 22: 0.0614075, 23: 0.058703, 24: 0.055453, 25: 0.056345, 26: 0.059517, 27: 0.061969, 28: 0.063179, 29: 0.0628635, 30: 0.061825, 31: 0.0592975, 32: 0.0559115, 33: 0.0565825, 34: 0.059609, 35: 0.0616025, 36: 0.0632265, 37: 0.0630195, 38: 0.0619905, 39: 0.059452, 40: 0.0563475, 41: 0.0555665, 42: 0.0590285, 43: 0.0613345, 44: 0.062263, 45: 0.062131, 46: 0.060913, 47: 0.058676, 48: 0.055425, 49: 0.0538335, 50: 0.057559, 51: 0.059288, 52: 0.060619, 53: 0.060564, 54: 0.059391, 55: 0.0575135, 56: 0.054275, 57: 0.0523775, 58: 0.055114, 59: 0.057103, 60: 0.058181, 61: 0.058476, 62: 0.0571855, 63: 0.0551645, 64: 0.0522895}
else:
    eff_nEvents = 1
    efficiency = efficiency_sim(eff_nEvents,Lx,Ly,H)

flux_4each_pad = flux_pad(A,dt,efficiency,N_obs_top)

#plt.plot(range(1,65), flux_4each_pad)
#plt.ylim(0,0.001)
#plt.show()


final_flux = flux_total(A,dt,efficiency,N_obs_top)
print(N_obs_top)
print(final_flux)
#print(flux_4each_pad)