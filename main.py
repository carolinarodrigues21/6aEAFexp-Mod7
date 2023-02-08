import math as mt
from matplotlib import pyplot as plt
import numpy as np

from info_file import * 
from efficiency_simulation import *
from N_obs import *
from flux import *

#RPC Parameters
Lx = 15 #cm
Ly = 19 #cm
H = 203 #cm
dt = 30420 #s
A = Lx*Ly*64 #cm^2

# data_file_name = 'example-run.txt'
data_file_name = 'pre-process-coluna1-linhas8-a-3.txt'

Npad_top, Npad_bot, line_top, col_top, line_bot, col_bot = getINFO(data_file_name)

v_max = 100                                         # max value for the color range
hist2D_save_path = 'results\example.png'     # relative path for saving the 2D histogram for that file

N_obs_top, N_obs_bot = N_obs_RPC(col_top, col_bot, line_top, line_bot, v_max, hist2D_save_path)
eff_nEvents_1M = True

if eff_nEvents_1M:
    efficiency = {0: 0.052534, 1: 0.053989, 2: 0.055612, 3: 0.056623, 4: 0.056218, 5: 0.055375, 6: 0.054243, 7: 0.051963, 8: 0.055211, 9: 0.057167, 10: 0.05867, 11: 0.059443, 12: 0.059653, 13: 0.058743, 14: 0.057031, 15: 0.05477, 16: 0.057463, 17: 0.059252, 18: 0.061278, 19: 0.061729, 20: 0.061536, 21: 0.061331, 22: 0.059352, 23: 0.057299, 24: 0.058316, 25: 0.060905, 26: 0.062655, 27: 0.062782, 28: 0.063172, 29: 0.062101, 30: 0.060895, 31: 0.057795, 32: 0.058849, 33: 0.060553, 34: 0.062012, 35: 0.063271, 36: 0.062791, 37: 0.062486, 38: 0.060252, 39: 0.058446, 40: 0.057037, 41: 0.059404, 42: 0.06142, 43: 0.06181, 44: 0.06196, 45: 0.060574, 46: 0.059466, 47: 0.057165, 48: 0.055445, 49: 0.057501, 50: 0.058641, 51: 0.059472, 52: 0.059193, 53: 0.058257, 54: 0.057433, 55: 0.055157, 56: 0.05227, 57: 0.054044, 58: 0.055897, 59: 0.056257, 60: 0.056152, 61: 0.055658, 62: 0.054067, 63: 0.051891}
else:
    efficiency = efficiency_sim()

final_flux = flux_total(A,dt,efficiency,N_obs_top)
print(N_obs_top)
print(final_flux)