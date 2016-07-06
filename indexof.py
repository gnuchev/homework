def indexof(listofnames, value):
    if value in listofnames:
        value_index = listofnames.index(value)
        return(listofnames, value_index)
    else: return(-1)
