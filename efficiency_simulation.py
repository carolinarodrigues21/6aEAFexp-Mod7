import numpy as np 
import matplotlib.pyplot as plt
import random

Lx = 15 #cm
Ly = 19 #cm
H = 203 #cm
dt = 30420 #s
A = Lx*Ly*64 #cm^2

def generate_angle(angle = True):
    """
    Generate the two angles corresponding to the muon direction, one zenith angle 
    and one azimuthal angle.
    """
    
    if (angle):
        
        zenith_angle = np.arccos(random.uniform(0,1))
        
        return zenith_angle
    else:
        
        azimuthal_angle = random.uniform(0,2*np.pi)
        
        return azimuthal_angle 

def coordinates_pad(pad_number:int,Lx:float,Ly:float,h:float):
    """
    Given a pad number, i.e., a number between 0 and 63, the coordinates of the
    center of the pad are calculated.
    """
    
    for i in range(1,9):
        if (pad_number - i)%8 == 0:
            col =(pad_number - i)/8 + 1
        else:
            i+= 1
            
    fil = 8 - (8*col - pad_number)

    coord_x = Lx*(col - 0.5)
    coord_y = Ly*(fil - 0.5)

    return (coord_x,coord_y,h)

def hit_evt_pad(coord_pad:tuple,ze_angle:float,az_angle:float):
    """
    Given the pad coordinates of the top rpc and the two angles corresponding 
    to the muon direction, is determined whether the muon hit the bottom rpc or not.
    """
    
    x = np.sin(ze_angle)*np.cos(az_angle) # from spherical coordinates to cartesian
    y = np.sin(ze_angle)*np.sin(az_angle) # from spherical coordinates to cartesian
    z = np.cos(ze_angle) # from spherical coordinates to cartesian
    unit_vec = (x,y,z) # trajectory unit vector 
    
    # Equation of the line in 3-D when z = 0
    alpha = -coord_pad[2]/unit_vec[2] # The free parameter is determined 
    # Coordinates of the point in which the muon hit the plane of the bottom rpc
    x_inter = coord_pad[0] + alpha * unit_vec[0]
    y_inter = coord_pad[1] + alpha * unit_vec[1]
        
    hit = False
    # Condition to determine wheter the muon hit
    if ((x_inter < Lx*8 and 0 < x_inter) and (y_inter < Ly*8 and 0 < y_inter)):
        hit = True
    
    return hit

def efficiency_sim(Lx:float,Ly:float,h:float, n_events = 10**6):
    """
    Calculate the efficiency per pad for a given number of events.
    """
    
    pads_dict = dict()

    for pad in range(1,65):
        
        coord_pad = coordinates_pad(pad,Lx,Ly,h)
        
        count_hits_pad = 0
        for evt in range(0,n_events):
            # Direction of the muon
            az_angle = generate_angle(False)
            ze_angle = generate_angle() # Remember that we generated a random num. bet. 0-1.
            
            hit_evt = hit_evt_pad(coord_pad,ze_angle,az_angle)
            if (hit_evt):
                count_hits_pad += 1
        
        eff =  count_hits_pad/n_events
        pads_dict[pad] = eff
        
    return pads_dict