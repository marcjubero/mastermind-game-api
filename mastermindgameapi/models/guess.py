from mastermindgameapi.config.game_config import GUESS_LENGTH
from mastermindgameapi.models.exceptions import InvalidGuessLength


class Guess:
    def __init__(self, values: list) -> None:
        # TODO 2019-06-16 check input array data type
        # TODO 2019-06-16 use Enum for colors
        if len(values) != GUESS_LENGTH:
            raise InvalidGuessLength()
        self._values = values

    @property
    def values(self):
        return self._values

    def eval(self, secret: 'Guess'):
        return Result(current=self, secret=secret)

    def __eq__(self, other):
        return self.values == other.values


class Result:
    def __init__(self, secret: Guess, current: Guess) -> None:
        self._secret = secret
        self._current = current
        self._blacks = self._compute_blacks()
        self._whites = self._compute_whites()
        self._values = self._compute_values()

    @property
    def values(self) -> list:
        return self._values

    def guessed(self) -> bool:
        return len(self._blacks) == GUESS_LENGTH

    def _compute_blacks(self):
        return [
            1
            for secret_item, current_guess_item in zip(self._secret.values, self._current.values)
            if secret_item == current_guess_item
        ]

    def _compute_whites(self):
        whites = []
        secret_cpy = self._secret.values.copy()
        for guess_item in self._current.values:
            if guess_item in secret_cpy:
                secret_cpy[secret_cpy.index(guess_item)] = None
                whites.append(0)

        return whites

    def _compute_values(self):
        return self._whites if len(self._blacks) == 0 else self._blacks + self._whites[:-len(self._blacks)]
