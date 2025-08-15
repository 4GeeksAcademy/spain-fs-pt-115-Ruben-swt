from typing import List
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey,Column,Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()



favorites_books = Table(
    "favorites_books",
    db.Model.metadata,
    Column("user_id", ForeignKey("user.id",ondelete="CASCADE"), primary_key=True ),
    Column("book_id", ForeignKey("book.id",ondelete="CASCADE"), primary_key=True ),
)
favorites_author = Table(
    "favorites_author",
    db.Model.metadata,
    Column("user_id", ForeignKey("user.id", ondelete="CASCADE"), primary_key=True),
    Column("author_id", ForeignKey("author.id", ondelete="CASCADE"), primary_key=True),
)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favo_book: Mapped[List["Book"]] = relationship(secondary= "favorites_books", passive_deletes=True)
    favo_author: Mapped[List["Author"]] = relationship(secondary= "favorites_author",passive_deletes=True)

    def serialize(self):
        try:
            f_authors = [a.serialize() for a in self.favo_author]
        except Exception:
            f_authors = None

        try:
            f_books = [b.serialize() for b in self.favo_book]
        except Exception:
            f_books = None
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "favorite_author":f_authors,
            "favorite_books": f_books,
        }

class Author(db.Model):
    id: Mapped[int]= mapped_column(primary_key=True)
    complete_name: Mapped[str] = mapped_column(String(120),nullable=False)
    books: Mapped[List["Book"]] = relationship("Book",back_populates="author", cascade="all, delete", passive_deletes=True)

    def serialize(self):
        return {
            "id":self.id,
            "complete_name": self.complete_name,
            "books":[b.serialize()["title"]for b in self.books]
        }

class Book (db.Model):
    id: Mapped[int]= mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120), nullable=False)
    cover: Mapped[str] = mapped_column(String(120),  nullable=False)
    description:Mapped[str] = mapped_column(String(120), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id", ondelete="CASCADE"))
    author: Mapped["Author"] = relationship("Author", back_populates="books")

    def serialize(self):
        return {
            "id":self.id, 
            "author_id":self.author_id,
            "title": self.title,
            "cover": self.cover,
            "description": self.description,
            "author":self.author.complete_name,
        }
