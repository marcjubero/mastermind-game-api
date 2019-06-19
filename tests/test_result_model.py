from os.path import join, dirname, abspath

import pytest

from mastermindgameapi.models.guess import Guess, Result
from tests.helpers.utils import parametrize_from_json_file

CURRENT_DIR = abspath(dirname(__file__))


class TestResultModel:
    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            'input_secret, input_guess, expected',
            fpath=join(CURRENT_DIR, 'test_cases/test_result_model.json'),
            test_class_name='TestResultModel',
            test_class_method='values'
        ))
    def test_values(self, input_secret, input_guess, expected):
        secret = Guess(input_secret)
        guess = Guess(input_guess)
        assert Result(secret=secret, current=guess).values == expected

    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            'input_secret, input_guess, expected',
            fpath=join(CURRENT_DIR, 'test_cases/test_result_model.json'),
            test_class_name='TestResultModel',
            test_class_method='guessed'
        ))
    def test_guessed(self, input_secret, input_guess, expected):
        secret = Guess(input_secret)
        guess = Guess(input_guess)
        assert Result(secret=secret, current=guess).guessed() == expected
