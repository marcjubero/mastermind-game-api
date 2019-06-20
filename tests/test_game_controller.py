from os.path import join, abspath, dirname

import pytest

from mastermindgameapi.data.game import Game
from mastermindgameapi.data.guess import Guess
from tests.helpers.base_controller_test import BaseControllerTest
from tests.helpers.utils import parametrize_from_json_file

CURRENT_DIR = abspath(dirname(__file__))


@pytest.fixture(autouse=True, scope="module")
def load_base_data(db):
    datas = [
        Game(secret='RED;GREEN;BLUE;YELLOW'),
        Game(secret='RED;GREEN;GREEN;BLUE', guesses=[
            Guess(value='YELLOW;GREEN;YELLOW;RED'),
            Guess(value='YELLOW;GREEN;YELLOW;RED'),
            Guess(value='YELLOW;GREEN;YELLOW;RED'),
            Guess(value='YELLOW;GREEN;YELLOW;RED'),
            Guess(value='YELLOW;GREEN;YELLOW;RED'),
            Guess(value='YELLOW;GREEN;YELLOW;RED'),
            Guess(value='YELLOW;GREEN;YELLOW;RED'),
            Guess(value='YELLOW;GREEN;YELLOW;RED'),
            Guess(value='YELLOW;GREEN;YELLOW;RED'),
            Guess(value='YELLOW;GREEN;YELLOW;RED'),
            Guess(value='YELLOW;GREEN;YELLOW;RED'),
            Guess(value='YELLOW;GREEN;YELLOW;RED')
        ])
    ]

    db.session.add_all(datas)
    db.session.commit()
    db.session.expunge_all()


class TestGameController(BaseControllerTest):
    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            fpath=join(CURRENT_DIR, 'test_cases/test_game_controller.json'),
            test_class_name='TestGameController',
            test_class_method='new_game'
        ))
    def test_new_game(self, method, url, headers, url_parameters, data, query_string, status_code, response_data,
                      config, app, mocker):
        self._run_standard_test(
            method=method,
            url=url,
            headers=headers,
            url_parameters=url_parameters,
            data=data,
            query_string=query_string,
            status_code=status_code,
            response_data=response_data,
            config=config,
            app=app)

    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            fpath=join(CURRENT_DIR, 'test_cases/test_game_controller.json'),
            test_class_name='TestGameController',
            test_class_method='get_single_game'
        ))
    def test_get_single_game(self, method, url, headers, url_parameters, data, query_string, status_code, response_data,
                             config, app, mocker):
        self._run_standard_test(
            method=method,
            url=url,
            headers=headers,
            url_parameters=url_parameters,
            data=data,
            query_string=query_string,
            status_code=status_code,
            response_data=response_data,
            config=config,
            app=app)

    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            fpath=join(CURRENT_DIR, 'test_cases/test_game_controller.json'),
            test_class_name='TestGameController',
            test_class_method='new_guess'
        ))
    def test_new_guess(self, method, url, headers, url_parameters, data, query_string, status_code, response_data,
                       config, app, mocker):
        self._run_standard_test(
            method=method,
            url=url,
            headers=headers,
            url_parameters=url_parameters,
            data=data,
            query_string=query_string,
            status_code=status_code,
            response_data=response_data,
            config=config,
            app=app)
