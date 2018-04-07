import logging
import time

from src.utils.switch import switch

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Quick Sort'}


def calculate_pivote(list_to_sort):
    return len(list_to_sort) / 2


def sort_two_elements(list_to_sort):
    if list_to_sort[0] > list_to_sort[1]:
        switch(0, 1, list_to_sort)
    return list_to_sort


def recursive_sort(list_to_sort):
    logging.info('List to sort {}'.format(list_to_sort), extra=log_info)
    if len(list_to_sort) > 1:
        if len(list_to_sort) == 2:
            return sort_two_elements(list_to_sort)
        pivot_position = calculate_pivote(list_to_sort)
        pivot_value = list_to_sort[pivot_position]
        del list_to_sort[pivot_position]
        logging.info('List to sort sin el pivote {} pivote {}'.format(list_to_sort, pivot_value), extra=log_info)
        i = 0
        j = len(list_to_sort) - 1
        while i < j:
            if list_to_sort[i] > pivot_value and list_to_sort[j] <= pivot_value:
                switch(i, j, list_to_sort)
            if list_to_sort[i] < pivot_value:
                i += 1
            if list_to_sort[j] >= pivot_value:
                j -= 1
        logging.info('I es {}'.format(i), extra=log_info)
        if i == j:
            logging.info('I y J son iguales!!!!', extra=log_info)
        else:
            logging.info('I y J se cruzaron !!!!', extra=log_info)
        medium = i+1
        if list_to_sort[i] > pivot_value:
            medium = i
        left = list_to_sort[:medium]
        right = list_to_sort[medium:]
        logging.info('Left {}'.format(left), extra=log_info)
        logging.info('Right {}'.format(right), extra=log_info)
        logging.info('Como quedo dividido {} + [{}] + {}'.format(left,pivot_value, right), extra=log_info)
        left_sorted = recursive_sort(left)
        logging.info('Left sorted {}'.format(left_sorted), extra=log_info)
        return left_sorted + [pivot_value] + recursive_sort(right)
    return list_to_sort


def sort(list_to_sort):
    sorted_list = recursive_sort(list_to_sort)
    return sorted_list











