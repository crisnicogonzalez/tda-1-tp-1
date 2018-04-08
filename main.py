import logging
import time
import numpy as np

from src.sort.merge_sort import sort as merge_sort
from src.sort.quick_sort import sort as quick_sort
from src.sort.insertion_sort import sort as insertion_sort
from src.utils.generator_numbers import generate_random_numbers_set,generate_numbers_in_orden


sorters = {
    'quick_sort': quick_sort,
    'merge_sort': merge_sort,
    'insertion_sort': insertion_sort
}


FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Main'}

set_lens = [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]


def wrapper(list_to_sort, sort):
    start = time.time()
    sort(list_to_sort)
    end = time.time()
    return end-start


def initialize_results_dict():
    result = {}
    for set_len in set_lens:
        result[set_len] = []
    return result


def print_sort_name_and_time(averages):
    for sort_name in averages:
        print sort_name
        for set_len in set_lens:
            print('{},{}'.format(set_len, averages[sort_name][set_len]))


def calculate_mean_time_for_every_sort(results):
    execution_time_averages = {}
    for sort_name in results:
        execution_time_averages[sort_name] = {}
        for set_len in set_lens:
            execution_time_averages[sort_name][set_len] = np.mean(results[sort_name][set_len])
    return execution_time_averages


def test_sorts(sets):
    results = {}
    for key_sort in sorters:
        sort = sorters[key_sort]
        logging.info('{}'.format(key_sort), extra=log_info)
        result = test_sort(sets, sort)
        results[key_sort] = result
    return results


def test_sort(sets, sort):
    results = initialize_results_dict()
    for set_len in set_lens:
        logging.info('Ordenando el set de {} elementos'.format(set_len), extra=log_info)
        for set in sets:
            testing_set = set[:set_len]
            execution_time = wrapper(testing_set, sort)
            results[set_len].append(execution_time)
    return results


def run():
    logging.info('Iniciando punto 1 item b del TP', extra=log_info)
    sets = generate_random_numbers_set(10000, 10)

    logging.info('Iniciando punto 1 item c del TP', extra=log_info)
    results = test_sorts(sets)

    logging.info('Iniciando punto 1 item d del TP', extra=log_info)
    execution_time_average = calculate_mean_time_for_every_sort(results)
    print execution_time_average
    print_sort_name_and_time(execution_time_average)

    logging.info('Iniciando punto 1 item f del TP', extra=log_info)
    logging.info('Generando peor set para insertion sort', extra=log_info)
    set_ordered = generate_numbers_in_orden(10000)
    result_insertion_sort = test_sort([set_ordered], insertion_sort)
    print result_insertion_sort
    # print results


if __name__ == '__main__':
    run()