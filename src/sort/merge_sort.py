from src.utils.switch import switch


def merge_sort_recusive(list_to_sort, first_position, last_position):
    len_list_to_sort = abs(first_position - last_position) + 1
    if len_list_to_sort > 1:
        medium = first_position + len_list_to_sort / 2
        merge_sort_recusive(list_to_sort, first_position, medium)
        merge_sort_recusive(list_to_sort, medium + 1, last_position)
        i = last_position
        j = medium + 1
        while i <= medium and j <= last_position:
            if list_to_sort[i] < list_to_sort[j]:
                i += 1
            else:
                switch(i, j, list_to_sort)
                i += 1

