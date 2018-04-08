import logging
import random

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Generator'}


def generate_random_numbers_set(number_of_elements, numbers_of_sets):
    logging.info('Generando conjunto de numeros randoms', extra=log_info)
    sets = []
    for i in range(0, numbers_of_sets):
        logging.info('Generando el conjunto {}'.format(i), extra=log_info)
        set = []
        for x in range(0, number_of_elements):
            set.append(random.randint(0, number_of_elements))
        sets.append(set)
    return sets


def generate_numbers_in_orden(size_limit, descending=True):
    if descending:
        return range(size_limit, 0, -1)
    return range(0, size_limit)


def generate_numbers_for_merge_sort_wort_case(numbers_of_elements, numbers_of_sets = 10):
    sets = []
    population = range(0, 10000)
    for number_set in range(0, numbers_of_sets):
        set = []
        for x in range(0, numbers_of_elements / 4):
            mini_set = random.sample(population, 4)
            mini_set.sort()
            set.extend([mini_set[2], mini_set[1], mini_set[3], mini_set[0]])
        sets.append(set)
    return sets