from math import tan, sin, cos, sqrt, atan2, pi, acos
import random
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from info_file import *

# measures
H = 203
Lx = 15
Ly = 19
xmax = 8*Lx
ymax = 8*Ly

# number of events
N = 1000000

def XandY(line, col):
    '''Function that find the position of a pad (considering its center) by its line and column number. The reference system has its origin at 
    the bottom left of the pad number 1 (line 1 and column 1). The arguments are:
    line (int) - the number of the line of a certain pad
    col (int) - the number of the column of a certain pad
    The function returns the x and y (floats) of a pad.
    '''
    x = (col - 1)*Lx + Lx/2
    y = (line - 1)*Ly + Ly/2
    return x,y

def position_RPC_bot(Npad, Theta, Phi):
    '''Function that finds where a muon hit the bottom RPC. The arguments are:
    Npad (int) - The number of the pad at the top RPC that a muon hit 
    Theta (float) - Zenital angle of the muon trajectory, in radians
    Phi (float) - Azimutal angle of the muon trajectory, in radians
    It returns the x and y (floats) where a muon hit the bottom RPC
    '''
    lpad, colpad = LineColPad(Npad)
    x0, y0 = XandY(lpad, colpad)

    d = H*tan(Theta)
    deltaX = d*sin(Phi)
    deltaY = d*cos(Phi)
    x, y = (x0 + deltaX, y0 + deltaY)
    
    return x,y

# Simulating the angles of the muon trajectory

theta = [] #zenital angle
phi = [] #azimutal angle
for i in range(0,N):
    one_cos2theta = np.random.rand()*(1 - 0) # cos² theta
    one_costheta = sqrt(one_cos2theta)
    one_phi = np.random.rand()*(2*pi - 0)
    one_theta = acos(one_costheta)
    
    theta.append(one_theta)
    phi.append(one_phi)

# Counting how many muons hit the bottom RPC

count_in_pad = []
for pad in range(1,65):
    count_in = 0
    for i,j in zip(theta, phi):
        x, y = position_RPC_bot(pad, i, j)
        if 0<x and x<xmax:
            if 0<y and y<ymax:
                count_in = count_in + 1
        else:
            continue
    count_in_pad.append(count_in)

# Hist 1D
plt.plot(np.arange(1,65), count_in_pad)
plt.title("Contagem de muons (em coincidência) por pad simulada")
plt.xlabel("Número da pad")
plt.ylabel("Contagem")

# Efficiency calculation for each pad

ef = []
for i in count_in_pad:
    ef_pad = i/N
    ef.append(ef_pad)

plt.plot(np.arange(0,64,1), ef)
plt.title("Eficiência simulada de cada pad da RPC superior")
plt.xlabel("Número da pad")
plt.ylabel("Eficiência")

# Flux calculation

Npad_bot, Npad_top, Nevento = getNpad("result.txt")
Nobs_dic = Counter(Npad_top) #Number of coincidence events observed in each pad of the top RPC

Ntot_pad_list = []
Ntot = 0
for i in range(0,64):
    ntot_pad = Nobs_dic[i + 1]/ef[i]
    Ntot_pad_list.append(Nobs_dic[i + 1]/ef[i])
    Ntot = Ntot + ntot_pad

# Calculating the total time
dt = 0
with open("tempo.txt") as file:
    for line in file:
        dt = dt + float(line)

# Measures in m and s
xmax = 8*Lx*0.01
ymax = 8*Ly*0.01
dt = dt/(10**6)

fluxo = Ntot/(xmax*ymax*dt)
print(fluxo)

# Incertainty

Nobs_list = list(Nobs_dic.values())
sum = 0
for i in Nobs_list:
    sum = sum + 1/i
inc = 1/sqrt(sum)
print(inc)





