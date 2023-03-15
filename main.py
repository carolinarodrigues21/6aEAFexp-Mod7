import math as mt
from matplotlib import pyplot as plt
import numpy as np

from info_file import * 
from efficiency_simulation import *
from graphs import *
from flux import *
from total_time import *

#RPC Parameters
Lx = 15/100 #cm
Ly = 19/100 #cm
H = 203/100 #cm
A = Lx*Ly*64 #cm^2
a_pad = Lx*Ly
dt = total_time('run_1M_09_02_2023/tempo.txt')

data_file_name = 'result.txt' 

Npad_bot, Npad_top, line_bot, col_bot, line_top, col_top = getINFO(data_file_name)

v_max = 20000                             # max value for the color range
hist2D_save_path1 = 'CountRPCtop.png'     # relative path for saving the 2D histogram for that file
hist2D_save_path2 = 'CountRPCdown.png'
hist1D_save_path1 = 'CountRPCtop1D.png'
hist1D_save_path2 = 'CountRPCdown1D.png'
title1 = 'Contagem por Pad RPC superior'
title2 = 'Contagem por Pad RPC inferior'

N_obs_top = hist2D_and_values(col_top,line_top, v_max, hist2D_save_path1, title1)
N_obs_bot = hist2D_and_values(col_bot,line_bot, v_max, hist2D_save_path2, title2)


plt.hist(Npad_bot, bins=63)
plt.title("RPC superior")
plt.xlabel('Número das pads')
plt.ylabel('Contagem de Eventos')
plt.savefig('CoroaTop')
plt.show()

plt.hist(Npad_top, bins=64)
plt.title("RPC inferior")
plt.xlabel('Número das pads')
plt.ylabel('Contagem de Eventos')
plt.savefig('CoroaBot')
plt.show()

# eff_nEvents_1M = True

# if eff_nEvents_1M:
#     efficiency = {1: 0.095224, 2: 0.10242, 3: 0.107277, 4: 0.109762, 5: 0.110121, 6: 0.107832, 7: 0.10252, 8: 0.095604, 9: 0.10032, 10: 0.106618, 11: 0.112485, 12: 0.115512, 13: 0.11534, 14: 0.1127, 15: 0.107312, 16: 0.100166, 17: 0.103373, 18: 0.110561, 19: 0.117712, 20: 0.119974, 21: 0.119608, 22: 0.117083, 23: 0.110755, 24: 0.103232, 25: 0.105014, 26: 0.113222, 27: 0.119055, 28: 0.122121, 29: 0.121635, 30: 0.118991, 31: 0.113205, 32: 0.10488, 33: 0.104522, 34: 0.113784, 35: 0.118686, 36: 0.121633, 37: 0.120989, 38: 0.118673, 39: 0.113015, 40: 0.105346, 41: 0.103349, 42: 0.11066, 43: 0.115847, 44: 0.11974, 45: 0.119624, 46: 0.117305, 47: 0.11105, 48: 0.10317, 49: 0.099582, 50: 0.108094, 51: 0.113178, 52: 0.116097, 53: 0.116001, 54: 0.112706, 55: 0.107233, 56: 0.10027, 57: 0.095261, 58: 0.102928, 59: 0.106866, 60: 0.110291, 61: 0.110138, 62: 0.107608, 63: 0.102025, 64: 0.095466}
# else:
#     eff_nEvents = 1
#     efficiency = efficiency_sim(eff_nEvents,Lx,Ly,H)

# flux_4each_pad = flux_pad(a_pad,dt,list(efficiency.values()),N_obs_top)
# print(flux_4each_pad)

# nTotalPad = N_total_pad(N_obs_top,list(efficiency.values()))

# hist1D_comparing(N_obs_top,nTotalPad)

#plt.plot(range(1,65), flux_4each_pad)
#plt.ylim(0,0.001)
#plt.show()

# final_flux = flux_total(A,dt,efficiency,N_obs_top)
# print(N_obs_top)
# print(final_flux)