import logging
import time

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Quick Sort'}


def select_pivote(list_to_sort):
    [a_pos, b_pos, c_pos] = take_sample(list_to_sort)
    logging.info('[{}, {}, {}]'.format(a_pos, b_pos,c_pos), extra=log_info)
    a = list_to_sort[a_pos]
    b = list_to_sort[b_pos]
    c = list_to_sort[c_pos]
    if a <= b and b >= c:
        return b_pos
    if b <= a and a >= c:
        return a_pos
    return c_pos


def take_sample(list_to_sort):
    if len(list_to_sort) < 3:
        return [0, 0, 0]
    piece_len = len(list_to_sort) / 3
    return list(map(lambda x: x*piece_len-1, range(1, 4)))


def sort(list_to_sort):
    start = time.time()
    len_list = len(list_to_sort)
    if len_list > 0:
        pivote_position = select_pivote(list_to_sort)
    end = time.time()
    logging.info('Tardo {} para {} elementos'.format(end-start, len_list), extra=log_info)













