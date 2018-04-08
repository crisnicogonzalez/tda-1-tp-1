from heapq import heappush,heappop


class Team:
    def __init__(self):
        self.number_of_players_i_want = 20
        self.players = []
        self.number_of_players_engaged_with_me = 0
        self.players_engaged_with_me = []

    def add_player(self, player, priority):
        heappush(self.players, (priority, player))

    def get_priority_player(self):
        if len(self.players) > 0:
            return heappop(self.players)
        return None

    def engage_with_player(self, player):
        self.number_of_players_engaged_with_me += self.number_of_players_engaged_with_me +1
        self.players_engaged_with_me.append(player)

    def is_ungaged(self):
        return self.number_of_players_engaged_with_me == self.number_of_players_i_want
