import os

from flask import Flask

from mastermindgameapi.config.config_factory import ConfigFactory


def create_app(config_class=None):
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV', 'local')
    cfg = ConfigFactory.get_config(env_name=env) if config_class is None else config_class

    app.config.from_object(cfg)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(port=os.getenv('FLASK_PORT', 8080))
