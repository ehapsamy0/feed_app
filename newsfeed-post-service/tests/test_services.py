from app.services.post_service import create_new_post, get_post, update_existing_post, delete_existing_post
from app.db_config import get_db
import uuid

def test_create_post_service(client):
    db = get_db()
    result = create_new_post(db, 'Test Title', 'user_id', 'This is test content')
    assert 'post_id' in result
    assert result["title"] == "Test Title"



def test_get_post_service_not_found(client):
    db = get_db()
    post_id = str(uuid.uuid4())  # Example UUID
    post = get_post(db, post_id)
    assert post is None  # No post exists


def test_get_post_service(client, create_post):
    db = get_db()
    post_id = create_post
    post = get_post(db, post_id)
    assert post["id"] == post_id 

def test_update_post_service(client, create_post):
    db = get_db()
    post_id = create_post
    result = update_existing_post(db, post_id, 'Updated content')
    assert result['message'] == "Post updated successfully!"

def test_delete_post_service(client, create_post):
    db = get_db()
    post_id = create_post
    result = delete_existing_post(db, post_id)
    assert result['message'] == "Post deleted successfully!"
