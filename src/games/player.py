from abc import ABC, abstractmethod

from games.state import State


class Player(ABC):  # Cria diferentes tipos de jogadores num jogo
    # contém métodos abstratos que devem ser implementados por qualquer classe herdada dela

    """
    :param name: name of the player (simply a text identifier for the player)
    """

    def __init__(self, name):
        self.__name = name
        self.__current_pos = None

    """
    retrieves the name of the player
    """

    def get_name(self):
        return self.__name

    """
    retrieves the current position of the player
    """

    def get_current_pos(self):
        return self.__current_pos

    """
    sets the current position of the player
    :param new_pos: the new position
    """

    def set_current_pos(self, new_pos):
        self.__current_pos = new_pos

    """
    prints to the console the stats of the player
    """
    @abstractmethod
    def print_stats(self):
        pass

    """
    Method that returns an action for a certain game state
    :param state: the current game state
    """
    # retorna a ação que o jogador deseja executar, dado o estado atual do jogo.
    @abstractmethod
    def get_action(self, state):
        pass

    """
    A method that is invoked once a new game starts
    """
    @abstractmethod
    def event_new_game(self):
        pass

    """
    A method that notifies the player that someone did a certain action. This can be used to log opponents actions
    :param pos: the position of the player that performed the action
    :param action: the action that was performed
    :param new_state: the resulting game state
    """
    # notifica o jogador que um jogador na posição pos executou uma ação e mudou o estado do jogo para new_state
    @abstractmethod
    def event_action(self, pos: int, action, new_state: State):
        pass

    """
    A method that notifies the player of a game result of a given player
    :param pos: the position of the player that got the result
    :param result: the result of the player
    """
    # notifica o jogador que um jogador na posição pos recebeu um resultado de resultado
    @abstractmethod
    def event_result(self, pos: int, result):
        pass

    """
    A method that notifies the player that a game has ended
    :param final_state: the final state of the game
    """
    @abstractmethod
    def event_end_game(self, final_state: State):
        pass
