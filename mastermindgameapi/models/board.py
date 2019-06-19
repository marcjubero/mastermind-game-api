from mastermindgameapi.config.game_config import MAX_TURNS
from mastermindgameapi.models.exceptions import FinishedGameException
from mastermindgameapi.models.game import Game
from mastermindgameapi.models.guess import Guess


class Board:
    def __init__(self, game: Game = None, turns: list = None):
        self._game = game
        self._turns = turns

    def new_turn(self, guess: Guess):
        if len(self._turns) >= MAX_TURNS:
            raise FinishedGameException('Max number of turns ({0}) reached'.format(MAX_TURNS))

        if len(self._turns) and self._game.eval_guess(guess=self._turns[-1]).guessed():
            raise FinishedGameException('The color code was discovered on turn {0}'.format(len(self._turns)))

        return self._game.eval_guess(guess=guess).values
