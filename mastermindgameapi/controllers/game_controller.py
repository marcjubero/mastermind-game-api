import json

from flask import Blueprint, request, make_response
from flask_restful import Api, Resource

from mastermindgameapi.data.repository.game_repository import GameRepository
from mastermindgameapi.data.repository.guess_repository import GuessRepository
from mastermindgameapi.models.exceptions import InvalidGuessLength
from mastermindgameapi.models.game import Game
from mastermindgameapi.models.guess import Guess

bp = Blueprint('game', __name__)
api = Api(bp)


class GamesController(Resource):
    def __init__(self) -> None:
        super().__init__()
        self._game_repo = GameRepository()

    def post(self):
        json_data = request.get_json() or {}
        try:
            secret = Guess(json_data.get('secret', []))
            game = self._game_repo.create(Game(secret=secret))

            response = make_response(json.dumps(self._game_repo.dump(game)), 201)
            response.headers['Content-Type'] = 'application/json'
            return response
        except InvalidGuessLength as e:
            return make_response(e.args[0], 400)
        except Exception as e:
            return make_response(e.args[0], 500)

    def get(self):
        pass


class GameController(Resource):
    def get(self, game_id):
        pass


class GameGuessController(Resource):
    def post(self, game_id):
        pass


api.add_resource(GamesController, '/games')
api.add_resource(GameController, '/games/<int:game_id>')
api.add_resource(GameGuessController, '/games/<int:game_id>/guess')
