import pytest

from os.path import join, dirname, abspath

from mastermindgameapi.services.game_service import GameService
from tests.helpers.utils import parametrize_from_json_file

CURRENT_DIR = abspath(dirname(__file__))


class TestGameService:
    def _service(self):
        return GameService()

    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            'input_secret, input_guess, expected',
            fpath=join(CURRENT_DIR, 'test_cases/test_game_service.json'),
            test_class_name='TestGameService',
            test_class_method='eval_guess'
        ))
    def test_eval_guess(self, input_secret, input_guess, expected):
        result = self._service().eval_guess(input_secret, input_guess)
        assert result == expected
