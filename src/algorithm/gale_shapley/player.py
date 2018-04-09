from heapq import heappush


class Player:
    def __init__(self, name):
        self.teams = []
        self.engaged_with = None
        self.name = name

    def add(self, team, priority):
        heappush(self.teams, (priority, team))
        print 'algo'

    def is_unengaged(self):
        return self.engaged_with is None

    def engage_with_team(self, team):
        if self.engaged_with is not None:
            team.unengage_player_by_name(self)
        self.engaged_with = team

    def get_name(self):
        return name

