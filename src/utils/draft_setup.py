import random
import os
from src.config.config import get_value_of_key


def create_drafts():
    players_names = get_players_names()
    teams_names = get_teams_names()
    create(teams_names, players_names, 'teams', 'equipo')
    create(players_names, teams_names, 'players', 'jugador')


def create(first_set, second_set, package, key_name_file):
    for player_name in first_set:
        file = open('src/files/gale_shapley/{}/{}_[{}].prf'.format(package, key_name_file, player_name), 'w')
        set_mix = random.sample(second_set, len(second_set))
        for team in set_mix:
            file.write(str(team)+'\n')
        file.close()


def delete_drafts():
    folder = 'src/files/gale_shapley'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


def get_players_names():
    return range(1, get_value_of_key('numbers_of_players')+1)


def get_teams_names():
    return range(1, get_value_of_key('numbers_of_teams')+1)
