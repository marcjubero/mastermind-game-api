from mastermindgameapi.app import db
from mastermindgameapi.data.game import Game as GameData
from mastermindgameapi.data.guess import Guess as GuessData
from mastermindgameapi.data.repository.base_repository import BaseRepository
from mastermindgameapi.models.guess import Guess as GuessModel


class GuessRepository(BaseRepository):
    __model__ = GuessData

    def create(self, model: GuessModel, game: GameData):
        g = GuessData(value=';'.join(str(x) for x in model.values), game=game)

        db.session.add(g)
        db.session.commit()

        return g

    def dump(self, data: GuessData):
        pass
