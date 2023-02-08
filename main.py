import math as mt
from matplotlib import pyplot as plt
import numpy as np

from info_file import * 
from efficiency_simulation import *
from N_obs import *

#RPC Parameters
Lx = 15
Ly = 19
H = 203

# data_file_name = 'example-run.txt'
data_file_name = 'pre-process-coluna1-linhas8-a-3.txt'

Npad_top, Npad_bot, line_top, col_top, line_bot, col_bot = getINFO(data_file_name)

v_max = 100                                         # max value for the color range
hist2D_save_path = 'results\example.png'     # relative path for saving the 2D histogram for that file

N_obs_top, N_obs_bot = N_obs_RPC(col_top, col_bot, line_top, line_bot, v_max, hist2D_save_path)

efficiency = efficiency_sim()