from matplotlib import pyplot as plt

def N_obs_RPC(col_top, col_bottom, lin_top, lin_bottom, v_max, save_path):
    """
    Given the columns and lines of each pad, it gives the value of the number of events for each of the RPC pad.
    It also returns a 2D histogram with these values.
    
    """
    fig, (ax1,ax2) = plt.subplots(1,2, figsize = [10,5])

    ax1.set_aspect("equal")
    hist, xbins, ybins, im = ax1.hist2d(col_top, lin_top, bins=[8,8],vmin=0, vmax=v_max, cmap="YlOrRd")

    count_pads_top = []
    count_pads_bot = []

    for i in range(len(ybins)-1):
        for j in range(len(xbins)-1):
            ax1.text(xbins[j]+0.5,ybins[i]+0.5, int(hist.T[i,j]), 
                    color="black", ha="center", va="center", fontsize = 'x-small')
            count_pads_top.append(int(hist.T[j,i]))

    ax2.set_aspect("equal")
    hist, xbins, ybins, im = ax2.hist2d(col_bottom, lin_bottom, bins=[8,8],vmin=0, vmax=v_max, cmap="YlOrRd")

    for a in range(len(ybins)-1):
        for b in range(len(xbins)-1):
            ax2.text(xbins[b]+0.5,ybins[a]+0.5, int(hist.T[a,b]), 
                    color="black", ha="center", va="center", fontsize = 'x-small')
            count_pads_bot.append(int(hist.T[b,a]))

    ax1.set_title("Top RPC ")
    ax2.set_title("Bottom RPC")

    ax1.set_xlabel('Line')
    ax1.set_ylabel('Column')
    ax2.set_xlabel ('Line')

    fig.suptitle("2D Pad Map of the RPCs - pre-process-linha1-colunas8-a-5.txt")
    plt.savefig(save_path)
    plt.show()
    return count_pads_top, count_pads_bot