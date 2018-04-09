from heapq import heappush,heappop


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

    def is_unengage(self):
        return self.number_of_players_engaged_with_me != self.number_of_players_i_want

    def engage_with_player(self, player):
        self.number_of_players_engaged_with_me += self.number_of_players_engaged_with_me + 1
        self.players_engaged_with_me.append(player)

    def unengage_player_by_name(self, player_name):
        # elimino de la lista de los que me interesan
        # elimino de la lista que estan conmigo
        #  actualizo la cantidad
        print('algo')

