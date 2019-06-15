class GameService:

    def __init__(self) -> None:
        pass

    def eval_guess(self, secret_code, guess):
        secret_cpy = secret_code.copy()

        blacks = [1 for secret, guess_item in zip(secret_cpy, guess) if secret == guess_item]

        whites = []
        for g in guess:
            if g in secret_cpy:
                secret_cpy[secret_cpy.index(g)] = None
                whites.append(0)

        return whites if len(blacks) == 0 else (blacks + whites[:-len(blacks)])
