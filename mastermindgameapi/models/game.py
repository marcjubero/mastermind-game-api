from mastermindgameapi.models.guess import Guess, Result


class Game:
    def __init__(self, secret: Guess) -> None:
        self._secret = secret

    @property
    def secret_raw_values(self):
        return self._secret.values

    def eval_guess(self, guess: Guess) -> Result:
        return guess.eval(self._secret)
