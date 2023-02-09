import numpy as np 

def N_total_pad(N_obs_pad:list,eff_pad:list):
    """
    Final number of muons for all pads considering the efficiency correction.
    """
    
    N = []
    for ii in range(0,64):
        N.append(N_obs_pad[ii]/eff_pad[ii])
        
    return N


def flux_pad(A:float,dt:float, eff_pad:list,N_obs_pad:list):
    "List of flux value for each RPC pad."

    flux_pad = []
    for i in range(len(eff_pad)):
        flux_pad.append(N_obs_pad[i]/(A*dt*eff_pad[i]))
    
    return flux_pad


def N_total(N_obs_pad:list,eff_pad:list)->float:
    """
    Final number of muons for all pads considering the efficiency correction.
    """
    
    N = 0 
    for ii in range(0,64):
        N += N_obs_pad[ii]/eff_pad[ii]
        
    return N

def flux_total(A:float,dt:float,eff_dict:dict,N_obs_list:list)->float:
    """
    Final flux, taking into account sensible area and time of measurment.
    """

    eff_list = list(eff_dict.values())

    N_tot = N_total(N_obs_list,eff_list)
    
    flux = N_tot/(A*dt)
    
    return flux 