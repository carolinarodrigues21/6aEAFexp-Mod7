import numpy as np 
import matplotlib.pyplot as plt
import random

h = 203 # Final measured height between rpcs [cm]
Lx = 15 # Pad size [cm]
Ly = 19 # Pad size [cm]
x_lim = 120 # Sensible area [cm]
y_lim = 152 # Sensible area [cm]

def generate_angle(angle = True):
    """
    Generate the two angles corresponding to the muon direction, one zenith angle 
    and one azimuthal angle. More precisely, the cosine of the zenith angle is 
    generated (we want a uniformely distributed angles in 3-D).
    """
    
    if (angle):
        
        zenith_angle = random.uniform(0,1)
        
        return zenith_angle
    else:
        
        azimuthal_angle = random.uniform(0,2*np.pi)
        
        return azimuthal_angle

#generate_angle(False)  


def coordinates_pad(pad_number):
    """
    Given a pad number, i.e., a number between 0 and 63, the coordinates of the
    center of the pad are calculated.
    """
    rpc = np.array([0 for ii in range(64)])
    rpc[pad_number] = 1 
    rpc = rpc.reshape(8,8)
    idx_x = int(np.where(rpc == 1)[0])+1
    idx_y = int(np.where(rpc == 1)[1])+1
    
    coord_x = Lx/2 + (idx_y-1)*Lx
    coord_y = Ly/2 + (idx_x-1)*Ly
    
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
    if ((x_inter < x_lim and 0 < x_inter) and (y_inter < y_lim and 0 < y_inter)):
        hit = True
    
    return hit

#hit_evt_pad((119,149,180),0,4.430693526565017)

def efficiency_sim(n_events):
    """
    Calculate the efficiency per pad for a given number of events.
    """
    
    pads_dict = dict()

    for pad in range(0,64):
        
        coord_pad = coordinates_pad(pad)
        az_angles_pad = list() # Not used at the end
        ze_angles_pad = list() # Not used at the end
        
        count_hits_pad = 0
        for evt in range(0,n_events):
            # Direction of the muon
            az_angle = generate_angle(False)
            ze_angle = np.arccos(generate_angle()) # Remember that we generated a random num. bet. 0-1.
            
            hit_evt = hit_evt_pad(coord_pad,ze_angle,az_angle)
            if (hit_evt):
                count_hits_pad += 1
        
        eff =  count_hits_pad/n_events
        pads_dict[pad] = eff
        
    return pads_dict