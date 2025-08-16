from flask import Blueprint,jsonify,request
from flask_cors import CORS
from api.models import Book, Author ,db

book_bp= Blueprint("book", __name__, url_prefix="/books")

CORS(book_bp)

@book_bp.route("/", methods=["GET"])
def get_books():
    books= Book.query.all()
    return jsonify ([b.serialize()for b in books]),200

@book_bp.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book= Book.query.get(book_id)

    if book:
        return jsonify(book.serialize()),200
    return jsonify({"msg":"Libro no enciontrado."}),404

@book_bp.route("/<int:autor_id>", methods=["POST"])
def post_book(autor_id):
    books = db.session.query(Book).all()
    author =Author.query.get(autor_id)
    data= request.get_json()
    title =data.get("title")
    cover =data.get("cover")
    description =data.get("description")

    if not author:
        return jsonify({"msg":"Autor no encontrado."}),404
    if not title or not cover or not description:
        return jsonify({"msg":"Faltan datos por rellenar"}),404
    

    new_book = Book(
        title= title,
        cover=cover,
        description=description,
        author_id= author.id,
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"msg":"Libro registrado.", "book": new_book.serialize() }),201
    
@book_bp.route("/<int:autor_id>/<int:book_id>", methods=["DELETE"])
def delete_book(autor_id, book_id):
    author = Author.query.get(autor_id)
    book = Book.query.get(book_id)

    if not author:
        return jsonify({"msg": "Autor no encontrado."}), 404
    if not book:
        return jsonify({"msg": "Libro no encontrado."}), 404
    if book.author_id != author.id:# Verificar que el libro pertenece al autor
        return jsonify({"msg": "El libro no pertenece a este autor."}), 400

    db.session.delete(book)
    db.session.commit()
    return jsonify({"msg": "Libro eliminado correctamente."}), 200

@book_bp.route("/<int:autor_id>/<int:book_id>", methods=["PATCH"])
def update_book(autor_id, book_id):
    author = Author.query.get(autor_id)
    book = Book.query.get(book_id)
    data = request.get_json()
    title = data.get("title")
    cover = data.get("cover")
    description = data.get("description")

    if not author:
        return jsonify({"msg": "Autor no encontrado."}), 404
    if not book:
        return jsonify({"msg": "Libro no encontrado."}), 404
    if book.author_id != author.id:# Verificar que el libro pertenece al autor
        return jsonify({"msg": "El libro no pertenece a este autor."}), 400

    if title is not None:
        book.title = title
    if cover is not None:
        book.cover = cover
    if description is not None:
        book.description = description


    db.session.commit()
    return jsonify({"msg": "Libro actualizado correctamente.", "book": book.serialize()}), 200





         
    


