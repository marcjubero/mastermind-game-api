from mastermindgameapi.config.local_config import LocalDevConfig


class ConfigFactory:
    _CONFIG_CLASSES = {
        'local_dev': LocalDevConfig
    }

    @classmethod
    def get_config(cls, env_name=None):
        return cls._CONFIG_CLASSES.get(env_name, None)
