
def swapPosition(list,pos1,pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

list = [23,22,24,34,45,56]
pos1,pos2 = 1, 3

print(swapPosition(list, pos1-1, pos2-1))
