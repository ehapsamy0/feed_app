import pytest
from app import create_app
from app.db_config import get_db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture
def create_post(client):
    response = client.post('/posts', json={
        'title': 'Test Post',
        'content': 'This is the content of the test post.'
    })
    data = response.get_json()
    post_id = data['post_id']
    return post_id