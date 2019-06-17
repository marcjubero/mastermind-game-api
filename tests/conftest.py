from os.path import dirname, abspath

import pytest

from mastermindgameapi.app import create_app, db as _db
from mastermindgameapi.config.test_config import TestConfig

CURRENT_DIR = abspath(dirname(__file__))


@pytest.fixture(scope='module')
def db(app, request):
    """Module-wide test database."""

    def teardown():
        _db.session.close_all()
        _db.session.close()
        _db.drop_all()

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='module')
def app(request):
    """Session-wide test database."""
    app = create_app(TestConfig)

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def removing_context():
        ctx.pop()

    request.addfinalizer(removing_context)
    return app
