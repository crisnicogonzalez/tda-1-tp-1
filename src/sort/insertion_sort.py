import logging
import time

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Insertion Sort'}


def sort(list_to_sort):
    start = time.time()
    len_list = len(list_to_sort)
    for pivote in range(1, len_list):
        pivote_value = list_to_sort[pivote]
        for x in range(pivote, -1, -1):
            x_value = list_to_sort[x]
            if x_value < pivote_value:
                list_to_sort.insert(x+1, pivote_value)
                del list_to_sort[pivote+1]
            break
    end = time.time()
    logging.info('Tardo {} para {} elementos'.format(end-start, len_list), extra=log_info)


