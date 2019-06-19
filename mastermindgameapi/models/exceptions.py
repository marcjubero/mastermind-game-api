from mastermindgameapi.config.game_config import GUESS_LENGTH


class InvalidGuessLength(AttributeError):
    def __init__(self, message: str = 'Guess length must be {0}'.format(GUESS_LENGTH)) -> None:
        super().__init__(message)


class FinishedGameException(Exception):
    def __init__(self, message: str = 'Guess length must be {0}'.format(GUESS_LENGTH)) -> None:
        super().__init__(message)
