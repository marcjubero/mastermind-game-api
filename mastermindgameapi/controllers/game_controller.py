from flask import Blueprint
from flask_restful import Api, Resource

bp = Blueprint('otp', __name__)
api = Api(bp)


class GamesController(Resource):
    def post(self):
        pass

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
