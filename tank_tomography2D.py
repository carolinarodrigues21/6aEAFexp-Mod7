import numpy as np
import matplotlib.pyplot as plt
from info_file import *
from hist2D_and_values import *

def getVOLT(filename):
    '''Gets the values of the voltages peak at a PMT.
        - filename: (str), .txt file with the voltage values
    Returns a list with  the values of voltage (float).'''
    voltagem = []
    with open(filename) as file:
        for line in file:
            str_line = str(line)
            col_list = str_line.split()
            voltagem.append(float(col_list[0]))
    
    return voltagem

def tank_location(filenameRPC, filenamePMT, threshold, vmax, save_path, title):
    '''Create a 2D histogram with the lines and columns of the pads that a muon hit with vertical trajectory. It also creates a txt file with the 
    number of those pads (top and bottom) for posterior analysis.
        - filenameRPC: (str), .txt file with the RPC digital signal
        - filenamePMT: (str), .txt file with the voltage values
        - threshold: (float), threshold of voltage for filtering
        - vmax: (float), maximum value of the scale of the 2D histogram
        - save_path: (str), path for saving the graph
        - title: (str), title of the graph'''
    nPads_top, nPads_bot, nEventos = getINFO(filenameRPC)
    volt = getVOLT(filenamePMT)

    volt_event = []
    index_hit = []
    Npad_top_hit, Npad_bot_hit = [], []
    VerticalHit = []
    line_top, col_top = [], []

    for i in range(len(volt)):
        if volt[i] < threshold:
            volt_event.append(i)

    for i in range(len(nEventos)):
        if int(nEventos[i]) in volt_event:
            index_hit.append(i)
    
    for index in index_hit:
        Npad_top_hit.append(nPads_top[index])
        Npad_bot_hit.append(nPads_bot[index])
    
    for i, j in zip(Npad_top_hit, Npad_bot_hit):
        if i == j:
            VerticalHit.append(i)
  
    for i in VerticalHit:
            line, col = LineColPad(i)
            line_top.append(line)
            col_top.append(col)

    hist2D_and_values(col_top, line_top, vmax, save_path, title)

    f = open("VerticalHitRotate.txt", "w")
    for i in VerticalHit:
        f.write(str(i)+" "+str(i)+"\n")
    f.close()