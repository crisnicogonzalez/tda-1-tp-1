import logging
import time

from src.utils.switch import switch

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Quick Sort'}


def calculate_pivote(list_to_sort):
    return len(list_to_sort) / 2


def calculate_naive_pivote(list_to_sort):
    return 0


def sort_two_elements(list_to_sort):
    if list_to_sort[0] > list_to_sort[1]:
        switch(0, 1, list_to_sort)
    return list_to_sort


def recursive_sort(list_to_sort, pivot_selector=calculate_pivote):
    logging.debug('List to sort {}'.format(list_to_sort), extra=log_info)
    if len(list_to_sort) > 1:
        if len(list_to_sort) == 2:
            return sort_two_elements(list_to_sort)
        pivot_position = pivot_selector(list_to_sort)
        pivot_value = list_to_sort[pivot_position]
        del list_to_sort[pivot_position]
        logging.debug('List to sort sin el pivote {} pivote {}'.format(list_to_sort, pivot_value), extra=log_info)
        i, j = 0, len(list_to_sort)-1
        while i < j:
            if list_to_sort[j] <= pivot_value < list_to_sort[i]:
                switch(i, j, list_to_sort)
                i+=1
                j-=1
            elif list_to_sort[i] <= pivot_value: i += 1
            elif list_to_sort[j] >= pivot_value: j -= 1
        medium = i+1
        if list_to_sort[i] > pivot_value: medium = i
        return recursive_sort(list_to_sort[:medium]) + [pivot_value] + recursive_sort(list_to_sort[medium:])
    return list_to_sort


def sort(list_to_sort):
    sorted_list = recursive_sort(list_to_sort)
    return sorted_list


def naive_quick_sort(list_to_sort):
    sorted_list = recursive_sort(list_to_sort,calculate_naive_pivote)
    return sorted_list




