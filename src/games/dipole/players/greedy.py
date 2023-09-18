from random import choice
from games.dipole.action import DipoleAction
from games.dipole.player import DipolePlayer
from games.dipole.state import DipoleState
from games.state import State


class GreedyDipolePlayer(DipolePlayer):
    def __init__(self, name):
        self.action_count = 0
        super().__init__(name)

    def get_action(self, state: DipoleState):
        self.action_count += 1

        if self.action_count > 15:
            return DipoleAction(is_pass=True)

        valid_actions = []
        capturing_actions = []

        for i in range(state.get_num_rows()):
            for j in range(state.get_num_cols()):
                action = DipoleAction(i, j)
                if state.validate_action(action):
                    new_state = state.clone()
                    new_state.update(action)
                    
                    opponent = 1 if state.get_acting_player() == 0 else 0
                    captured_count = new_state._count_captured_pieces(state.get_acting_player())
                    
                    if captured_count > 0:
                        capturing_actions.append(action)
                    else:
                        valid_actions.append(action)

        if len(capturing_actions) > 0:
            print(f"Player {state.get_acting_player()} selecionou uma ação de captura: {action.get_row()}, {action.get_col()}")
            return choice(capturing_actions)
        elif len(valid_actions) > 0:
            return choice(valid_actions)
        else:
            return DipoleAction(is_pass=True)

    def event_new_game(self):
        super().event_new_game()
        self.action_count = 0
    
    def event_action(self, pos: int, action, new_state: State):
        pass

    def event_end_game(self, final_state: State):
        pass