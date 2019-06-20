from mastermindgameapi.app import db
from mastermindgameapi.data.game import Game as GameData
from mastermindgameapi.data.guess import Guess as GuessData
from mastermindgameapi.data.repository.base_repository import BaseRepository
from mastermindgameapi.models.guess import Guess as GuessModel
from mastermindgameapi.models.game import Game as GameModel


class GuessRepository(BaseRepository):
    __model__ = GuessData

    def create(self, model: GuessModel, game: GameData, **kwargs):
        g = GuessData(value=';'.join(str(x) for x in model.values), game=game)

        db.session.add(g)
        self.save()

        return g

    def dump(self, data: GuessData):
        guess_value = data.value.split(';')
        return {
            "id": data.id,
            "value": guess_value,
            "result": GameModel.from_data(data.game).eval_guess(GuessModel(guess_value)).values
        }
