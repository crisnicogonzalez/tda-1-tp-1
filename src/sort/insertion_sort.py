import logging
import time

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Insertion Sort'}


def sort(list_to_sort):
    logging.debug('La lista originalmente {}'.format(list_to_sort), extra=log_info)
    len_list = len(list_to_sort)
    for pivote in range(1, len_list):
        pivote_value = list_to_sort[pivote]
        logging.debug('La posicion pivote es {} y el valor es {}'.format(pivote, pivote_value), extra=log_info)
        x = pivote - 1
        x_value = list_to_sort[x]
        logging.debug('X {} X value {}'.format(x, x_value), extra=log_info)
        while pivote_value < x_value and x >= 0:
            x = x - 1
            x_value = list_to_sort[x]
            logging.debug('X {} X value {}'.format(x, x_value), extra=log_info)
        if pivote_value >= x_value and x != pivote -1:
            logging.debug('insertar en la posicion {} el valor {}'.format(x+1, pivote_value), extra=log_info)
            list_to_sort.insert(x+1, pivote_value)
            del list_to_sort[pivote+1]
        logging.debug('La lista {}'.format(list_to_sort), extra=log_info)
    return list_to_sort

