import uuid


def get_all_posts(db):
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM posts WHERE is_deleted = FALSE"
    cursor.execute(query)
    posts = cursor.fetchall()
    cursor.close()
    return posts


def create_post(db, title, user_id, content):
    cursor = db.cursor()
    post_id = str(uuid.uuid4())
    query = """
    INSERT INTO posts (id, title, user_id, content, created_at, updated_at, is_deleted)
    VALUES (%s, %s, %s, %s, NOW(), NOW(), FALSE)
    """
    cursor.execute(query, (post_id, title, user_id, content))
    db.commit()
    post_id = cursor.lastrowid
    cursor.close()
    return post_id


def get_post_by_id(db, post_id):
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM posts WHERE id = %s AND is_deleted = FALSE"
    cursor.execute(query, (post_id,))
    post = cursor.fetchone()
    cursor.close()
    return post


def update_post(db, post_id, content):
    cursor = db.cursor()
    query = "UPDATE posts SET content = %s, updated_at = NOW() WHERE id = %s AND is_deleted = FALSE"
    cursor.execute(query, (content, post_id))
    db.commit()
    cursor.close()


def delete_post(db, post_id):
    cursor = db.cursor()
    query = "UPDATE posts SET is_deleted = TRUE WHERE id = %s"
    cursor.execute(query, (post_id,))
    db.commit()
    cursor.close()
