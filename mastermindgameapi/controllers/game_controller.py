import json

from flask import Blueprint, request, make_response
from flask_restful import Api, Resource

from mastermindgameapi.data.exceptions import DataNotFoundException
from mastermindgameapi.data.repository.game_repository import GameRepository
from mastermindgameapi.data.repository.guess_repository import GuessRepository
from mastermindgameapi.models.board import Board
from mastermindgameapi.models.exceptions import InvalidGuessLength, FinishedGameException
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
        except KeyError as e:
            return make_response('{0} is not a valid color'.format(e.args[0]), 400)
        except Exception as e:
            return make_response(e.args[0], 500)

    def get(self):
        serialized = [self._game_repo.dump(g) for g in self._game_repo.all()]
        response_data = (json.dumps(serialized), 200) if len(serialized) else ('', 204)
        response = make_response(response_data[0], response_data[1])
        response.headers['Content-Type'] = 'application/json'
        return response


class GameController(Resource):
    def __init__(self) -> None:
        super().__init__()
        self._game_repo = GameRepository()

    def get(self, game_id):
        try:
            game = self._game_repo.first_or_raise(**{'id': str(game_id)})
            response = make_response(json.dumps(self._game_repo.dump(game)))
            response.headers['Content-Type'] = 'application/json'
            return response
        except DataNotFoundException as _:
            return make_response('Game with id \'{0}\' not found'.format(game_id), 404)
        except Exception as e:
            return make_response(e.args[0], 500)


class GameGuessController(Resource):
    def __init__(self) -> None:
        super().__init__()
        self._game_repository = GameRepository()
        self._guess_repository = GuessRepository()

    def post(self, game_id):
        json_data = request.get_json() or {}
        try:
            g_data = self._game_repository.first_or_raise(**{'id': str(game_id)})

            guess = Guess(json_data.get('guess', []))

            board = Board(game=Game.from_data(g_data), turns=[Guess(g.value.split(';')) for g in g_data.guesses])
            result = board.new_turn(guess=guess)

            self._guess_repository.create(guess, g_data)

            return make_response(json.dumps({'result': result}))

        except DataNotFoundException as _:
            return make_response('Game with id \'{0}\' not found'.format(game_id), 404)
        except InvalidGuessLength as e:
            return make_response(e.args[0], 400)
        except FinishedGameException as e:
            return make_response(e.args[0], 400)
        except KeyError as e:
            return make_response('{0} is not a valid color'.format(e.args[0]), 400)
        except Exception as e:
            return make_response(e.args[0], 500)


api.add_resource(GamesController, '/games')
api.add_resource(GameController, '/games/<int:game_id>')
api.add_resource(GameGuessController, '/games/<int:game_id>/guesses')
