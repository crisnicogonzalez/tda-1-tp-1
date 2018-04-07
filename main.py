import logging
import random

FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'service': 'Main'}


def generate_random_numbers_set():
    logging.info('Generando el conjunto de numeros randoms', extra=log_info)
    sets = []
    quantity_sets = 5
    limit = 50000
    for i in range(0, quantity_sets):
        set = []
        logging.info('Generando el conjunto {}'.format(i), extra=log_info)
        for x in range(0, limit):
            set.append(random.randint(0, limit))
        sets.append(set)
    return sets


def run():
    logging.info('Iniciando punto 1 item b del TP', extra=log_info)
    sets = generate_random_numbers_set()
    return True

if __name__ == '__main__':
    run()