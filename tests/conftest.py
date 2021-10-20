import pytest

from crow.app import create_app

@pytest.fixture(scope="module")
def test_client():
  _app = create_app("flask_test.cfg")

  with _app.test_client() as test_client:
    with _app.app_context():
      yield test_client