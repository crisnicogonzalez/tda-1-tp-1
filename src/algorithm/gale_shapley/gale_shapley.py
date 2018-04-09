def gale_shapley(teams, players):
    while if_there_is_a_free_team(teams):
        team = get_free_team(teams)
        player = team.get_priority_player()
        if player.is_unengaged() or player.team_has_more_priority(team.getName()):
            player.engage_with_team(team)
        else:
            player.delete_team(team.getName())
    print_result(teams, players)


def print_result(teams, players):
    print 'algo'


def if_there_is_a_free_team(teams):
    for team in teams:
        if team.is_unengage():
            return True
    return False


def get_free_team(teams):
    for team in teams:
        if team.is_unengage():
            return team
    return None