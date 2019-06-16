from mastermindgameapi.models.guess import Guess, Result


class Mastermind:
    def __init__(self, secret: Guess) -> None:
        self._secret = secret

    def eval_guess(self, guess: Guess) -> Result:
        return guess.eval(self._secret)
