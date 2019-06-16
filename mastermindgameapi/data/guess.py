from mastermindgameapi.app import db


class Guess(db.Model):
    __tablename__ = 'guesses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.String, nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
