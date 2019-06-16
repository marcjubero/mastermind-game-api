from mastermindgameapi.app import db
from mastermindgameapi.data.game import Game as GameData
from mastermindgameapi.data.repository.base_repository import BaseRepository
from mastermindgameapi.models.game import Game as GameModel


class GameRepository(BaseRepository):
    __model__ = GameData

    def create(self, model: GameModel) -> GameData:
        m = GameData(secret=';'.join(str(x) for x in model.secret_raw_values))
        db.session.add(m)
        db.session.commit()

        return m

    def dump(self, model: GameData) -> dict:
        return {
            'id': model.id,
            'secret': model.secret.split(';'),
            'guesses': [{'id': g.id, 'value': g.value.split(';')} for g in model.guesses]
        }
