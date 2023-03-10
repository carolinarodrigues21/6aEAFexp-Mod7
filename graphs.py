from matplotlib import pyplot as plt

def hist1D_count(nEvento1, nEvento2):

    fig, (ax1,ax2) = plt.subplots(2,1,  figsize = [10,20])
    ax1.hist(nEvento1, bins=64)
    ax2.hist(nEvento2, bins=63)
    
    ax1.set_title("RPC superior")
    ax2.set_title("RPC inferior")

    ax1.set_xlabel('Número das pads')
    ax1.set_ylabel('Contagem de Eventos')
    ax2.set_xlabel ('Número das pads')
    plt.savefig('Coroa')
    
    return plt.show()

def hist1D_comparing(N_obs,N_tot):
    "Creates 2 histograms comparing the nunber of events observed and the total events"

    nObs = []
    nTot = []
    for j in range(64):
        for i in range(N_obs[j]):
            nObs.append(j)
        
        for k in range(int(N_tot[j])):
            nTot.append(j)

    fig, (ax1,ax2) = plt.subplots(1,2,  figsize = [20,10])
    ax1.hist(nObs, bins=63)
    ax2.hist(nTot, bins=63)
    
    ax1.set_title("Eventos Medidos")
    ax2.set_title("Eventos Totais")

    ax1.set_xlabel('Pads')
    ax1.set_ylabel('Eventos')
    ax2.set_xlabel ('Pads')

    fig.suptitle("Comparação antes e depois da correção geométrica")
    return plt.show()



def hist2D_and_values(col, lin, v_max:int , save_path:str, title:str):
    """
    Creates a 2D histogtam with the value for each cell and returns that value.
    
    """
    fig, ax1 = plt.subplots(figsize = [10,5])

    ax1.set_aspect("equal")
    hist, xbins, ybins, im = ax1.hist2d(col, lin, bins=[8,8],vmin=0, vmax=v_max, cmap="YlOrRd")

    values = []

    for i in range(len(ybins)-1):
        for j in range(len(xbins)-1):
            ax1.text(xbins[j]+0.5,ybins[i]+0.5, int(hist.T[i,j]), 
                    color="black", ha="center", va="center", fontsize = 'x-small')
            values.append(int(hist.T[j,i]))

    ax1.set_xlabel('Coluna')
    ax1.set_ylabel('Linha')

    fig.suptitle(title)
    plt.savefig(save_path)
    plt.show()
    return values