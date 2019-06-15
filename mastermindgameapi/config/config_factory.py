from mastermindgameapi.config.local_config import LocalDevConfig
from mastermindgameapi.config.test_config import TestConfig


class ConfigFactory:
    _CONFIG_CLASSES = {
        'local': LocalDevConfig,
        'test': TestConfig
    }

    @classmethod
    def get_config(cls, env_name=None):
        return cls._CONFIG_CLASSES.get(env_name, None)()
