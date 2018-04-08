import logging
import time

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
log_info = {'sort': 'Insertion Sort'}


def sort(list_to_sort):
    logging.debug('La lista originalmente {}'.format(list_to_sort), extra=log_info)
    for i in range(1, len(list_to_sort)):
        j = i
        pivot_value = list_to_sort[j]
        while j-1 >= 0 and list_to_sort[j-1] > pivot_value:
            list_to_sort[j] = list_to_sort[j-1]
            j -= 1
        list_to_sort[j] = pivot_value
    return list_to_sort
