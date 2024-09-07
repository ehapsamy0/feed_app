from flask import Blueprint, request, jsonify
from app.db_config import get_db
from app.services.post_service import (
    create_new_post,
    get_post,
    update_existing_post,
    delete_existing_post,
    get_all_posts_service,
)

post_bp = Blueprint("post", __name__)


@post_bp.route("/posts", methods=["GET"])
def get_all_posts_route():
    db = get_db()
    posts = get_all_posts_service(db)
    return jsonify(posts), 200


# Create Post
@post_bp.route("/posts", methods=["POST"])
def create_post_route():
    """
    Endpoint to create a new post.

    Currently, `user_id` is expected to be provided in the request body.
    In the future, we will fetch `user_id` from the request authentication service.
    """

    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400

    data = request.get_json()
    if not data:
        return jsonify({"error": "Empty request body"}), 400

    title = data.get("title")
    content = data.get("content")

    # Validate required fields
    if not all([title, content]):
        return jsonify(
            {"error": "Missing required fields: title, or content"}
        ), 400
    db = get_db()

    user_id =None
    result = create_new_post(db, title, user_id, content)

    return jsonify(result), 201

@post_bp.route("/posts/<uuid:post_id>", methods=["GET"])
def get_post_route(post_id):
    db = get_db()
    post = get_post(db, str(post_id))
    if post:
        return jsonify(post), 200
    return jsonify({"error": "Post not found"}), 404

@post_bp.route("/posts/<uuid:post_id>", methods=["PUT"])
def update_post_route(post_id):
    """
    Endpoint to update a post by its UUID.
    """
    if not request.is_json:
        return jsonify({"error": "Request body must be JSON"}), 400

    data = request.get_json()
    content = data.get("content")

    if not content:
        return jsonify({"error": "Missing required field: content"}), 400

    db = get_db()
    result = update_existing_post(db, str(post_id), content)
    if result:
        return jsonify(result), 200
    return jsonify({"error": "Post not found"}), 404



@post_bp.route("/posts/<uuid:post_id>", methods=["DELETE"])
def delete_post_route(post_id):
    """
    Endpoint to delete a post by its UUID (soft delete).
    """
    db = get_db()
    result = delete_existing_post(db, str(post_id))
    if result:
        return jsonify(result), 200
    return jsonify({"error": "Post not found"}), 404