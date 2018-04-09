import logging

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Gale Shapley'}


def gale_shapley(teams):
    while if_there_is_a_free_team(teams):
        team = get_free_team(teams)
        player = team.get_priority_player()
        if player.is_unengaged() or player.team_has_more_priority(team.get_name()):
            player.engage_with_team(team)
            team.engage_with_player(player)


def if_there_is_a_free_team(teams):
    for team in teams:
        if team.is_incomplete():
            return True
    return False


def get_free_team(teams):
    for team in teams:
        if team.is_incomplete():
            return team
    return None