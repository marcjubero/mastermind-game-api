from os.path import abspath, dirname, join

import pytest

from tests.helpers.base_controller_test import BaseControllerTest
from tests.helpers.utils import parametrize_from_json_file

CURRENT_DIR = abspath(dirname(__file__))


class TestBoardController(BaseControllerTest):
    @pytest.mark.parametrize(
        **parametrize_from_json_file(
            fpath=join(CURRENT_DIR, 'test_cases/test_board_controller.json'),
            test_class_name='TestBoardController',
            test_class_method='get_games_historic'
        ))
    def test_get_games(self, method, url, headers, url_parameters, data, query_string, status_code, response_data,
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
