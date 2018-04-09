from heapq import heappush, heappop


class Team:
    def __init__(self, name):
        self.number_of_players_i_want = 20
        self.players = []
        self.number_of_players_engaged_with_me = 0
        self.players_engaged_with_me = []
        self.name = name

    def add(self, player, priority):
        heappush(self.players, (priority, player))

    def get_priority_player(self):
        if len(self.players) > 0:
            return heappop(self.players)[1]
        return None

    def is_incomplete(self):
        return len(self.players_engaged_with_me) != self.number_of_players_i_want

    def engage_with_player(self, player):
        self.players_engaged_with_me.append(player)

    def delete_player_of_players(self,player):
        i = 0
        aux_player = self.players[i][1]
        while aux_player.get_name() != player.get_name():
            i += 1
            aux_player = self.players[i][1]
        del self.players[i]
        i = 0
        aux_player = self.players_engaged_with_me[i]
        while aux_player.get_name() != player.get_name():
            i += 1
            aux_player = self.players_engaged_with_me[i]
        del self.players_engaged_with_me[i]


