from mastermindgameapi.app import db


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    secret = db.Column(db.String, nullable=False)

    guesses = db.relationship('Guess', backref=db.backref('game', lazy=True), lazy=True)
