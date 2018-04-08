import logging
import time
import numpy as np

from src.sort.merge_sort import sort as merge_sort
from src.sort.quick_sort import sort as quick_sort,naive_quick_sort
from src.sort.insertion_sort import sort as insertion_sort
from src.utils.generator_numbers import *

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


def print_result_of_sort(result):
    for x in result:
        print '{},{}'.format(x, result[x][0])


def print_sort_name_and_time(averages):
    for sort_name in averages:
        print sort_name
        for set_len in set_lens:
            print('{0:10},{1:10f}'.format(set_len, averages[sort_name][set_len]))


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


def run_merge_sort_wort_case():
    logging.info('Merge sort', extra=log_info)
    wort_set_for_merge_sort = generate_numbers_for_merge_sort_wort_case(10000)
    normal_set_for_merge_sort = generate_random_numbers_set(10000, 10)
    result_merge_sort_wort_case = test_sort(wort_set_for_merge_sort, merge_sort)
    result_merge_sort_normal_case = test_sort(normal_set_for_merge_sort, merge_sort)
    print_sort_name_and_time(calculate_mean_time_for_every_sort({'merge_sort_wort_case': result_merge_sort_wort_case}))
    print_sort_name_and_time(calculate_mean_time_for_every_sort({'merge_sort_normal_case': result_merge_sort_normal_case}))


def run_insertion_sort_wort_case():
    logging.info('Insertion sort', extra=log_info)
    wort_set_for_insertion_set = generate_numbers_in_orden(10000)
    normal_set_for_insertion_set = generate_random_numbers_set(10000, 10)
    result_insertion_sort_wort_case = test_sort(wort_set_for_insertion_set, insertion_sort)
    result_insertion_sort_normal_case = test_sort(normal_set_for_insertion_set, insertion_sort)
    print_sort_name_and_time(
        calculate_mean_time_for_every_sort({'insertion_sort_wort_case': result_insertion_sort_wort_case}))
    print_sort_name_and_time(
        calculate_mean_time_for_every_sort({'insertion_sort_normal_case': result_insertion_sort_normal_case}))


def run():
    logging.info('Iniciando punto 1 item b del TP', extra=log_info)
    sets = generate_random_numbers_set(10000, 10)

    logging.info('Iniciando punto 1 item c del TP', extra=log_info)
    results = test_sorts(sets)

    logging.info('Iniciando punto 1 item d del TP', extra=log_info)
    execution_time_average = calculate_mean_time_for_every_sort(results)
    print_sort_name_and_time(execution_time_average)

    logging.info('Iniciando punto 1 item f del TP', extra=log_info)
    run_insertion_sort_wort_case()
    run_merge_sort_wort_case()
    





if __name__ == '__main__':
    run()