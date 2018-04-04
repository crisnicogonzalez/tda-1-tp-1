

# Dada una lista y 2 posiciones,hace el cambio de valores
# switch(0,1,[1,2,3]) -> [2,1,3]
def switch(x, y, list_to_switch):
    x_value = list_to_switch[x]
    list_to_switch[x] = list_to_switch[y]
    list_to_switch[y] = x_value