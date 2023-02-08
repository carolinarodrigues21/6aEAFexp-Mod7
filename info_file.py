def getNpad(filename):
    '''Returns the number of the pad of a RPC that a muon hit, considering the bottom and the top RPC. 
    It returns also the number of the event (hit).
    '''
    nPads_RPC1, nPads_RPC2, Nevento = [], [], []
    with open(filename) as file:
        for line in file:
            str_line = str(line)
            col_list = str_line.split()
            nPads_RPC1.append(col_list[0].find("1")+1)
            nPads_RPC2.append(col_list[1].find("1")+1)
            Nevento.append(col_list[2])
    
    return nPads_RPC1, nPads_RPC2, Nevento

def LineColPad(Npad):
    "Returns the line and column of a pad"
    if Npad%8 == 0:
        col = Npad/8
        line = 8
    else:
        col = Npad//8 + 1
        line = Npad%8
    return line,col

def getINFO(filename):
    '''Main function that returns a list of the numbers of the pad that happend a hit of a RPC at the top and at the bottom. 
    It also returns a list with the line and column of those pads.
    '''
    Npad_top, Npad_bot, Nevento = getNpad(filename)
    line_top, col_top = [], []
    line_bot, col_bot = [], []
    azi, zen = [], []

    for i in range(len(Npad_top)):
        line1, col1 = LineColPad(Npad_top[i])
        line2, col2 = LineColPad(Npad_bot[i])

        line_top.append(line1)
        line_bot.append(line2)
        col_top.append(col1)
        col_bot.append(col2)
        
    return Npad_top, Npad_bot, line_top, col_top, line_bot, col_bot