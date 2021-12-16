import pytest

def test_landing(test_client):
  """
  GIVEN a Flask application configured for testing
  WHEN the '/' page is requested (GET)
  THEN check that the response is valid
  """
  response = test_client.get("/")

  assert response.status_code == 200
  assert b"I'm CROW" in response.data