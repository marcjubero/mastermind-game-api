from mastermindgameapi.models.guess import Guess, Result


class Mastermind:
    def __init__(self, secret: Guess) -> None:
        self._secret = secret

    def eval_guess(self, guess: Guess) -> Result:
        if len(guess.values) != len(self._secret.values):
            raise Exception()  # TODO

        return guess.eval(self._secret)

        # secret_cpy = self._secret.copy()
        #
        # blacks = [1 for secret, guess_item in zip(secret_cpy, guess) if secret == guess_item]
        #
        # whites = []
        # for guess_item in guess:
        #     if guess_item in secret_cpy:
        #         secret_cpy[secret_cpy.index(guess_item)] = None
        #         whites.append(0)
        #
        # return whites if len(blacks) == 0 else blacks + whites[:-len(blacks)]
