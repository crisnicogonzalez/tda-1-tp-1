from src.utils.team_lib import get_teams_names
import random


def create_draf(env='PROD'):
    players_name = get_players_names(env)
    teams_name = get_teams_names(env)
    for player_name in players_name:
        file = open('jugador_[{}].prf'.format(player_name), 'w')
        random_draft(teams_name)
        for team in teams_name:
            file.write(team)
        file.close()


def random_draft(teams_name):
    random.sample(teams_name, len(teams_name))


def get_players_names(env='HIGHT'):
    if env == 'MEDIUM':
        return range(1, 101)
    elif env == 'MINIMAL':
        return range(1, 21)
    elif env == 'HIGHT':
        return range(1, 201)