import os

from flask import Flask

from mastermindgameapi.config.config_factory import ConfigFactory


def create_app(config_class=None):
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV', 'localdev')
    cfg = config_class if config_class is not None else ConfigFactory.get_config(env_name=env)

    app.config.from_object(cfg)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(port=os.getenv('FLASK_PORT', 8080))
