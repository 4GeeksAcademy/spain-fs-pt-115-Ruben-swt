from flask import Blueprint
from .user_routes import user_bp
from .author_routes import author_bp 
from .book_routes import book_bp
from .favorites_books import favorites_books_bp
from .favorites_authors import favorites_authors_bp
api= Blueprint("api", __name__)



api.register_blueprint(user_bp)
api.register_blueprint(author_bp)
api.register_blueprint(book_bp)
api.register_blueprint(favorites_books_bp)
api.register_blueprint(favorites_authors_bp)