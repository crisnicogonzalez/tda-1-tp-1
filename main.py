import logging
import random
import time
import numpy as np
import matplotlib.pyplot as plt

from src.sort.merge_sort import sort as merge_sort
from src.sort.quick_sort import sort as quick_sort
from src.sort.insertion_sort import sort as insertion_sort


sorters = {
    'quick_sort': quick_sort,
    'merge_sort': merge_sort,
    'insertion_sort': insertion_sort
}


FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Main'}

limit = 10000


def generate_random_numbers_set():
    logging.info('Generando el conjunto de numeros randoms', extra=log_info)
    sets = []
    quantity_sets = 10
    set = []
    for i in range(0, quantity_sets):
        logging.info('Generando el conjunto {}'.format(i), extra=log_info)
        for x in range(0, limit):
            set.append(random.randint(0, limit))
        sets.append(set)
    return sets


def wrapper(list_to_sort, sort):
    start = time.time()
    sort(list_to_sort)
    end = time.time()
    return end-start


def initialize_results_dict(set_lens):
    results = {}
    for set_len in set_lens:
        results[set_len] = {}
        for key_sort in sorters:
            results[set_len][key_sort] = []
    return results


def calculate_mean_time_for_every_sort(results):
    variance_and_mean_times = {}
    for len_set in results:
        variance_and_mean_times[len_set] = {}
        for key_sort in results[len_set]:
            execution_times = results[len_set][key_sort]
            variance_and_mean_times[len_set][key_sort] = {
                'mean': np.mean(execution_times),
            }
    return variance_and_mean_times


def test_sorts(sets):
    set_lens = [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]
    results = initialize_results_dict(set_lens)
    for key_sort in sorters:
        sort = sorters[key_sort]
        for set in sets:
            for set_len in set_lens:
                logging.info('Algoritmo {} para {} elementos'.format(key_sort, set_len), extra=log_info)
                testing_set = set[:set_len]
                ejecution_time = wrapper(testing_set, sort)
                results[set_len][key_sort].append(ejecution_time)
    return results


def grafic_average():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    plt.plot([1, 2, 3, 6], [1, 4, 9, 18], 'ro')
    plt.axis([0, 6, 0, 20])
    plt.show()


def run():
    logging.info('Iniciando punto 1 item b del TP', extra=log_info)
    sets = generate_random_numbers_set()
    logging.info('Iniciando punto 1 item c del TP', extra=log_info)
    results = test_sorts(sets)
    logging.info('Iniciando punto 1 item d del TP', extra=log_info)
    averages_and_variances = calculate_mean_time_for_every_sort(results)
    print averages_and_variances
    grafic_average()
    print results



if __name__ == '__main__':
    run()