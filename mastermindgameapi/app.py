import os

from flask import Flask
from werkzeug.utils import import_string, find_modules

from mastermindgameapi.config.config_factory import ConfigFactory

APPNAME = 'mastermindgameapi'


def register_blueprints(app):
    """Register all blueprint modules

    Reference: Armin Ronacher, "Flask for Fun and for Profit" PyBay 2016.
    """
    for name in find_modules(APPNAME + '.controllers'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            prefix = mod.prefix if hasattr(mod, 'prefix') else app.config.get('API_VERSION', 'v1')
            app.register_blueprint(mod.bp, url_prefix='/{0}'.format(prefix))

    return None


def create_app(config_class=None):
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV', 'local')
    cfg = ConfigFactory.get_config(env_name=env) if config_class is None else config_class

    app.config.from_object(cfg)

    register_blueprints(app=app)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(port=os.getenv('FLASK_PORT', 8080))
