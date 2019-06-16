class BaseConfig:
    DEBUG = False
    ERROR_404_HELP = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mastermind.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GUESS_LENGTH = 4
