import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string, find_modules

from mastermindgameapi.config.config_factory import ConfigFactory

APPNAME = 'mastermindgameapi'

db = SQLAlchemy()


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


def register_elements(package):
    """Register additional stuff

    Args:
        package (str): package name
    """
    for name in find_modules('{}.{}'.format(APPNAME, package)):
        import_string(name)


def create_app(config_class=None):
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV', 'local')
    cfg = ConfigFactory.get_config(env_name=env) if config_class is None else config_class

    app.config.from_object(cfg)

    db.init_app(app)
    register_blueprints(app=app)
    register_elements('data')

    db.create_all(app=app)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(port=os.getenv('FLASK_PORT', 8080))  # pragma: no cover
