import logging
import time

from src.utils.switch import switch

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Selection Sort'}


def sort(list_to_sort):
    for pivote_position in range(0, len(list_to_sort)):
        less = list_to_sort[pivote_position]
        less_position = pivote_position
        for x in range(pivote_position, len(list_to_sort)):
            posible_less = list_to_sort[x]
            if posible_less < less:
                less = posible_less
                less_position = x
        if less_position != pivote_position:
            switch(pivote_position, less_position, list_to_sort)
    return list_to_sort


