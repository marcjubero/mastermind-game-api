from os.path import join, dirname, abspath

import pytest

from mastermindgameapi.models.board import Board
from mastermindgameapi.models.exceptions import FinishedGameException
from mastermindgameapi.models.game import Game
from mastermindgameapi.models.guess import Guess
from tests.helpers.utils import parametrize_from_json_file

CURRENT_DIR = abspath(dirname(__file__))


class TestBoardModel:
    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            'input_secret, input_old_guesses, input_new_guess, expected_msg',
            fpath=join(CURRENT_DIR, 'test_cases/test_board_model.json'),
            test_class_name='TestBoardModel',
            test_class_method='new_turn_raise'
        ))
    def test_new_turn_raise_exception(self, input_secret, input_old_guesses, input_new_guess, expected_msg):
        with pytest.raises(FinishedGameException) as e:
            Board(
                game=Game(secret=Guess(input_secret)),
                turns=[Guess(g) for g in input_old_guesses]
            ).new_turn(guess=Guess(input_new_guess))
        assert e.value.args[0] == expected_msg
