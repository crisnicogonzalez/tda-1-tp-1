from heapq import heappush, heappop
import logging

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Team'}


class Team:
    def __init__(self, name, numbers_of_players=3):
        self.number_of_players_i_want = numbers_of_players
        self.players = []
        self.players_engaged_with_me = []
        self.name = name

    def add(self, player, priority):
        heappush(self.players, (priority, player))

    def get_priority_player(self):
        if len(self.players) > 0:
            return heappop(self.players)[1]
        return None

    def is_incomplete(self):
        return len(self.players_engaged_with_me) < self.number_of_players_i_want

    def engage_with_player(self, player):
        self.players_engaged_with_me.append(player)

    def delete_player(self, player):
        logging.info('Eliminando relacion entre el equipo {} y el jugador {}'.format(self.name, player.get_name()), extra=log_info)
        i = 0
        aux_player = self.players_engaged_with_me[i]
        while aux_player.get_name() != player.get_name() and i < len(self.players_engaged_with_me):
            aux_player = self.players_engaged_with_me[i]
            i += 1
        if aux_player.get_name() == player.get_name():
            del self.players_engaged_with_me[i-1]

    def get_name(self):
        return self.name


