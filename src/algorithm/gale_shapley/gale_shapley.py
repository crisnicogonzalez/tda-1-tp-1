import logging
FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Gale Shapley'}


def gale_shapley(instance_teams_by_name):
    set_teams_instance = create_set(instance_teams_by_name)
    while len(set_teams_instance) != 0:
        team = set_teams_instance.pop()
        player = team.get_priority_player()
        if player.is_unengaged() or player.team_has_more_priority(team.get_name()):
            player.engage_with_team(team)
            team.engage_with_player(player)
        if team.is_incomplete():
            set_teams_instance.add(team)


def create_set(instance_teams_by_name):
    my_set = set()
    for name in instance_teams_by_name:
        team = instance_teams_by_name[name]
        team.set_teams_queue(my_set)
        my_set.add(team)
    return my_set
