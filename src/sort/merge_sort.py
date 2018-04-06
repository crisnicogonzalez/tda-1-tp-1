
from src.utils.switch import switch

def sort_lists(first_list, second_list):
    i, j = 0, 0
    list_to_return = []
    while i < len(first_list) and j < len(second_list):
        i_value = first_list[i]
        j_value = second_list[j]
        if i_value < j_value:
            list_to_return.append(i_value)
            i += 1
        else:
            list_to_return.append(j_value)
            j += 1
    if j == len(second_list):
        return list_to_return.extend(first_list[i:])
    else:
        list_to_return.extend(second_list[j:])
    return list_to_return


def sort(list_to_sort):
    list_size = len(list_to_sort)
    if list_size <= 2:
        if list_size <= 1:
            return list_to_sort
        else:
            if list_to_sort[1] < list_to_sort[0]:
                switch(0, 1, list_to_sort)
                return list_to_sort
    else:
        medium = (list_size / 2)
        list_right = sort(list_to_sort[:medium])
        list_left = sort(list_to_sort[medium:])
        return sort_lists(list_right, list_left)



