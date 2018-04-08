from heapq import heappush


class Player:
    def __init__(self):
        self.teams = []
        self.engaged_with = None

    def add_team(self, team, priority):
        heappush(self.teams, (priority, team))

    def is_unengaged(self):
        return self.engaged_with is None

    def engage_with_team(self, team):
        team.engage_with_player(self)
        self.engaged_with = team