import logging
import math
import random

from src.utils.switch import switch

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Generator'}


def generate_random_numbers_set(number_of_elements=10000, numbers_of_sets=10):
    logging.info('Generando conjunto de numeros randoms', extra=log_info)
    sets = []
    for i in range(0, numbers_of_sets):
        logging.info('Generando el conjunto {}'.format(i), extra=log_info)
        set = []
        for x in range(0, number_of_elements):
            set.append(random.randint(0, number_of_elements))
        sets.append(set)
    return sets


def generate_numbers_in_orden(number_of_elements=10000, number_of_sets=10, descending=True):
    sets = []
    for x in range(0, number_of_sets):
        if descending:
             sets.append(range(number_of_elements, 0, -1))
        else:
            sets.append(range(0, number_of_elements))
    return sets


def generate_numbers_for_merge_sort_wort_case(number_of_elements=10000, number_of_sets=10):
    sets = []
    population = range(0, 10000)
    for number_set in range(0, number_of_sets):
        set = []
        for x in range(0, number_of_elements / 4):
            mini_set = random.sample(population, 4)
            mini_set.sort()
            set.extend([mini_set[2], mini_set[1], mini_set[3], mini_set[0]])
        sets.append(set)
    return sets


def generate_numbers_for_quick_sort_wort_case(number_of_elements=10000, number_of_sets=10):
    return generate_numbers_in_orden(number_of_elements, number_of_sets)