from os.path import join, dirname, abspath

import pytest

from mastermindgameapi.data.game import Game as GameData
from mastermindgameapi.models.game import Game
from mastermindgameapi.models.guess import Guess
from tests.helpers.utils import parametrize_from_json_file

CURRENT_DIR = abspath(dirname(__file__))


class TestGameModel:
    def _service(self, secret):
        return Game(secret)

    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            'input_secret, input_guess, expected',
            fpath=join(CURRENT_DIR, 'test_cases/test_game_model.json'),
            test_class_name='TestGameService',
            test_class_method='eval_guess'
        ))
    def test_eval_guess(self, input_secret, input_guess, expected):
        secret = Guess(input_secret)
        guess = Guess(input_guess)
        result = self._service(secret).eval_guess(guess)
        assert result.values == expected

    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            'input_secret, expected',
            fpath=join(CURRENT_DIR, 'test_cases/test_game_model.json'),
            test_class_name='TestGameService',
            test_class_method='secret_raw_values'
        ))
    def test_secret_raw_values(self, input_secret, expected):
        secret = Guess(input_secret)
        result = self._service(secret).secret_raw_values
        assert result == expected

    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            'input_secret, expected',
            fpath=join(CURRENT_DIR, 'test_cases/test_game_model.json'),
            test_class_name='TestGameService',
            test_class_method='from_data'
        ))
    def test_from_data(self, input_secret, expected):
        game_data = GameData(secret=';'.join(input_secret))
        result = Game.from_data(game_data)
        assert isinstance(result, Game)
        assert result.secret_raw_values == expected
