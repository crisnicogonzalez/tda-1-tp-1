import sys

this = sys.modules[__name__]
this.environment = 'MINIMAL'

my_config = {
    'MINIMAL': {
        'numbers_of_players': 12,
        'numbers_of_teams': 2,
        'need_to_complete': 6,
        'run_point_one': False,
        'run_point_two': True,
    },
    'PROD': {
        'numbers_of_players': 200,
        'numbers_of_teams': 20,
        'need_to_complete': 10,
        'run_point_one': True,
        'run_point_two': True
    },
    'MEDIUM': {
        'numbers_of_players': 100,
        'numbers_of_teams': 10,
        'need_to_complete': 10,
        'run_point_one': False,
        'run_point_two': True
    },
    'PROD_SHAPLEY': {
        'numbers_of_players': 200,
        'numbers_of_teams': 20,
        'need_to_complete': 10,
        'run_point_one': False,
        'run_point_two': True
    },
    'PROD_SORT': {
        'numbers_of_players': 200,
        'numbers_of_teams': 20,
        'need_to_complete': 10,
        'run_point_one': True,
        'run_point_two': False
    },
}


def set_environment(env):
    this.environment = env


def get_value_of_key(key):
    return my_config[this.environment][key]
