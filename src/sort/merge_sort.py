import logging
import time

from src.utils.switch import switch

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Merge Sort'}


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
        list_to_return.extend(first_list[i:])
    else:
        list_to_return.extend(second_list[j:])
    return list_to_return


def merge_sort(list_to_sort):
    logging.info('List to sort {}'.format(list_to_sort), extra=log_info)
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
        list_right = merge_sort(list_to_sort[:medium])
        list_left = merge_sort(list_to_sort[medium:])
        logging.info('Right list {} Left list {}'.format(list_right, list_left), extra=log_info)
        list_sorted =  sort_lists(list_right, list_left)
        logging.info('List sorted'.format(list_sorted), extra=log_info)
        return list_sorted


def sort(list_to_sort):
    start = time.time()
    list_to_return = merge_sort(list_to_sort)
    end = time.time()
    logging.info('Tardo {} para {} elementos'.format(end-start, len(list_to_sort)), extra=log_info)
    return list_to_return
