from mastermindgameapi.config.base_config import BaseConfig


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mastermind_test.db'
