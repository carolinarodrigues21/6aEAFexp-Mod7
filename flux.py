def prepare_array_efficiency(array_efficiencies:list):
    """
    Since different numerations of the pads were used, at the end it is necessary to 
    make them compatible.
    """
    array_efficiencies = np.array(array_efficiencies).reshape((8,8))
    array_efficiencies = np.transpose(array_efficiencies)
    
    array_cols = [array_efficiencies.T[ii] for ii in range(0,8)]
    array_efficiencies_aux = np.zeros((8,8))
    for ii in range(0,8):
        col = list(array_cols[ii])
        col.reverse()
        array_efficiencies_aux.T[ii] = col 
    
    array_efficiencies_aux = array_efficiencies_aux.reshape((1,64))
    array_efficiencies_aux = [array_efficiencies_aux[0][ii] for ii in range(0,64)]

    return array_efficiencies_aux

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
    Final flux, taking into account sensible area an time of measurent.
    """

    eff_list = list(eff_dict.values())
    eff_list = prepare_array_efficiency(eff_list)

    N_tot = N_total(N_obs_list,eff_list)
    
    flux = N_tot/(A*dt)
    
    return flux 