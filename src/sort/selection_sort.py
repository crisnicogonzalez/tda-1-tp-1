def sort(list_to_sort):
    for pivote_position in range(0, len(list_to_sort)):
        less = list_to_sort[pivote_position]
        less_position = pivote_position
        for x in range(pivote, len(list_to_sort)):
            posible_less = list_to_sort[x]
            if posible_less < less:
                less = posible_less
                less_position = x
        if less_position != pivote_position:
            switch(pivote_position, less_position, list_to_sort)


# Dada una lista y 2 posiciones,hace el cambio de valores
# switch(0,1,[1,2,3]) -> [2,1,3]
def switch(x, y, list_to_switch):
    x_value = list_to_switch[x]
    list_to_switch[x] = list_to_switch[y]
    list_to_switch[y] = x_value
