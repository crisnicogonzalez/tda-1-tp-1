from src.algorithm.gale_shapley.player import Player
from src.algorithm.gale_shapley.team import Team


def factory(players_name, teams_name):
    players, teams = create_instances(players_name, teams_name)
    players_draft = up_draft(players_name, 'jugador')
    teams_draft = up_draft(teams_name, 'equipo')
    relationate(players_draft, players)
    relationate(teams_draft, teams)


def relationate(draft, instances_dict, other_instances_dict):
    for instance_name in draft:
        draft_instance = draft_dict[instance_name]
        instance = instances_dict[instance_name]
        for position in range(0, len(draft_instance)):
            instance.add(other_instances_dict[draft_instance[position]],position)


def create_instances(players_name, teams_name):
    players = {}
    teams = {}
    for player_name in players_name:
        players[player_name] == Player(player_name)
    for team_name in teams_name:
        teams[team_name] = Team(team_name)
    return players, teams


def exist_file_by_name(file_name):
    return True


def up_file_by_name(file_name):
    return False


def format_file(file):
    return []


def up_draft(names, key_word_file):
    draft = {}
    for name in names:
        file_name = '{}_[{}]'.format(key_word_file, players_name)
        if exist_file_by_name(file_name):
            file = up_file_by_name(file_name)
            draft[name] = format_file(file)
    return draft
