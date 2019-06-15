import pytest

from mastermindgameapi.app import create_app
from mastermindgameapi.config.test_config import TestConfig


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
