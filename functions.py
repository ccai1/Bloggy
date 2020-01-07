def checkApos(string):
    '''Fixes strings with apostrophers'''
    i = -1
    aposIndexes = []
    while True:
        i = string.find("'", i + 1)
        if i == -1: break
        aposIndexes.append(i)
    j = 0
    for index in aposIndexes:
        string = string[:index +j ] + "'" + string[index+ j:]
        j += 1
    return string
