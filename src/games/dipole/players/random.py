from random import randint
from random import random

from games.dipole.action import DipoleAction
from games.dipole.player import DipolePlayer
from games.dipole.state import DipoleState
from games.state import State


class RandomDipolePlayer(DipolePlayer):
    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: DipoleState):
        no_moves_left = state.no_valid_moves_left()
        if random() < 0.1 or no_moves_left:  # probabilidade de passar 10%
            return DipoleAction(-1, -1, True)  # Ação de passar o turno
        else:
            while True:
                action = DipoleAction(randint(0, state.get_num_cols() - 1), randint(0, state.get_num_rows() - 1))
                if state.validate_action(action):
                    return action

    def event_action(self, pos: int, action, new_state: State):
        pass

    def event_end_game(self, final_state: State):
        pass
