from games.dipole.action import DipoleAction
from games.dipole.player import DipolePlayer
from games.dipole.state import DipoleState


class HumanDipolePlayer(DipolePlayer):
    def __init__(self, name):
        super().__init__(name)

    def get_user_input(self, choice_input: str) -> int:
        while True:
            try:
                user_input = input(choice_input)
                return int(user_input)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro válido.")

    def get_action(self, state: DipoleState):
        state.display()

        while True:
            choose_input = input("Digite 'p' para passar a jogada ou 'j' para fazer uma jogada: ")

            if choose_input.lower() == 'p':
                action = DipoleAction(is_pass=True)
            elif choose_input.lower() == 'j':
                x = self.get_user_input(f"Player {state.get_acting_player()}, escolha uma coluna: ")
                y = self.get_user_input(f"Player {state.get_acting_player()}, escolha uma linha: ")

                if x is not None and y is not None:
                    action = DipoleAction(x, y)
                else:
                    print("Introduziu um número para o tabuleiro inválido, tente novamente.")
                    continue
            else:
                print("Entrada inválida, tente novamente.")
                continue

            if state.validate_action(action):
                return action
            else:
                print("Jogada inválida, tente novamente.")

    def event_action(self, pos: int, action, new_state: DipoleState):
        pass

    def event_end_game(self, final_state: DipoleState):
        pass
