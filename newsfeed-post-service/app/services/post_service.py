from app.repositories.post_repository import (
    create_post,
    get_post_by_id,
    update_post,
    delete_post,
)


from app.repositories.post_repository import get_all_posts


def get_all_posts_service(db):
    posts = get_all_posts(db)
    return posts if posts else []


def create_new_post(db, title, user_id, content):
    post_id, title = create_post(db, title, user_id, content)
    return {"post_id": post_id,"title":title, "message": "Post created successfully!"}


def get_post(db, post_id):
    post = get_post_by_id(db, post_id)
    if not post:
        return None
    return post


def update_existing_post(db, post_id, content):
    post = get_post_by_id(db, post_id)
    if not post:
        return None
    update_post(db, post_id, content)
    return {"message": "Post updated successfully!"}


def delete_existing_post(db, post_id):
    post = get_post_by_id(db, post_id)
    if not post:
        return None
    delete_post(db, post_id)
    return {"message": "Post deleted successfully!"}
