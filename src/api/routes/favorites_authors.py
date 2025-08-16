from flask import Blueprint,jsonify,request
from flask_cors import CORS
from api.models import User ,Book, Author ,db

favorites_authors_bp= Blueprint("favorites_authors", __name__, url_prefix="/favorites_authors")

CORS(favorites_authors_bp)

@favorites_authors_bp.route("/<int:user_id>", methods=["GET"])
def get_favorite_authors(user_id):
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"msg": "Usuario no encontrado"}), 404

    favorite_authors = user.favo_author or []

    if not favorite_authors:
        return jsonify({"msg": "El usuario no tiene autores favoritos"}), 200

    return jsonify({
        "msg": "Autores favoritos obtenidos correctamente",
        "favorite_authors": [author.serialize() for author in favorite_authors]
    }), 200


@favorites_authors_bp.route("/<int:user_id>/<int:author_id>", methods=["POST"])
def add_favorite_author(user_id, author_id):
    user = db.session.get(User, user_id)
    author = db.session.get(Author, author_id)

    if not user or not author:
        return jsonify({"msg": "Usuario o autor no encontrado"}), 404

    if author in user.favo_author:
        return jsonify({"msg": "El autor ya está en favoritos"}), 200

    user.favo_author.append(author)
    db.session.commit()

    return jsonify({"msg": "Autor agregado a favoritos"}), 201


@favorites_authors_bp.route("/<int:user_id>/<int:author_id>", methods=["DELETE"])
def remove_favorite_author(user_id, author_id):
    user = db.session.get(User, user_id)
    author = db.session.get(Author, author_id)

    if not user or not author:
        return jsonify({"msg": "Usuario o autor no encontrado"}), 404

    if author not in user.favo_author:
        return jsonify({"msg": "El autor no está en favoritos"}), 404

    user.favo_author.remove(author)
    db.session.commit()

    return jsonify({"msg": "Autor eliminado de favoritos"}), 200