from heapq import heappush
import logging

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Team'}


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
        if self.engaged_with is not None:
            team.delete_player(self)
        logging.info('Relacionando el equipo {} con el jugador {}'.format(team.get_name(), self.name), extra=log_info)
        self.engaged_with = team

    def get_name(self):
        return name

