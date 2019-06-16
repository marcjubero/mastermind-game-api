from os.path import join, dirname, abspath

import pytest

from mastermindgameapi.models.game import Mastermind
from mastermindgameapi.models.guess import Guess
from tests.helpers.utils import parametrize_from_json_file

CURRENT_DIR = abspath(dirname(__file__))


class TestGameService:
    def _service(self, secret):
        return Mastermind(secret)

    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            'input_secret, input_guess, expected',
            fpath=join(CURRENT_DIR, 'test_cases/test_game_service.json'),
            test_class_name='TestGameService',
            test_class_method='eval_guess'
        ))
    def test_eval_guess(self, input_secret, input_guess, expected):
        secret = Guess(input_secret)
        guess = Guess(input_guess)
        result = self._service(secret).eval_guess(guess)
        assert result.values == expected
