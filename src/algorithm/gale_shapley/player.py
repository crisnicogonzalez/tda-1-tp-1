from heapq import heappush
import logging

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
log_info = {'sort': 'Player'}


class Player:
    def __init__(self, name):
        self.priority_by_team_name = {}
        self.teams = []
        self.engaged_with = None
        self.name = name

    def add(self, team, priority):
        heappush(self.teams, (priority, team))
        self.priority_by_team_name[team.get_name()] = priority

    def is_unengaged(self):
        return self.engaged_with is None

    def engage_with_team(self, team):
        if self.engaged_with is not None:
            self.engaged_with.delete_player(self)
        logging.info('Relacionando el equipo {} con el jugador {}'.format(team.get_name(), self.name), extra=log_info)
        self.engaged_with = team

    def get_name(self):
        return self.name

    def team_has_more_priority(self,team_name):
        if self.engaged_with is None:
            return True
        priority_of_actual_team = self.priority_by_team_name[self.engaged_with.get_name()]
        priority_of_posible_team = self.priority_by_team_name[team_name]
        return priority_of_posible_team < priority_of_actual_team

