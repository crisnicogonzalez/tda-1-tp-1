from heapq import heappush


class Player:
    def __init__(self, name):
        self.teams = []
        self.engaged_with = None
        self.name = name

    def add(self, team, priority):
        heappush(self.teams, (priority, team))

    def is_unengaged(self):
        return self.engaged_with is None

    def engage_with_team(self, team):
        team.engage_with_player(self)
        if self.engaged_with is None:
            self.engaged_with = team
        else:
            self.delete_team_by_name(self.engaged_with.get_name())
            self.engaged_with = team

    def delete_team_by_name(self, team_name):
        #obtengo la referencia
        #la elimino de la lista
        # llamo
        team.delete_player_by_name(self.get_name())