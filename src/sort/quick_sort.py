import logging
import time

from src.sort.selection_sort import switch

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Quick Sort'}


def calculate_pivote(list_to_sort, first_position, last_position):
    if abs(first_position-last_position) == 2:
        return last_position - 1
    a = list_to_sort[first_position]
    b = list_to_sort[first_position + abs(last_position - first_position) / 2]
    c = list_to_sort[last_position]
    media = (a + b + c) / 3
    logging.info('Media calculada {}'.format(media), extra=log_info)
    a_distance_media = abs(a-media)
    b_distance_media = abs(b-media)
    c_distance_media = abs(c-media)
    if a_distance_media < b_distance_media and a_distance_media < c_distance_media:
        return 0
    if b_distance_media < a_distance_media and b_distance_media < c_distance_media:
        return len(list_to_sort)/2
    return len(list_to_sort)-1


def recursive_sort(list_to_sort, first_position, last_position):
    if first_position < last_position:
        logging.info('La lista se encuentra de esta manera {}'.format(list_to_sort), extra=log_info)
        logging.info('Desde la posicion first_position {} a last_position {}'.format(first_position, last_position), extra=log_info)
        i = first_position
        j = last_position
        pivote_position = calculate_pivote(list_to_sort, first_position, last_position)
        pivote_value = list_to_sort[pivote_position]
        logging.info('Pivote seleccionado en la posicion {} con valor {}'.format(pivote_position, pivote_value), extra=log_info)
        logging.info('i -> {} j -> {}'.format(i,j), extra=log_info)
        switches = {}
        somePointerAdvanced = True
        while i < j and somePointerAdvanced:
            logging.info('La lista se encuentra de esta manera {}'.format(list_to_sort), extra=log_info)
            i_advance = False
            j_advance = False
            if list_to_sort[i] > pivote_value:
                i += 1
                i_advance = True
                logging.info('i avanzo a {}'.format(i), extra=log_info)
            if list_to_sort[j] <= pivote_value:
                j -= 1
                j_advance = True
                logging.info('j retrocedio a {}'.format(j), extra=log_info)
            if i_advance and j_advance:
                logging.info('Switch entre {} y {}'.format(list_to_sort[i-1], list_to_sort[j+1]), extra=log_info)
                switch(i-1, j+1, list_to_sort)
                switches[i-1] = j+1
                switches[j+1] = i-1
            somePointerAdvanced = j_advance or i_advance
        logging.info('La lista se encuentra de esta manera {}'.format(list_to_sort), extra=log_info)
        recursive_sort(list_to_sort, first_position, i-2)
        recursive_sort(list_to_sort, i+1, last_position)


def sort(list_to_sort):
    start = time.time()
    recursive_sort(list_to_sort, 0, len(list_to_sort)-1)
    end = time.time()
    logging.info('Tardo {} para {} elementos'.format(end-start, len_list), extra=log_info)












