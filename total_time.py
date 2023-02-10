def total_time(file:str):

    "Returns the total time in seconds"

    arquivo = open(file, "r")
    lines = arquivo.readlines()
    totalTime = 0
    for data in lines:
        totalTime +=int(data)
    

    return totalTime/10**6
