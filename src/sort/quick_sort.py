import logging
import time

from src.sort.selection_sort import switch

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Quick Sort'}


def select_pivote(list_to_sort, first_position, last_position):
    a = list_to_sort[first_position]
    b = list_to_sort[first_position + (last_position - first_position) / 2]
    c = list_to_sort[last_position]
    media = a + b + c / 3
    a_distance_media = abs(a-media)
    b_distance_media = abs(b-media)
    c_distance_media = abs(c-media)
    if a_distance_media < b_distance_media and a_distance_media < c_distance_media:
        return 0
    if b_distance_media < a_distance_media and b_distance_media < c_distance_media:
        return len(list_to_sort)/2
    return len(list_to_sort)-1


def recursive_sort(list_to_sort, first_position, last_position):
    pivote_position = select_pivote(list_to_sort, first_position, last_position)
    pivote_value = list_to_sort[pivote_position]
    i = first_position
    j = last_position
    switches = {}
    while i < j:
        i_advance = False
        j_advance = False
        if list_to_sort[i] > pivote_value:
            i += 1
            i_advance = True
        if list_to_sort[j] < pivote_value:
            j += 1
            j_advance = True
        if i_advance and j_advance:
            switch(list_to_sort, i-1, j-1)
            switches[i-1] = j-1
            switches[j-1] = i-1
    switch(switches[pivote_position, switches[pivote_position]])
    recursive_sort(list_to_sort, first_position, i-1)
    recursive_sort(list_to_sort, i+1, last_position)

def sort(list_to_sort):
    start = time.time()
    recursive_sort(list_to_sort, 0, len(list_to_sort))
    end = time.time()
    logging.info('Tardo {} para {} elementos'.format(end-start, len_list), extra=log_info)












