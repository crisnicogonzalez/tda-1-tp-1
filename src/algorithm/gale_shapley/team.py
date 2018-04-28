from heapq import heappush, heappop
import logging

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Team'}


class Team:
    def __init__(self, name, numbers_of_players=3):
        self.number_of_players_i_want = numbers_of_players
        self.players = []
        self.players_engaged_with_me = {}
        self.name = name
        self.teams_set = None

    def add(self, player, priority):
        heappush(self.players, (priority, player))

    def get_priority_player(self):
        if len(self.players) > 0:
            return heappop(self.players)[1]
        return None

    def is_incomplete(self):
        return len(self.players_engaged_with_me) < self.number_of_players_i_want

    def engage_with_player(self, player):
        self.players_engaged_with_me[player.get_name()] = player

    def delete_player(self, player):
        logging.info('Eliminando relacion entre el equipo {} y el jugador {}'.format(self.name, player.get_name()), extra=log_info)
        self.players_engaged_with_me.pop(player.get_name(), None)
        self.teams_set.add(self)

    def get_name(self):
        return self.name

    def set_teams_queue(self, set_team):
        self.teams_set = set_team


