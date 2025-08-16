from flask import Blueprint,jsonify,request
from flask_cors import CORS
from api.models import User ,Book ,db

favorites_books_bp= Blueprint("favorites_books", __name__, url_prefix="/favorites_books")

CORS(favorites_books_bp)

@favorites_books_bp.route("/<int:user_id>", methods=["GET"])
def get_favorite_books(user_id):
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"msg": "Usuario no encontrado"}), 404

    favorite_books = user.favo_book or []

    if not favorite_books:
        return jsonify({"msg": "El usuario no tiene libros favoritos"}), 200

    return jsonify({
        "msg": "Libros favoritos obtenidos correctamente",
        "favorite_books": [book.serialize() for book in favorite_books]
    }), 200

@favorites_books_bp.route("/<int:user_id>/<int:book_id>", methods=["POST"])
def add_favorite_book(user_id, book_id):
    user = db.session.get(User, user_id)
    book = db.session.get(Book, book_id)

    if not user or not book:
        return jsonify({"msg": "Usuario o libro no encontrado"}), 404

    if book in user.favo_book:
        return jsonify({"msg": "El libro ya está en favoritos"}), 200

    user.favo_book.append(book)
    db.session.commit()

    return jsonify({"msg": "Libro agregado a favoritos"}), 201

@favorites_books_bp.route("/<int:user_id>/<int:book_id>", methods=["DELETE"])
def remove_favorite_book(user_id, book_id):
    user = db.session.get(User, user_id)
    book = db.session.get(Book, book_id)

    if not user or not book:
        return jsonify({"msg": "Usuario o libro no encontrado"}), 404

    if book not in user.favo_book:
        return jsonify({"msg": "El libro no está en favoritos"}), 404

    user.favo_book.remove(book)
    db.session.commit()

    return jsonify({"msg": "Libro eliminado de favoritos"}), 200