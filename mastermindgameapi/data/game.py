from mastermindgameapi.app import db


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    secret = db.Column(db.String, nullable=False)
    games = db.relationship('Guesses', backref='game', lazy=True)
