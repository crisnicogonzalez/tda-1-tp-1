import random
import os


def create_drafts(env='MINIMAL'):
    players_names = get_players_names(env)
    teams_names = get_teams_names(env)
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


def get_players_names(env='HIGHT'):
    if env == 'MEDIUM':
        return range(1, 101)
    elif env == 'MINIMAL':
        return range(1, 21)
    elif env == 'HIGHT':
        return range(1, 201)


def get_teams_names(env='HIGHT'):
    if env == 'MEDIUM':
        return range(1, 5)
    elif env == 'MINIMAL':
        return range(1, 3)
    elif env == 'HIGHT':
        return range(1, 21)