from os.path import join, dirname, abspath

import pytest

from mastermindgameapi.models.exceptions import InvalidGuessLength
from mastermindgameapi.models.guess import Guess, Result
from tests.helpers.utils import parametrize_from_json_file

CURRENT_DIR = abspath(dirname(__file__))


class TestGuessModel:
    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            'input_guess',
            fpath=join(CURRENT_DIR, 'test_cases/test_guess_model.json'),
            test_class_name='TestGuessModel',
            test_class_method='raise_when_invalid_length'
        ))
    def test_raise_when_invalid_length(self, input_guess):
        with pytest.raises(InvalidGuessLength) as _:
            Guess(input_guess)

    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            'input_guess, expected',
            fpath=join(CURRENT_DIR, 'test_cases/test_guess_model.json'),
            test_class_name='TestGuessModel',
            test_class_method='guess_creation'
        ))
    def test_guess_creation(self, input_guess, expected):
        guess = Guess(input_guess)
        expected_guess = Guess(expected)
        assert guess == expected_guess

    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            'input_guess, expected',
            fpath=join(CURRENT_DIR, 'test_cases/test_guess_model.json'),
            test_class_name='TestGuessModel',
            test_class_method='values'
        ))
    def test_values(self, input_guess, expected):
        guess = Guess(input_guess)
        assert guess.values == expected

    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            'input_guess, secret',
            fpath=join(CURRENT_DIR, 'test_cases/test_guess_model.json'),
            test_class_name='TestGuessModel',
            test_class_method='eval'
        ))
    def test_eval(self, input_guess, secret):
        res = Guess(input_guess).eval(Guess(secret))
        assert isinstance(res, Result)
