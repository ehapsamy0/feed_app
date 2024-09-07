import uuid

def test_create_post(client):
    response = client.post('/posts', json={
        'title': 'Test Post',
        'content': 'This is the content of the test post.'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert 'post_id' in data
    assert data["title"] in "Test Post"

def test_get_post_not_found(client):
    post_id = str(uuid.uuid4())
    response = client.get(f'/posts/{post_id}')
    assert response.status_code == 404  # No post exists initially


def test_get_post(client, create_post):
    post_id = create_post
    response = client.get(f'/posts/{post_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == post_id

def test_update_post(client, create_post):
    post_id = create_post
    response = client.put(f'/posts/{post_id}', json={
        'content': 'Updated content of the test post.'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Post updated successfully!'

def test_delete_post(client, create_post):
    post_id = create_post
    response = client.delete(f'/posts/{post_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Post deleted successfully!'